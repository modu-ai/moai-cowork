---
title: "기능 검증과 평가"
description: "형식 검사·실제 도구 노출·모델 평가·사용자 여정을 구분합니다"
weight: 10
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-06
geekdocBreadcrumb: true
---


<!--more-->


## 검사마다 확인하는 범위

| 검사 | 확인하는 것 | 대신 확인하지 못하는 것 |
|---|---|---|
| 스키마·문법 | 패키지 형식·필드·참조 | 실제 앱 설치와 계정 인증 |
| tools/list | 도구 정의·안내 속성 | 외부 서버에서 작업 성공 |
| 단위 검사 | 구현의 지정된 동작 | 모든 OS·계정의 사용자 경험 |
| 모델 평가 | 실제 예제 실행의 품질 | 미실행한 예제 |
| 사용자 여정 | 앱에서 설치·자료·결과 흐름 | 다른 계정·플랫폼 전체 |

## 저장소 검사

개발 환경에서 `scripts/check-skill-contracts.py`, `scripts/check-mcp-annotations.py`, 문서 빌드 및 링크 검사를 실행합니다. 필요한 개발 의존성을 확인하고 명령·출력·트리·커밋·검사 범위를 기록합니다.

모델 평가 정의가 존재한다는 사실과 실제 모델 평가가 통과한 것은 구분합니다. 실행·권한·외부 변경 범위를 제한하고 검토 가능한 예제로 평가합니다. 자세한 절차는 저장소의 `docs/behavioral-evals.md`에서 확인하세요.

## 공식 문서와 참고 자료

- [평가 운영 문서](https://github.com/modu-ai/moai-cowork/blob/main/docs/behavioral-evals.md)
