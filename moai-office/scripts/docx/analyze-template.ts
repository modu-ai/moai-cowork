#!/usr/bin/env -S deno run --allow-read --allow-write
/**
 * analyze-template.ts — DOCX 템플릿 분석기
 *
 * DOCX 파일의 플레이스홀더, 스타일, 구조를 분석하여 보고서를 출력합니다.
 *
 * 사용 예시:
 *   deno run --allow-read analyze-template.ts ./template.docx
 *   deno run --allow-read analyze-template.ts ./template.docx --output report.json
 *   deno run --allow-read analyze-template.ts ./template.docx --format text
 *
 * 플레이스홀더 형식 지원:
 *   {{변수명}}, ${변수명}, <<변수명>>, [변수명]
 */

import { join } from "https://deno.land/std@0.224.0/path/mod.ts";

// ─────────────────────────────────────────────
// 타입 정의
// ─────────────────────────────────────────────

interface Placeholder {
  pattern: string;       // 원본 패턴 (예: {{회사명}})
  variableName: string;  // 변수명 (예: 회사명)
  format: PlaceholderFormat;
  occurrences: number;
  locations: string[];   // 발견 위치 설명
}

type PlaceholderFormat = "double-brace" | "dollar-brace" | "angle-bracket" | "square-bracket" | "unknown";

interface StyleInfo {
  name: string;
  basedOn?: string;
  isHeading: boolean;
  isList: boolean;
  isTable: boolean;
}

interface TemplateSection {
  type: "heading" | "paragraph" | "table" | "list" | "image";
  level?: number;         // 제목 레벨 (1-6)
  text?: string;          // 텍스트 미리보기 (최대 100자)
  placeholders: string[]; // 해당 섹션의 플레이스홀더 목록
}

interface AnalysisReport {
  filePath: string;
  analyzedAt: string;
  fileSize: number;
  placeholders: Placeholder[];
  styles: StyleInfo[];
  sections: TemplateSection[];
  summary: {
    totalPlaceholders: number;
    uniquePlaceholders: number;
    totalSections: number;
    hasKoreanText: boolean;
    estimatedPageCount: number;
  };
}

// ─────────────────────────────────────────────
// DOCX 파서 (ZIP 기반)
// ─────────────────────────────────────────────

/**
 * DOCX 파일에서 XML 콘텐츠를 추출합니다.
 * DOCX = ZIP 아카이브이며, word/document.xml이 본문입니다.
 */
async function extractDocxXml(filePath: string): Promise<{ document: string; styles: string }> {
  // Deno 내장 ZIP 지원 없으므로 unzip 명령어 사용
  const tmpDir = await Deno.makeTempDir({ prefix: "docx_analyze_" });

  try {
    const unzip = new Deno.Command("unzip", {
      args: ["-o", filePath, "word/document.xml", "word/styles.xml", "-d", tmpDir],
      stdout: "null",
      stderr: "null",
    });
    const { code } = await unzip.output();
    if (code !== 0) {
      throw new Error("DOCX 파일 압축 해제 실패. unzip이 설치되어 있는지 확인하세요.");
    }

    const documentXml = await Deno.readTextFile(join(tmpDir, "word", "document.xml"));
    let stylesXml = "";
    try {
      stylesXml = await Deno.readTextFile(join(tmpDir, "word", "styles.xml"));
    } catch {
      // styles.xml이 없는 경우 무시
    }

    return { document: documentXml, styles: stylesXml };
  } finally {
    await Deno.remove(tmpDir, { recursive: true });
  }
}

// ─────────────────────────────────────────────
// 플레이스홀더 탐지
// ─────────────────────────────────────────────

const PLACEHOLDER_PATTERNS: Array<{ regex: RegExp; format: PlaceholderFormat }> = [
  { regex: /\{\{([^}]+)\}\}/g,     format: "double-brace" },
  { regex: /\$\{([^}]+)\}/g,       format: "dollar-brace" },
  { regex: /<<([^>]+)>>/g,         format: "angle-bracket" },
  { regex: /\[([가-힣A-Za-z_][가-힣A-Za-z0-9_\s]*)\]/g, format: "square-bracket" },
];

function detectPlaceholders(text: string): Map<string, Placeholder> {
  const found = new Map<string, Placeholder>();

  for (const { regex, format } of PLACEHOLDER_PATTERNS) {
    for (const match of text.matchAll(regex)) {
      const pattern = match[0];
      const variableName = match[1].trim();
      const key = `${format}:${variableName}`;

      if (found.has(key)) {
        found.get(key)!.occurrences += 1;
      } else {
        found.set(key, {
          pattern,
          variableName,
          format,
          occurrences: 1,
          locations: [],
        });
      }
    }
  }

  return found;
}

// ─────────────────────────────────────────────
// XML → 구조 분석
// ─────────────────────────────────────────────

function stripXmlTags(xml: string): string {
  return xml.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
}

function parseSections(documentXml: string): TemplateSection[] {
  const sections: TemplateSection[] = [];

  // 단락 추출 (w:p 태그)
  const paragraphRegex = /<w:p[ >][\s\S]*?<\/w:p>/g;

  for (const match of documentXml.matchAll(paragraphRegex)) {
    const para = match[0];
    const text = stripXmlTags(para).trim();
    if (!text) continue;

    // 제목 스타일 감지 (w:pStyle)
    const styleMatch = para.match(/<w:pStyle w:val="([^"]+)"/);
    const styleName = styleMatch?.[1] ?? "";

    const headingMatch = styleName.match(/[Hh]eading(\d)|제목(\d)/);
    const isHeading = !!headingMatch;
    const headingLevel = headingMatch ? parseInt(headingMatch[1] || headingMatch[2]) : undefined;

    // 목록 감지
    const isList = /<w:numPr>/.test(para);

    // 플레이스홀더 탐지
    const ph = detectPlaceholders(text);
    const placeholderList = Array.from(ph.values()).map((p) => p.pattern);

    sections.push({
      type: isHeading ? "heading" : isList ? "list" : "paragraph",
      level: headingLevel,
      text: text.length > 100 ? text.slice(0, 97) + "..." : text,
      placeholders: placeholderList,
    });
  }

  // 표 감지 (w:tbl 태그)
  const tableRegex = /<w:tbl[ >][\s\S]*?<\/w:tbl>/g;
  for (const match of documentXml.matchAll(tableRegex)) {
    const tableText = stripXmlTags(match[0]);
    const ph = detectPlaceholders(tableText);
    sections.push({
      type: "table",
      text: tableText.length > 100 ? tableText.slice(0, 97) + "..." : tableText,
      placeholders: Array.from(ph.values()).map((p) => p.pattern),
    });
  }

  return sections;
}

function parseStyles(stylesXml: string): StyleInfo[] {
  const styles: StyleInfo[] = [];
  const styleRegex = /<w:style[^>]+>([\s\S]*?)<\/w:style>/g;

  for (const match of stylesXml.matchAll(styleRegex)) {
    const styleBlock = match[0];
    const nameMatch = styleBlock.match(/<w:name w:val="([^"]+)"/);
    const basedOnMatch = styleBlock.match(/<w:basedOn w:val="([^"]+)"/);
    const name = nameMatch?.[1] ?? "Unknown";

    styles.push({
      name,
      basedOn: basedOnMatch?.[1],
      isHeading: /heading|제목/i.test(name),
      isList: /list|목록/i.test(name),
      isTable: /table|표/i.test(name),
    });
  }

  return styles;
}

// ─────────────────────────────────────────────
// 메인 분석 함수
// ─────────────────────────────────────────────

async function analyzeTemplate(filePath: string): Promise<AnalysisReport> {
  const stat = await Deno.stat(filePath);
  const { document: documentXml, styles: stylesXml } = await extractDocxXml(filePath);

  const sections = parseSections(documentXml);
  const styles = parseStyles(stylesXml);

  // 전체 플레이스홀더 집계
  const allText = stripXmlTags(documentXml);
  const placeholdersMap = detectPlaceholders(allText);
  const placeholders = Array.from(placeholdersMap.values());

  // 섹션별 위치 정보 추가
  sections.forEach((sec, idx) => {
    sec.placeholders.forEach((ph) => {
      const key = [...placeholdersMap.entries()].find(([, v]) => v.pattern === ph)?.[0];
      if (key) {
        placeholdersMap.get(key)?.locations.push(`섹션 ${idx + 1}: ${sec.text?.slice(0, 40) ?? ""}`);
      }
    });
  });

  const hasKoreanText = /[가-힣]/.test(allText);
  const paragraphCount = (documentXml.match(/<w:p[ >]/g) ?? []).length;
  const estimatedPageCount = Math.max(1, Math.ceil(paragraphCount / 30));

  return {
    filePath,
    analyzedAt: new Date().toISOString(),
    fileSize: stat.size,
    placeholders,
    styles,
    sections,
    summary: {
      totalPlaceholders: placeholders.reduce((sum, p) => sum + p.occurrences, 0),
      uniquePlaceholders: placeholders.length,
      totalSections: sections.length,
      hasKoreanText,
      estimatedPageCount,
    },
  };
}

// ─────────────────────────────────────────────
// 출력 포맷터
// ─────────────────────────────────────────────

function formatTextReport(report: AnalysisReport): string {
  const lines: string[] = [];
  lines.push("═".repeat(60));
  lines.push("DOCX 템플릿 분석 보고서");
  lines.push("═".repeat(60));
  lines.push(`파일: ${report.filePath}`);
  lines.push(`분석 시각: ${report.analyzedAt}`);
  lines.push(`파일 크기: ${(report.fileSize / 1024).toFixed(1)} KB`);
  lines.push("");

  lines.push("[ 요약 ]");
  lines.push(`  플레이스홀더 총 개수: ${report.summary.totalPlaceholders}개`);
  lines.push(`  고유 플레이스홀더: ${report.summary.uniquePlaceholders}개`);
  lines.push(`  섹션 수: ${report.summary.totalSections}개`);
  lines.push(`  한글 포함: ${report.summary.hasKoreanText ? "예" : "아니오"}`);
  lines.push(`  예상 페이지 수: ${report.summary.estimatedPageCount}페이지`);
  lines.push("");

  if (report.placeholders.length > 0) {
    lines.push("[ 플레이스홀더 목록 ]");
    for (const ph of report.placeholders) {
      lines.push(`  ${ph.pattern} (형식: ${ph.format}, 발생 횟수: ${ph.occurrences})`);
    }
    lines.push("");
  }

  lines.push("[ 섹션 구조 ]");
  for (const sec of report.sections.slice(0, 20)) {
    const prefix = sec.type === "heading" ? `H${sec.level ?? "?"} ` : `  `;
    lines.push(`${prefix}[${sec.type}] ${sec.text ?? ""}`);
    if (sec.placeholders.length > 0) {
      lines.push(`       → 플레이스홀더: ${sec.placeholders.join(", ")}`);
    }
  }
  if (report.sections.length > 20) {
    lines.push(`  ... 외 ${report.sections.length - 20}개 섹션`);
  }

  lines.push("═".repeat(60));
  return lines.join("\n");
}

// ─────────────────────────────────────────────
// CLI 진입점
// ─────────────────────────────────────────────

async function main() {
  const args = Deno.args;
  if (args.length === 0 || args[0] === "--help" || args[0] === "-h") {
    console.log("사용법: analyze-template.ts <파일.docx> [--output 결과.json] [--format text|json]");
    Deno.exit(0);
  }

  const filePath = args[0];
  let outputPath: string | undefined;
  let format: "text" | "json" = "text";

  for (let i = 1; i < args.length; i++) {
    if (args[i] === "--output" && args[i + 1]) {
      outputPath = args[++i];
    } else if (args[i] === "--format" && args[i + 1]) {
      format = args[++i] as "text" | "json";
    }
  }

  try {
    console.log(`분석 중: ${filePath}`);
    const report = await analyzeTemplate(filePath);

    const output = format === "json"
      ? JSON.stringify(report, null, 2)
      : formatTextReport(report);

    if (outputPath) {
      await Deno.writeTextFile(outputPath, output, { create: true });
      console.log(`보고서 저장: ${outputPath}`);
    } else {
      console.log(output);
    }
  } catch (err) {
    console.error(`오류: ${err instanceof Error ? err.message : String(err)}`);
    Deno.exit(1);
  }
}

await main();
