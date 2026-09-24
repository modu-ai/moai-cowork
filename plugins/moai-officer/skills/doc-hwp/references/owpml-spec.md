# OWPML 구조 참고 — HWPX

이 문서는 HWPX의 주요 파일과 텍스트 추출 위치를 설명합니다. 완전한 OWPML 명세서나 직접 파일을 생성할 수 있는 XML 템플릿은 아닙니다. 생성·수정에는 현재 설치된 HWPX 도구와 그 버전의 API를 사용합니다.

## 패키지 구조

[한컴테크의 HWPX 구조 설명](https://tech.hancom.com/hwpxformat/)에 따르면 HWPX는 ZIP 기반 XML 형식입니다. 주요 파일은 다음과 같습니다.

| 경로 | 역할 |
|---|---|
| `mimetype` | HWPX 형식 식별 |
| `version.xml` | 형식·저장 환경 정보 |
| `Contents/content.hpf` | OPF 방식의 metadata·manifest·spine. spine 순서가 문서 읽기 순서 |
| `Contents/header.xml` | 글자·문단 모양 등 서식 참조 정보 |
| `Contents/section0.xml` 등 | 구역별 본문 |
| `META-INF/` | 컨테이너 정보, 암호 문서의 관련 정보 |
| `BinData/` | 포함된 그림 등 바이너리 자료 |

본문의 문단은 `<hp:p>`, 텍스트 런은 `<hp:run>`, 글자는 `<hp:t>`에 들어갑니다. 이 구조만으로 표·그림·각주·서식 전체를 복원할 수는 없습니다.

## 읽기 전용 텍스트 추출 예시

이 예시는 암호화되지 않은 HWPX의 첫 구역에서 글자 노드만 읽습니다. 문서 순서 전체, 표 셀 경계, 서식 보존, 파일 수정에는 사용하지 않습니다.

```python
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

source = Path("source.hwpx")
with ZipFile(source) as archive:
    if archive.testzip() is not None:
        raise ValueError("ZIP 손상")
    root = ET.fromstring(archive.read("Contents/section0.xml"))
    ns = {"hp": "http://www.hancom.co.kr/hwpml/2011/paragraph"}
    text = "".join(node.text or "" for node in root.findall(".//hp:t", ns))
print(text)
```

XML 파싱에 성공해도 한컴오피스에서 열리는지, 서식이 유지됐는지는 입증되지 않습니다. `content.hpf`와 헤더·구역 참조를 포함한 유효성 검사, 사용한 도구로 재개봉, 대상 앱의 시각 확인은 별도로 수행합니다. 원본 HWPX를 직접 ZIP으로 다시 쓰면 매니페스트·서명·보존 정보가 손상될 수 있으므로 원본을 보존합니다.
