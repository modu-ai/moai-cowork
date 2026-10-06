# 문서 개편 검증 기록

측정 작업 트리: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`

각 명령은 이 작업 트리에서 실행했으며 종료 코드는 모두 0입니다. CI 구성 검사 범위는 YAML 구문과 작업 설정이며 원격 CI 실행은 아닙니다.

## 1

```sh
hugo --quiet --minify --enableGitInfo=false --source www --destination /tmp/moai-docs-20261005-final
```

```text
exit 0; stdout empty
```

## 2

```sh
python3 scripts/check-docs.py /tmp/moai-docs-20261005-final --report reports/20261005-docs-rebuild/site-check.json
```

```text
{
  "html_files": 288,
  "internal_references": 25098,
  "fragment_references": 3345,
  "images": 413,
  "search_entries": 170,
  "sitemap_entries": 192,
  "classroom_rows": 6,
  "classroom_types": {
    "배송": 3,
    "반품": 2,
    "결제": 1
  },
  "worked_arithmetic": [
    {
      "path": "www/content/cookbook/guides/data-analysis.md",
      "expected": [
        50,
        34,
        68.0
      ],
      "actual": [
        50,
        34,
        68
      ]
    },
    {
      "path": "www/content/cookbook/guides/data-visualization.md",
      "expected": [
        50,
        34,
        68.0
      ],
      "actual": [
        50,
        34,
        68
      ]
    },
    {
      "path": "www/content/cookbook/projects/public-data-report.md",
      "expected": [
        50,
        34,
        68.0
      ],
      "actual": [
        50,
        34,
        68
      ]
    },
    {
      "path": "www/content/cookbook/templates/excel.md",
      "expected": [
        25000
      ],
      "actual": [
        25000
      ]
    },
    {
      "path": "www/content/cookbook/templates/financial.md",
      "expected": [
        2000000,
        800000,
        500000,
        700000
      ],
      "actual": [
        2000000,
        800000,
        500000,
        700000
      ]
    },
    {
      "path": "www/content/cookbook/tracks/track-data.md",
      "expected": [
        50,
        34,
        68.0
      ],
      "actual": [
        50,
        34,
        68
      ]
    },
    {
      "path": "www/content/cookbook/tracks/track-documents.md",
      "expected": [
        25000
      ],
      "actual": [
        25000
      ]
    },
    {
      "path": "www/content/cookbook/tracks/track-finance.md",
      "expected": [
        2000000,
        800000,
        500000,
        700000
      ],
      "actual": [
        2000000,
        800000,
        500000,
        700000
      ]
    },
    {
      "path": "www/content/moai-agents/accountant.md",
      "expected": [
        2000000,
        800000,
        500000,
        700000
      ],
      "actual": [
        2000000,
        800000,
        500000,
        700000
      ]
    },
    {
      "path": "www/content/moai-agents/analyst.md",
      "expected": [
        50,
        34,
        68.0
      ],
      "actual": [
        50,
        34,
        68
      ]
    },
    {
      "path": "www/content/moai-agents/officer.md",
      "expected": [
        25000
      ],
      "actual": [
        25000
      ]
    }
  ],
  "lessons": 6,
  "errors": [],
  "scope": "built_site_local_references_and_fixtures_only"
}
```

## 3

```sh
uv run --no-project --python 3.11 --with skills-ref==0.1.1 --with jsonschema==4.25.1 --with pyyaml==6.0.3 python scripts/check-skill-contracts.py
```

```text
{
  "skills": 252,
  "packages": 18,
  "errors": [],
  "scope": "offline_contracts_only"
}
```

## 4

```sh
python3 reports/20261005-docs-rebuild/verify-checker.py
```

```text
{
  "missing_link_detected": true,
  "wrong_example_total_detected": true
}
```

## 5

```sh
node reports/20261005-docs-rebuild/verify-copy.cjs
```

```text
{
  "scope": "DOM model, not operating-system clipboard",
  "cases": [
    {
      "mode": "clipboard-success",
      "observedLabel": "복사됨",
      "promptRemoved": true
    },
    {
      "mode": "clipboard-denied",
      "observedLabel": "직접 복사",
      "promptRemoved": true
    },
    {
      "mode": "fallback-success",
      "observedLabel": "복사됨",
      "promptRemoved": true
    },
    {
      "mode": "fallback-denied",
      "observedLabel": "직접 복사",
      "promptRemoved": true
    }
  ]
}
```

## 6

```sh
git diff --check -- www README.md CHANGELOG.md .github/workflows/docs-check.yml scripts/check-docs.py
```

```text
exit 0; stdout empty
```

