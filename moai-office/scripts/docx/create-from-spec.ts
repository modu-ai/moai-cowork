#!/usr/bin/env -S deno run --allow-read --allow-write
/**
 * create-from-spec.ts — 스펙(JSON)에서 DOCX 문서 생성
 *
 * JSON 스펙 파일을 입력받아 구조화된 DOCX 문서를 생성합니다.
 * 한국어 비즈니스 문서 형식을 지원합니다.
 *
 * 사용 예시:
 *   deno run --allow-read --allow-write create-from-spec.ts --spec doc-spec.json --output result.docx
 *   deno run --allow-read --allow-write create-from-spec.ts --spec spec.json --output out.docx --template base.docx
 *
 * spec.json 구조:
 * {
 *   "meta": { "title": "보고서 제목", "author": "홍길동", "date": "2026-04-09" },
 *   "style": { "font": "Pretendard", "fontSize": 11, "lineSpacing": 1.5 },
 *   "sections": [
 *     { "type": "heading", "level": 1, "text": "제1장 개요" },
 *     { "type": "paragraph", "text": "본 보고서는..." },
 *     { "type": "table", "headers": ["항목", "내용"], "rows": [["날짜", "2026-04-09"]] },
 *     { "type": "list", "items": ["첫 번째", "두 번째"], "ordered": true },
 *     { "type": "pagebreak" }
 *   ]
 * }
 */

import { join } from "https://deno.land/std@0.224.0/path/mod.ts";

// ─────────────────────────────────────────────
// 타입 정의
// ─────────────────────────────────────────────

interface DocMeta {
  title?: string;
  author?: string;
  date?: string;
  subject?: string;
  keywords?: string[];
  description?: string;
}

interface DocStyle {
  font?: string;           // 기본 폰트 (기본: "맑은 고딕")
  fontSize?: number;       // pt 단위 (기본: 11)
  lineSpacing?: number;    // 배수 (기본: 1.15)
  margins?: {
    top?: number;    // mm
    bottom?: number;
    left?: number;
    right?: number;
  };
}

type SectionType = "heading" | "paragraph" | "table" | "list" | "image" | "pagebreak" | "hr";

interface BaseSection {
  type: SectionType;
  style?: Partial<DocStyle>;
}

interface HeadingSection extends BaseSection {
  type: "heading";
  level: 1 | 2 | 3 | 4 | 5 | 6;
  text: string;
  numbered?: boolean;
}

interface ParagraphSection extends BaseSection {
  type: "paragraph";
  text: string;
  align?: "left" | "center" | "right" | "justify";
  bold?: boolean;
  italic?: boolean;
  underline?: boolean;
}

interface TableSection extends BaseSection {
  type: "table";
  headers?: string[];
  rows: string[][];
  caption?: string;
  headerStyle?: "bold" | "shaded" | "none";
}

interface ListSection extends BaseSection {
  type: "list";
  items: string[];
  ordered?: boolean;
  startNumber?: number;
}

interface ImageSection extends BaseSection {
  type: "image";
  path: string;
  caption?: string;
  width?: number;   // cm
  align?: "left" | "center" | "right";
}

interface PagebreakSection extends BaseSection {
  type: "pagebreak";
}

interface HrSection extends BaseSection {
  type: "hr";
}

type Section =
  | HeadingSection
  | ParagraphSection
  | TableSection
  | ListSection
  | ImageSection
  | PagebreakSection
  | HrSection;

interface DocSpec {
  meta?: DocMeta;
  style?: DocStyle;
  sections: Section[];
}

// ─────────────────────────────────────────────
// OOXML 생성 유틸리티
// ─────────────────────────────────────────────

function escapeXml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function mm2twips(mm: number): number {
  // 1인치 = 25.4mm, 1인치 = 1440 twips
  return Math.round((mm / 25.4) * 1440);
}

function pt2halfPt(pt: number): number {
  return pt * 2;
}

// ─────────────────────────────────────────────
// OOXML 섹션별 생성기
// ─────────────────────────────────────────────

function buildRunXml(text: string, bold?: boolean, italic?: boolean, underline?: boolean, font?: string, size?: number): string {
  const rPr: string[] = [];
  if (font) rPr.push(`<w:rFonts w:ascii="${escapeXml(font)}" w:hAnsi="${escapeXml(font)}" w:eastAsia="${escapeXml(font)}"/>`);
  if (size) rPr.push(`<w:sz w:val="${pt2halfPt(size)}"/><w:szCs w:val="${pt2halfPt(size)}"/>`);
  if (bold) rPr.push("<w:b/><w:bCs/>");
  if (italic) rPr.push("<w:i/><w:iCs/>");
  if (underline) rPr.push('<w:u w:val="single"/>');

  const rPrXml = rPr.length > 0 ? `<w:rPr>${rPr.join("")}</w:rPr>` : "";
  return `<w:r>${rPrXml}<w:t xml:space="preserve">${escapeXml(text)}</w:t></w:r>`;
}

function buildHeadingXml(sec: HeadingSection, style: DocStyle): string {
  const styleName = `제목${sec.level}`;
  const fontSize = [28, 24, 20, 18, 16, 14][sec.level - 1] ?? 14;
  const run = buildRunXml(sec.text, true, false, false, style.font, fontSize);
  return `<w:p>
  <w:pPr>
    <w:pStyle w:val="${styleName}"/>
    <w:spacing w:before="240" w:after="120"/>
  </w:pPr>
  ${run}
</w:p>`;
}

function buildParagraphXml(sec: ParagraphSection, style: DocStyle): string {
  const alignMap: Record<string, string> = { left: "left", center: "center", right: "right", justify: "both" };
  const jc = sec.align ? `<w:jc w:val="${alignMap[sec.align] ?? "left"}"/>` : "";
  const lineSpacing = style.lineSpacing ?? 1.15;
  const line = Math.round(lineSpacing * 240);

  const run = buildRunXml(sec.text, sec.bold, sec.italic, sec.underline, style.font, style.fontSize);
  return `<w:p>
  <w:pPr>
    <w:spacing w:line="${line}" w:lineRule="auto" w:after="160"/>
    ${jc}
  </w:pPr>
  ${run}
</w:p>`;
}

function buildTableXml(sec: TableSection, style: DocStyle): string {
  const rows: string[] = [];

  // 헤더 행
  if (sec.headers && sec.headers.length > 0) {
    const cells = sec.headers.map((h) => {
      const shading = sec.headerStyle === "shaded"
        ? '<w:shd w:val="clear" w:color="auto" w:fill="D0E4F1"/>'
        : "";
      return `<w:tc>
        <w:tcPr>${shading}<w:tcBorders><w:top w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/></w:tcBorders></w:tcPr>
        <w:p><w:pPr><w:jc w:val="center"/></w:pPr>${buildRunXml(h, true, false, false, style.font, style.fontSize)}</w:p>
      </w:tc>`;
    }).join("");
    rows.push(`<w:tr><w:trPr><w:tblHeader/></w:trPr>${cells}</w:tr>`);
  }

  // 데이터 행
  for (const row of sec.rows) {
    const cells = row.map((cell) => `<w:tc>
      <w:tcPr><w:tcBorders><w:top w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/></w:tcBorders></w:tcPr>
      <w:p>${buildRunXml(cell, false, false, false, style.font, style.fontSize)}</w:p>
    </w:tc>`).join("");
    rows.push(`<w:tr>${cells}</w:tr>`);
  }

  const captionXml = sec.caption
    ? `<w:p><w:pPr><w:jc w:val="center"/></w:pPr>${buildRunXml(`[표] ${sec.caption}`, false, true, false, style.font, (style.fontSize ?? 11) - 1)}</w:p>`
    : "";

  return `<w:tbl>
  <w:tblPr>
    <w:tblStyle w:val="TableGrid"/>
    <w:tblW w:w="0" w:type="auto"/>
    <w:tblBorders>
      <w:insideH w:val="single" w:sz="4"/>
      <w:insideV w:val="single" w:sz="4"/>
    </w:tblBorders>
  </w:tblPr>
  ${rows.join("\n")}
</w:tbl>
${captionXml}`;
}

function buildListXml(sec: ListSection, style: DocStyle): string {
  return sec.items.map((item, idx) => {
    const bullet = sec.ordered ? `${(sec.startNumber ?? 1) + idx}.` : "•";
    const run = buildRunXml(`${bullet} ${item}`, false, false, false, style.font, style.fontSize);
    return `<w:p>
  <w:pPr>
    <w:ind w:left="720"/>
    <w:spacing w:after="80"/>
  </w:pPr>
  ${run}
</w:p>`;
  }).join("\n");
}

function buildPagebreakXml(): string {
  return `<w:p><w:r><w:br w:type="page"/></w:r></w:p>`;
}

function buildHrXml(): string {
  return `<w:p>
  <w:pPr>
    <w:pBdr>
      <w:bottom w:val="single" w:sz="6" w:space="1" w:color="888888"/>
    </w:pBdr>
  </w:pPr>
</w:p>`;
}

// ─────────────────────────────────────────────
// 전체 문서 XML 빌더
// ─────────────────────────────────────────────

const DEFAULT_STYLE: Required<DocStyle> = {
  font: "맑은 고딕",
  fontSize: 11,
  lineSpacing: 1.15,
  margins: { top: 30, bottom: 30, left: 35, right: 30 },
};

function buildDocumentXml(spec: DocSpec): string {
  const style: Required<DocStyle> = {
    ...DEFAULT_STYLE,
    ...spec.style,
    margins: { ...DEFAULT_STYLE.margins, ...spec.style?.margins },
  };

  const margins = style.margins;
  const pgMar = `<w:pgMar w:top="${mm2twips(margins.top ?? 30)}" w:right="${mm2twips(margins.right ?? 30)}" w:bottom="${mm2twips(margins.bottom ?? 30)}" w:left="${mm2twips(margins.left ?? 35)}" w:header="708" w:footer="708" w:gutter="0"/>`;

  const bodyParts: string[] = [];

  for (const sec of spec.sections) {
    switch (sec.type) {
      case "heading":   bodyParts.push(buildHeadingXml(sec, style)); break;
      case "paragraph": bodyParts.push(buildParagraphXml(sec, style)); break;
      case "table":     bodyParts.push(buildTableXml(sec, style)); break;
      case "list":      bodyParts.push(buildListXml(sec, style)); break;
      case "pagebreak": bodyParts.push(buildPagebreakXml()); break;
      case "hr":        bodyParts.push(buildHrXml()); break;
      case "image":
        bodyParts.push(`<w:p><w:r><w:t>[이미지: ${escapeXml((sec as ImageSection).path)}]</w:t></w:r></w:p>`);
        break;
    }
  }

  return `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
  xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
  xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml">
  <w:body>
    ${bodyParts.join("\n    ")}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      ${pgMar}
    </w:sectPr>
  </w:body>
</w:document>`;
}

function buildCorePropsXml(meta: DocMeta): string {
  const date = meta.date ?? new Date().toISOString().split("T")[0];
  return `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>${escapeXml(meta.title ?? "")}</dc:title>
  <dc:creator>${escapeXml(meta.author ?? "")}</dc:creator>
  <dc:description>${escapeXml(meta.description ?? "")}</dc:description>
  <dc:subject>${escapeXml(meta.subject ?? "")}</dc:subject>
  <dcterms:created xsi:type="dcterms:W3CDTF">${date}T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">${new Date().toISOString()}</dcterms:modified>
</cp:coreProperties>`;
}

const CONTENT_TYPES_XML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>`;

const RELS_XML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>`;

const WORD_RELS_XML = `<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>`;

// ─────────────────────────────────────────────
// DOCX 패키지 생성
// ─────────────────────────────────────────────

async function createDocx(spec: DocSpec, outputPath: string): Promise<void> {
  const tmpDir = await Deno.makeTempDir({ prefix: "docx_create_" });

  try {
    // 디렉토리 구조 생성
    await Deno.mkdir(join(tmpDir, "_rels"), { recursive: true });
    await Deno.mkdir(join(tmpDir, "word", "_rels"), { recursive: true });
    await Deno.mkdir(join(tmpDir, "docProps"), { recursive: true });

    // 파일 쓰기
    await Deno.writeTextFile(join(tmpDir, "[Content_Types].xml"), CONTENT_TYPES_XML);
    await Deno.writeTextFile(join(tmpDir, "_rels", ".rels"), RELS_XML);
    await Deno.writeTextFile(join(tmpDir, "word", "_rels", "document.xml.rels"), WORD_RELS_XML);
    await Deno.writeTextFile(join(tmpDir, "word", "document.xml"), buildDocumentXml(spec));
    await Deno.writeTextFile(join(tmpDir, "docProps", "core.xml"), buildCorePropsXml(spec.meta ?? {}));

    // ZIP으로 압축
    const outputAbs = join(Deno.cwd(), outputPath);
    await Deno.mkdir(outputAbs.replace(/[^/]+$/, ""), { recursive: true });

    const zip = new Deno.Command("bash", {
      args: ["-c", `cd "${tmpDir}" && zip -r "${outputAbs}" .`],
      stdout: "null",
      stderr: "piped",
    });
    const { code, stderr } = await zip.output();
    if (code !== 0) {
      throw new Error(`DOCX 생성 실패: ${new TextDecoder().decode(stderr)}`);
    }
  } finally {
    await Deno.remove(tmpDir, { recursive: true });
  }
}

// ─────────────────────────────────────────────
// CLI 진입점
// ─────────────────────────────────────────────

async function main() {
  const args = Deno.args;

  if (args.length === 0 || args.includes("--help")) {
    console.log(`사용법:
  create-from-spec.ts --spec <spec.json> --output <출력.docx>

옵션:
  --spec     문서 스펙 JSON 파일 경로 (필수)
  --output   출력 DOCX 파일 경로 (필수)

스펙 JSON 구조 예시는 이 파일 상단 주석을 참조하세요.`);
    Deno.exit(0);
  }

  let specPath = "";
  let outputPath = "";

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--spec") specPath = args[++i];
    else if (args[i] === "--output") outputPath = args[++i];
  }

  if (!specPath || !outputPath) {
    console.error("오류: --spec 과 --output 은 필수입니다.");
    Deno.exit(1);
  }

  try {
    const specText = await Deno.readTextFile(specPath);
    const spec: DocSpec = JSON.parse(specText);

    console.log(`스펙 파일: ${specPath}`);
    console.log(`섹션 수: ${spec.sections.length}개`);
    console.log(`출력 파일: ${outputPath}`);

    await createDocx(spec, outputPath);

    console.log("\n문서 생성 완료!");
  } catch (err) {
    console.error(`오류: ${err instanceof Error ? err.message : String(err)}`);
    Deno.exit(1);
  }
}

await main();
