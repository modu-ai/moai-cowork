# PptxGenJS 작성 예시

이 문서는 실행 환경에 PptxGenJS가 이미 있고 현재 버전의 API가 확인된 경우에만 사용한다. 이 플러그인에 PPTX 생성 스크립트나 PptxGenJS 패키지가 번들돼 있다는 뜻이 아니다. [공식 빠른 시작](https://gitbrent.github.io/PptxGenJS/docs/introduction/)과 [레이아웃 설명](https://gitbrent.github.io/PptxGenJS/docs/usage-pres-options/)을 우선한다.

## 최소 예시

```javascript
import PptxGenJS from "pptxgenjs";

const pptx = new PptxGenJS();
pptx.layout = "LAYOUT_WIDE";
const slide = pptx.addSlide();
slide.background = { color: "FFFFFF" };
slide.addText("확인된 문서 제목", {
  x: 0.7, y: 0.6, w: 11.9, h: 0.7,
  fontSize: 32, bold: true, color: "1A1A1A"
});
slide.addText("원본 자료에서 확인한 본문", {
  x: 0.7, y: 1.7, w: 11.9, h: 1.6,
  fontSize: 20, color: "1A1A1A"
});
await pptx.writeFile({ fileName: "output.pptx" });
```

좌표와 크기는 PptxGenJS의 슬라이드 단위를 따른다. `LAYOUT_WIDE`는 [공식 레이아웃 목록](https://gitbrent.github.io/PptxGenJS/docs/usage-pres-options/)의 약 13.3 × 7.5인치이며 1920×1080픽셀 좌표가 아니다. 실제 렌더링에서 글자가 박스를 넘는지 확인한다.

## 표·차트·이미지

- 표는 실제 행·열 자료를 확인한 뒤 `slide.addTable(rows, options)`로 넣는다. 합계는 원본 값으로 다시 계산한다.
- 차트는 사용 중인 버전의 `addChart` API와 데이터 계열 형식을 확인한다. 축 단위·기간·분모·범례를 명시하고 원본 데이터와 대조한다.
- 그림은 실제 파일 경로나 지원되는 데이터 URL을 사용한다. 원본 비율과 사용 권한을 확인한다.
- 글꼴 이름을 지정했다고 파일에 서체 바이너리가 포함되는 것은 아니다. 발표 PC 또는 PDF 결과의 대체 글꼴·줄바꿈을 확인한다.

## 품질 확인

파일을 다시 열어 슬라이드 수와 텍스트를 확인하고, 가능하면 대상 발표 앱에서 전체 슬라이드를 시각 검수한다. 코드에서 객체 좌표를 검사해도 실제 글꼴 대체나 줄바꿈을 증명하지 못한다. 예시 값과 사용자 자료를 섞지 않는다.
