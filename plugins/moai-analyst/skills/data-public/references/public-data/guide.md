# 공공데이터 조회 가이드

## data.go.kr API 호출 패턴

```
GET https://apis.data.go.kr/{기관코드}/{서비스명}?ServiceKey={키}&...
```

응답: JSON 또는 XML

## KOSIS API 호출 패턴

```
GET https://kosis.kr/openapi/Param/statisticsParameterData.do
  ?method=getList
  &apiKey={키}
  &itmId=T10
  &objL1=ALL
  &objL2=ALL
  &format=json
  &jsonVD=Y
  &prdSe=M
  &startPrdDe=202501
  &endPrdDe=202512
  &orgId=101
  &tblId=DT_1B04005N
```

## API 키 로드 함수 (참조)

키는 사용자가 앱의 연결 설정 또는 실행 환경에 등록한 값으로 읽는다. 환경변수 경로에서는 `DATA_GO_KR_API_KEY` 또는 `KOSIS_API_KEY`를 사용한다. 키를 채팅에서 수집하거나 플러그인 폴더에 저장하지 않는다. 두 API 모두 요청 URL에 키가 포함될 수 있으므로 URL 전체를 결과나 진단 로그에 출력하지 않는다.
