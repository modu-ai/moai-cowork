# 픽셀 인포그래픽 제작 기록

도구: 내장 `image_gen.imagegen`. 두 이미지 모두 새로 생성했고 배경은 불투명이다. 생성 결과를 원본 그대로 복사했으며 파일을 편집하거나 재색칠하지 않았다.

## 병렬 작업

저장: `www/design-system/eink-proposal/assets/parallel-pixel-ko.png`

생성 원본: `/Users/goos/.codex/generated_images/01a10aae-6716-7681-b5d7-d558155d9f86/exec-93ed2285-f7d9-42fb-80c6-d2e147274b20.png`

최종 프롬프트:

```text
Create a premium Korean teaching infographic in monochrome pixel art, designed to sit in a Kindle e-ink reader style educational website. Landscape canvas 3:2, warm light gray background #e9e9e5, black #202020 and gray only. All shapes and illustrations are crisp square pixels, stepped outlines, discreet dither patterns, no antialias-like painterly shading, no colors, no gradients. This MUST communicate a fork and join workflow through strong connectors and little pixel pictograms of workers/documents, not boxes filled with prose. Exact Korean labels, large very legible pixel Korean letters, never cropped: Top center title '함께 만들고, 합쳐서 검토'. At upper center a documents-and-magnifier pixel pictogram labeled '문의 분석'. Draw a clear Y split into two equal branches: middle-left pixel FAQ document pictogram labeled 'FAQ 작성', middle-right pixel envelope pictogram labeled '안내문 작성'. Both branch arrows converge down at a stacked-document pictogram labeled '결과 합치기'. A downward arrow leads to magnifier-and-checklist pictogram labeled '원문 검토'. A final downward arrow leads to reader person and checked page labeled '사용자 확인'. Show a small dotted return arrow from '원문 검토' back toward both writing branches, with short Korean label '수정 요청'. The two writing branches must visibly be peers at same height and simultaneous. Only these exact labels; no English, no numbered cards, no footer, no '한국어 개념 설명', no logo, no fake software screenshot. Generous margins and whitespace, clear black arrows, every Korean letter fully visible. Put workflow centrally, all labels comfortably inside the canvas.
```

## 프로젝트 자료와 폴더

저장: `www/design-system/eink-proposal/assets/context-pixel-ko.png`

생성 원본: `/Users/goos/.codex/generated_images/01a10aae-6716-7681-b5d7-d558155d9f86/exec-cef72b44-d1b8-40cc-9e67-599d8f41463c.png`

최종 프롬프트:

```text
Create a clear Korean educational infographic, monochrome pixel art for a Kindle e-ink styled website. Landscape 3:2 composition with warm light gray #e9e9e5 background, black #202020 and neutral gray only, square pixels, stepped outlines, discrete dither, generous whitespace, large complete Korean pixel lettering. Title exactly '프로젝트 자료와 작업의 연결'. A top outlined rectangular container titled '프로젝트' contains three distinct small pixel document pictograms with labels '목표', '지침', '참고 자료'. Three black arrows exit these three items downward, converging on ONE central person-at-computer pictogram labeled '현재 작업'. A separate bottom rectangular folder container titled '허용된 폴더' contains two distinct pictograms: left source pages labeled '원본 자료', right completed page labeled '결과 파일'. A clearly separated dotted arrow from bottom-left source pages UP toward central work is labeled '접근 범위 확인'. A clearly separated solid arrow from central work DOWN toward bottom-right result is labeled '결과 저장'. The upper project and lower folder containers have no direct connecting arrow: central work is the sole bridge. All arrows must have correct unambiguous direction. Outer containers can have a stepped pixel corner treatment. Small pixel humans and folders support the spatial distinction; the image must be a relationship diagram, not text cards. Only the exact labels above, no other text, no English, no logo, no footer, no color, no fake application UI. Huge safe margins ensure no Korean text is cropped. Make all labels easy to read at 800px display width.
```

한국어 표기, 화살표 방향, 두 작성 역할의 같은 높이 배치, 프로젝트와 로컬 폴더의 분리 배치를 생성 결과와 실제 문서 화면에서 육안 확인했다. 이미지의 내용을 자동 OCR로 검증한 것은 아니다.
