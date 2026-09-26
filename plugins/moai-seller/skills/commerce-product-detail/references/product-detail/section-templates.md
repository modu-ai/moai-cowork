# 상품 상세 섹션 템플릿

[상위 스킬](../../SKILL.md)에 따라 판매 채널과 산출물 형식을 먼저 결정합니다.
마켓 에디터의 HTML·CSS·JavaScript 허용 여부는 [채널별 확인 항목](platform-specs.md)과
현재 계정에서 확인합니다. 아래 HTML은 자사몰·독립 웹사이트의 시작 예시이며
마켓에 그대로 업로드할 수 있다는 뜻이 아닙니다.

## 콘텐츠 입력

| 항목 | 자료가 없을 때 |
| --- | --- |
| 상품명·대표 사진·옵션 | 자리표시자로 두고 게시 전 확인 |
| 가격·배송·반품·재고 | 현재 계약·판매 화면에서 확인 |
| 후기·평점·판매량 | 실제 집계와 인용·사진 사용 권한 확인 전 생략 |
| 할인·행사·보증 | 현재 적용 조건과 기간 확인 전 생략 |
| 효능·인증·전문가 추천 | 제품별 근거와 공개 권한 확인 전 생략 |
| 관련 상품 | 실제 판매 상품과 가격 확인 전 생략 |

## 기본 HTML 예시

이 예시는 정적 정보 구조만 보여줍니다. 중괄호 자리표시자를
실제 값으로 바꿀 때는 HTML 이스케이프와 URL 검증을 적용합니다.
확인되지 않은 항목은 요소째 생략합니다.

```html
<main class="product-detail">
  <article>
    <header>
      <h1>{PRODUCT_NAME}</h1>
      <p>{VERIFIED_SHORT_DESCRIPTION}</p>
    </header>

    <figure>
      <img src="{VERIFIED_IMAGE_URL}" alt="{PRODUCT_IMAGE_DESCRIPTION}">
      <figcaption>{VERIFIED_IMAGE_CAPTION}</figcaption>
    </figure>

    <section aria-labelledby="product-facts">
      <h2 id="product-facts">상품 정보</h2>
      <dl>
        <dt>구성</dt><dd>{VERIFIED_CONTENTS}</dd>
        <dt>사용 방법</dt><dd>{VERIFIED_USE_INSTRUCTIONS}</dd>
      </dl>
    </section>

    <section aria-labelledby="purchase-terms">
      <h2 id="purchase-terms">구매 조건</h2>
      <p>{CURRENT_PRICE_AND_OPTIONS}</p>
      <p>{CURRENT_SHIPPING_AND_RETURN_TERMS}</p>
      <a href="{VERIFIED_PURCHASE_OR_INQUIRY_URL}">{ACTUAL_ACTION_LABEL}</a>
    </section>
  </article>
</main>
```

가격·옵션·장바구니·구매 버튼이 데이터와 연결되지 않은 정적 시안이라면
주문 가능 페이지라고 표시하지 않습니다. 버튼 역할을 하는 요소는 실제
동작이나 유효한 목적지가 있을 때만 추가합니다.

## 선택 섹션

- 후기는 실제 원문·집계 기준·사용 허락을 확인한 경우만 표시합니다.
- FAQ 답변은 실제 운영·제품 자료로 확인한 뒤 작성합니다.
- 비교·추천 상품은 현재 판매 자료와 같은 조건의 비교 근거가 있을 때만 넣습니다.
- 이미지 갤러리·동영상·탭·아코디언은 필요할 때 구현하고 키보드 조작과
  상태 알림을 렌더링한 화면에서 확인합니다.
- 할인율은 현재 기준 가격과 판매가로 계산합니다. 기준 가격이 없거나
  유효하지 않으면 할인 배지를 만들지 않습니다.
- 구조화 데이터는 실제 페이지에 있는 상품·가격·재고·후기만 반영합니다.
  예시 평점·리뷰 수·무료배송·배송일을 그대로 게시하지 않습니다.

## React 또는 다른 프레임워크

기존 프로젝트에 설치된 프레임워크·디자인 토큰·컴포넌트를 재사용합니다.
React, Next.js, 특정 CSS 모듈 구조를 기본 설치 전제로 강제하지 않습니다.
이미지·옵션·수량·가격·재고는 실제 상태와 연결하고, 빈 목록·미확인 가격·
이미지 로딩 실패를 처리합니다. 클릭만 가능한 장바구니·구매 버튼을
완료된 결제 흐름으로 보고하지 않습니다.

## 검증과 인계

생성한 파일을 읽고 실제 렌더링에서 모바일·데스크톱 화면, 키보드 조작,
이미지 대체 텍스트, 글자 대비, 링크 목적지, 가격·옵션 상태를 확인합니다.
계정 미리보기·이미지 업로드·공개 게시·실제 주문은 각각 별도 결과로
기록합니다. 실행하지 못한 검증은 NOT-RUN으로 남깁니다.
