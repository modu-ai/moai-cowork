"""XML 응답을 도구 응답용 딕셔너리로 바꾼다.

KIPRIS Plus와 USPTO TSDR은 XML만 돌려준다. 요소 이름을 하나하나 옮기지 않고
구조를 그대로 딕셔너리로 바꿔서, 상대 API가 필드를 추가해도 서버 코드를 고칠 필요가
없게 한다.

규칙
- 네임스페이스 접두어는 떼고 로컬 이름만 쓴다 (`{urn:..}MarkVerbalElementText` → `MarkVerbalElementText`).
- 같은 이름의 형제 요소가 둘 이상이면 리스트로 묶는다.
- 자식이 없는 요소는 텍스트 값이 된다. 빈 텍스트는 버린다 — 응답이 불필요하게 길어진다.
- 속성은 `@이름` 키로 싣는다.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any

from moai_mcp_core import UpstreamError


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def element_to_data(element: ET.Element) -> Any:
    children = list(element)
    attributes = {f"@{local_name(k)}": v for k, v in element.attrib.items()}
    if not children:
        text = (element.text or "").strip()
        if attributes:
            if text:
                attributes["#text"] = text
            return attributes
        return text

    data: dict[str, Any] = dict(attributes)
    for child in children:
        value = element_to_data(child)
        if value in ("", {}, []):
            continue
        key = local_name(child.tag)
        if key in data:
            existing = data[key]
            if not isinstance(existing, list):
                data[key] = [existing]
            data[key].append(value)
        else:
            data[key] = value
    return data


def parse(text: str) -> ET.Element:
    try:
        return ET.fromstring(text.encode("utf-8"))
    except ET.ParseError as exc:
        raise UpstreamError("응답을 XML로 해석하지 못했습니다.", body=text) from exc


def find_first(root: ET.Element, name: str) -> ET.Element | None:
    for element in root.iter():
        if local_name(element.tag) == name:
            return element
    return None


def find_all(root: ET.Element, name: str) -> list[ET.Element]:
    return [element for element in root.iter() if local_name(element.tag) == name]


def text_of(root: ET.Element, name: str) -> str:
    element = find_first(root, name)
    return (element.text or "").strip() if element is not None else ""
