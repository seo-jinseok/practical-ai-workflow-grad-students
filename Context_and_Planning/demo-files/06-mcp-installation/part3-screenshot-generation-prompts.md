# Part 3 스크린샷 생성 프롬프트 스크립트

**목적**: Part 3의 8개 연구 도구 웹페이지 스크린샷 자동 생성  
**대상**: 2025년 AI 연구 도구 생태계

## 대상 URL 목록 (8개)

1. Elicit: https://elicit.org/ → `elicit-main.png`
2. Perplexity: https://perplexity.ai/ → `perplexity-main.png`
3. NotebookLM: https://notebooklm.google.com/ → `notebooklm-main.png`
4. Consensus: https://consensus.app/ → `consensus-main.png`
5. Scite: https://scite.ai/ → `scite-main.png`
6. ResearchRabbit: https://researchrabbit.ai/ → `researchrabbit-main.png`
7. Connected Papers: https://www.connectedpapers.com/ → `connectedpapers-main.png`
8. Semantic Scholar: https://www.semanticscholar.org/ → `semanticscholar-main.png`

**저장 위치**: `resources/images/tools-ecosystem/`

## 사전 확인 체크리스트

- [ ] Cline MCP `webpageScreenshot` 서버 활성화 확인
- [ ] Node.js 20+ 버전 확인
- [ ] 디렉토리 구조 생성 확인
- [ ] Playwright Chromium 다운로드 확인

## 디렉토리 생성 명령

```bash
mkdir -p resources/images/tools-ecosystem
```

## 개별 스크린샷 생성 프롬프트 (8개)

### 프롬프트 1: Elicit

```
https://elicit.org/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/elicit-main.png로 저장해주세요.
```

- **URL**: https://elicit.org/
- **저장 경로**: `resources/images/tools-ecosystem/elicit-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., search interface, main features) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: AI 기반 논문 검색 및 요약 도구, 메인 인터페이스와 핵심 기능 표시
- **예상 파일 크기**: 1-2MB

### 프롬프트 2: Perplexity

```
https://perplexity.ai/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/perplexity-main.png로 저장해주세요.
```

- **URL**: https://perplexity.ai/
- **저장 경로**: `resources/images/tools-ecosystem/perplexity-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., search bar, example queries) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: AI 검색 엔진, 웹 검색 및 인용 기능 강조
- **예상 파일 크기**: 1-2MB

### 프롬프트 3: NotebookLM

```
https://notebooklm.google.com/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/notebooklm-main.png로 저장해주세요.
```

- **URL**: https://notebooklm.google.com/
- **저장 경로**: `resources/images/tools-ecosystem/notebooklm-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., main interface, feature highlights) are centered and fully visible within the viewport. 페이지 로드 완료 대기, Google 쿠키 배너 처리 필요 가능성
- **설명**: Google의 노트북 기반 연구 도구, 메인 랜딩 페이지
- **예상 파일 크기**: 1-2MB

### 프롬프트 4: Consensus

```
https://consensus.app/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/consensus-main.png로 저장해주세요.
```

- **URL**: https://consensus.app/
- **저장 경로**: `resources/images/tools-ecosystem/consensus-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., search interface, research features) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: 학술 연구 합의 도구, 메인 인터페이스와 검색 기능
- **예상 파일 크기**: 1-2MB

### 프롬프트 5: Scite

```
https://scite.ai/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/scite-main.png로 저장해주세요.
```

- **URL**: https://scite.ai/
- **저장 경로**: `resources/images/tools-ecosystem/scite-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., citation analysis features) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: 인용 분석 도구, 메인 인터페이스와 핵심 기능
- **예상 파일 크기**: 1-2MB

### 프롬프트 6: ResearchRabbit

```
https://researchrabbit.ai/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/researchrabbit-main.png로 저장해주세요.
```

- **URL**: https://researchrabbit.ai/
- **저장 경로**: `resources/images/tools-ecosystem/researchrabbit-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., research discovery features) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: 연구 발견 및 추천 도구, 메인 랜딩 페이지
- **예상 파일 크기**: 1-2MB

### 프롬프트 7: Connected Papers

```
https://www.connectedpapers.com/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/connectedpapers-main.png로 저장해주세요.
```

- **URL**: https://www.connectedpapers.com/
- **저장 경로**: `resources/images/tools-ecosystem/connectedpapers-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., graph visualization preview) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: 논문 연결 시각화 도구, 메인 인터페이스와 그래프 예시
- **예상 파일 크기**: 1-2MB

### 프롬프트 8: Semantic Scholar

```
https://www.semanticscholar.org/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/tools-ecosystem/semanticscholar-main.png로 저장해주세요.
```

- **URL**: https://www.semanticscholar.org/
- **저장 경로**: `resources/images/tools-ecosystem/semanticscholar-main.png`
- **캡처 옵션**: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., search bar, featured papers) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- **설명**: AI 기반 학술 검색 엔진, 메인 인터페이스
- **예상 파일 크기**: 1-2MB

## 실행 순서

1. 각 프롬프트를 Cline 대화창에 순차적으로 입력 (또는 배치 프롬프트 사용)
2. MCP 서버가 `capture_screenshot` 도구를 호출하는지 확인
3. 각 스크린샷 생성 완료 후 파일 존재 여부 확인
4. 생성된 이미지를 미리보기로 열어 품질 확인
5. 8개 스크린샷 생성 예상 시간: 약 10분 (배치 처리 시)

## 검증 체크리스트

- [ ] 8개 파일이 모두 지정된 경로에 생성됨
- [ ] 각 파일이 PNG 포맷임
- [ ] 이미지 해상도가 1920x1080임
- [ ] 파일 크기가 2MB 이하임
- [ ] 이미지가 정상적으로 열리고 내용이 선명함
- [ ] 파일명이 kebab-case 규칙을 따름
- [ ] 각 도구의 핵심 기능이 화면에 표시됨

## 트러블슈팅

- **타임아웃 오류**: 네트워크 연결 확인, URL 유효성 확인, 일부 도구는 로딩 시간이 길 수 있음
- **저장 경로 오류**: 디렉토리가 존재하는지 확인
- **Chromium 오류**: `pnpm playwright install --with-deps --only-shell chromium` 실행
- **권한 오류**: macOS에서 `chmod -R 755 resources/images/` 실행
- **로그인 필요 페이지**: 메인 랜딩 페이지만 캡처, 로그인 후 화면은 수동 캡처로 전환
- **쿠키 배너**: Google 서비스(NotebookLM)는 쿠키 배너가 나타날 수 있으므로 재시도 필요 가능성

## 배치 실행 옵션 (권장)

단일 프롬프트로 8개 스크린샷을 한 번에 생성 (시간 절약):

```
다음 8개 연구 도구의 스크린샷을 1920x1080 해상도로 캡처해주세요:
1. https://elicit.org/ → resources/images/tools-ecosystem/elicit-main.png
2. https://perplexity.ai/ → resources/images/tools-ecosystem/perplexity-main.png
3. https://notebooklm.google.com/ → resources/images/tools-ecosystem/notebooklm-main.png
4. https://consensus.app/ → resources/images/tools-ecosystem/consensus-main.png
5. https://scite.ai/ → resources/images/tools-ecosystem/scite-main.png
6. https://researchrabbit.ai/ → resources/images/tools-ecosystem/researchrabbit-main.png
7. https://www.connectedpapers.com/ → resources/images/tools-ecosystem/connectedpapers-main.png
8. https://www.semanticscholar.org/ → resources/images/tools-ecosystem/semanticscholar-main.png
```

## 참고 문서

- `cline-screenshot-mcp-setup.md`: MCP 서버 설정 가이드
- `part1-screenshot-generation-prompts.md`: Part 1 프롬프트 예시
- `part2-screenshot-generation-prompts.md`: Part 2 프롬프트 예시
- `troubleshooting-quick.md`: 트러블슈팅 가이드
- `24-37_screenshot_descriptions.md`: Part 3 스크린샷 요구사항

## 품질 기준

- 각 도구의 핵심 기능이 명확히 보여야 함
- 도구 간 비교가 가능하도록 일관된 캡처 스타일 유지
- 무료/유료 기능 차이가 있다면 메인 페이지에서 확인 가능해야 함
- 로고와 브랜딩이 명확히 표시되어야 함
