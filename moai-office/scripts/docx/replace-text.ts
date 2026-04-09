#!/usr/bin/env -S deno run --allow-read --allow-write
/**
 * replace-text.ts — DOCX 템플릿 플레이스홀더 교체기
 *
 * DOCX 템플릿의 플레이스홀더를 실제 값으로 교체합니다.
 * 한국어 텍스트를 완벽하게 지원합니다.
 *
 * 사용 예시:
 *   deno run --allow-read --allow-write replace-text.ts \
 *     --template template.docx \
 *     --output filled.docx \
 *     --values '{"회사명":"(주)모아이","담당자":"김철수"}'
 *
 *   deno run --allow-read --allow-write replace-text.ts \
 *     --template template.docx \
 *     --output filled.docx \
 *     --values-file values.json
 *
 * values.json 예시:
 *   {
 *     "{{회사명}}": "(주)모아이",
 *     "{{담당자}}": "김철수",
 *     "{{날짜}}": "2026년 4월 9일",
 *     "{{금액}}": "1,000,000원"
 *   }
 */

import { join } from "https://deno.land/std@0.224.0/path/mod.ts";

// ─────────────────────────────────────────────
// 타입 정의
// ─────────────────────────────────────────────

type ReplacementMap = Record<string, string>;

interface ReplaceOptions {
  templatePath: string;
  outputPath: string;
  replacements: ReplacementMap;
  strict?: boolean;  // true이면 매핑되지 않은 플레이스홀더가 있을 때 오류 발생
}

interface ReplaceResult {
  success: boolean;
  replacedCount: number;
  skippedPlaceholders: string[];
  outputPath: string;
}

// ─────────────────────────────────────────────
// 플레이스홀더 정규화
// ─────────────────────────────────────────────

/**
 * 값 맵의 키를 정규화합니다.
 * "회사명", "{{회사명}}", "${회사명}" 등 다양한 형태를 지원합니다.
 */
function normalizeReplacements(raw: ReplacementMap): Map<RegExp, string> {
  const normalized = new Map<RegExp, string>();

  for (const [key, value] of Object.entries(raw)) {
    // 이미 패턴이 포함된 경우 ({{...}}, ${...}, <<...>>, [...])
    if (/^\{\{.+\}\}$/.test(key)) {
      const inner = key.slice(2, -2);
      normalized.set(new RegExp(`\\{\\{${escapeRegex(inner)}\\}\\}`, "g"), value);
    } else if (/^\$\{.+\}$/.test(key)) {
      const inner = key.slice(2, -1);
      normalized.set(new RegExp(`\\$\\{${escapeRegex(inner)}\\}`, "g"), value);
    } else if (/^<<.+>>$/.test(key)) {
      const inner = key.slice(2, -2);
      normalized.set(new RegExp(`<<${escapeRegex(inner)}>>`, "g"), value);
    } else if (/^\[.+\]$/.test(key)) {
      const inner = key.slice(1, -1);
      normalized.set(new RegExp(`\\[${escapeRegex(inner)}\\]`, "g"), value);
    } else {
      // 패턴 없는 순수 변수명 → 모든 패턴 형식으로 매칭
      const escaped = escapeRegex(key);
      const combined = new RegExp(
        `\\{\\{${escaped}\\}\\}|\\$\\{${escaped}\\}|<<${escaped}>>|\\[${escaped}\\]`,
        "g"
      );
      normalized.set(combined, value);
    }
  }

  return normalized;
}

function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// ─────────────────────────────────────────────
// XML 내 텍스트 교체
// ─────────────────────────────────────────────

/**
 * DOCX XML에서는 플레이스홀더가 여러 <w:r> 런(run)으로 분리될 수 있습니다.
 * 이 함수는 런을 병합한 후 교체하고 다시 분리합니다.
 */
function mergeRunsAndReplace(xml: string, patterns: Map<RegExp, string>): {
  xml: string;
  replacedCount: number;
} {
  let replacedCount = 0;

  // w:p 단락 단위로 처리
  xml = xml.replace(/<w:p[ >][\s\S]*?<\/w:p>/g, (para) => {
    // 단락 내 모든 텍스트 런(w:r) 추출
    const runs: Array<{ full: string; text: string }> = [];
    for (const m of para.matchAll(/<w:r[ >][\s\S]*?<\/w:r>/g)) {
      const textMatch = m[0].match(/<w:t[^>]*>([^<]*)<\/w:t>/);
      runs.push({ full: m[0], text: textMatch?.[1] ?? "" });
    }

    if (runs.length === 0) return para;

    // 런 텍스트 병합
    const merged = runs.map((r) => r.text).join("");

    // 교체 수행
    let replaced = merged;
    for (const [pattern, value] of patterns) {
      const before = replaced;
      replaced = replaced.replace(pattern, value);
      if (replaced !== before) replacedCount++;
    }

    if (replaced === merged) return para; // 변경 없음

    // 첫 번째 런에 교체된 텍스트 전체를 넣고 나머지 런 제거
    if (runs.length > 0) {
      const firstRun = runs[0].full.replace(
        /<w:t[^>]*>[^<]*<\/w:t>/,
        `<w:t xml:space="preserve">${escapeXml(replaced)}</w:t>`
      );
      let result = para.replace(runs[0].full, firstRun);
      for (let i = 1; i < runs.length; i++) {
        result = result.replace(runs[i].full, "");
      }
      return result;
    }

    return para;
  });

  return { xml, replacedCount };
}

function escapeXml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

// ─────────────────────────────────────────────
// 남은 플레이스홀더 탐지
// ─────────────────────────────────────────────

function findRemainingPlaceholders(xml: string): string[] {
  const found = new Set<string>();
  const patterns = [/\{\{([^}]+)\}\}/g, /\$\{([^}]+)\}/g, /<<([^>]+)>>/g];
  for (const p of patterns) {
    for (const m of xml.matchAll(p)) {
      found.add(m[0]);
    }
  }
  return Array.from(found);
}

// ─────────────────────────────────────────────
// ZIP 조작 (DOCX = ZIP)
// ─────────────────────────────────────────────

async function replaceInDocx(options: ReplaceOptions): Promise<ReplaceResult> {
  const { templatePath, outputPath, replacements, strict = false } = options;

  const tmpDir = await Deno.makeTempDir({ prefix: "docx_replace_" });

  try {
    // 압축 해제
    const unzip = new Deno.Command("unzip", {
      args: ["-o", templatePath, "-d", tmpDir],
      stdout: "null",
      stderr: "piped",
    });
    const { code: unzipCode, stderr } = await unzip.output();
    if (unzipCode !== 0) {
      throw new Error(`압축 해제 실패: ${new TextDecoder().decode(stderr)}`);
    }

    const patterns = normalizeReplacements(replacements);
    let totalReplaced = 0;

    // 교체 대상 XML 파일 목록
    const xmlFiles = [
      join(tmpDir, "word", "document.xml"),
      join(tmpDir, "word", "header1.xml"),
      join(tmpDir, "word", "footer1.xml"),
      join(tmpDir, "word", "header2.xml"),
      join(tmpDir, "word", "footer2.xml"),
    ];

    for (const xmlFile of xmlFiles) {
      try {
        let content = await Deno.readTextFile(xmlFile);
        const { xml: updated, replacedCount } = mergeRunsAndReplace(content, patterns);
        if (replacedCount > 0) {
          await Deno.writeTextFile(xmlFile, updated);
          totalReplaced += replacedCount;
        }
      } catch {
        // 파일이 없는 경우 무시
      }
    }

    // 남은 플레이스홀더 확인
    const documentXml = await Deno.readTextFile(join(tmpDir, "word", "document.xml"));
    const remaining = findRemainingPlaceholders(documentXml);

    if (strict && remaining.length > 0) {
      throw new Error(`교체되지 않은 플레이스홀더: ${remaining.join(", ")}`);
    }

    // 재압축
    const outputDir = outputPath.replace(/[^/]+$/, "") || ".";
    await Deno.mkdir(outputDir, { recursive: true });

    const zip = new Deno.Command("bash", {
      args: ["-c", `cd "${tmpDir}" && zip -r "${Deno.cwd()}/${outputPath}" .`],
      stdout: "null",
      stderr: "piped",
    });
    const { code: zipCode, stderr: zipErr } = await zip.output();
    if (zipCode !== 0) {
      throw new Error(`압축 실패: ${new TextDecoder().decode(zipErr)}`);
    }

    return {
      success: true,
      replacedCount: totalReplaced,
      skippedPlaceholders: remaining,
      outputPath,
    };
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
  replace-text.ts --template <입력.docx> --output <출력.docx> --values '<JSON>'
  replace-text.ts --template <입력.docx> --output <출력.docx> --values-file <values.json>

옵션:
  --template      원본 DOCX 파일 경로
  --output        출력 DOCX 파일 경로
  --values        JSON 문자열로 교체 값 지정
  --values-file   JSON 파일로 교체 값 지정
  --strict        미교체 플레이스홀더 발생 시 오류 처리`);
    Deno.exit(0);
  }

  let templatePath = "";
  let outputPath = "";
  let valuesJson = "";
  let valuesFile = "";
  let strict = false;

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case "--template":   templatePath = args[++i]; break;
      case "--output":     outputPath = args[++i]; break;
      case "--values":     valuesJson = args[++i]; break;
      case "--values-file": valuesFile = args[++i]; break;
      case "--strict":     strict = true; break;
    }
  }

  if (!templatePath || !outputPath) {
    console.error("오류: --template 과 --output 은 필수입니다.");
    Deno.exit(1);
  }

  let replacements: ReplacementMap;
  if (valuesFile) {
    const text = await Deno.readTextFile(valuesFile);
    replacements = JSON.parse(text);
  } else if (valuesJson) {
    replacements = JSON.parse(valuesJson);
  } else {
    console.error("오류: --values 또는 --values-file 중 하나는 필수입니다.");
    Deno.exit(1);
  }

  try {
    console.log(`템플릿: ${templatePath}`);
    console.log(`교체 항목: ${Object.keys(replacements!).length}개`);

    const result = await replaceInDocx({
      templatePath,
      outputPath,
      replacements: replacements!,
      strict,
    });

    console.log(`\n완료!`);
    console.log(`  교체된 플레이스홀더: ${result.replacedCount}개`);
    if (result.skippedPlaceholders.length > 0) {
      console.log(`  미교체 플레이스홀더: ${result.skippedPlaceholders.join(", ")}`);
    }
    console.log(`  출력 파일: ${result.outputPath}`);
  } catch (err) {
    console.error(`오류: ${err instanceof Error ? err.message : String(err)}`);
    Deno.exit(1);
  }
}

await main();
