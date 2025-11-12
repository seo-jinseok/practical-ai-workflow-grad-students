# Screenshot MCP 테스트 프롬프트 가이드

## 저장 경로 구조

**기본 저장 경로**: `v13.0_resources/images/`

### Part별 폴더 구조
- **Part 1**: `v13.0_resources/images/part1/[category]/[filename].png`
- **Part 2**: `v13.0_resources/images/part2/[filename].png`
- **Part 3**: `v13.0_resources/images/part3/tools-ecosystem/[filename].png`

### 파일명 규칙
- `[도구명]-[기능]-[단계].png`
- `[웹사이트명]-screenshot.png`
- `[카테고리]-[설명].png`

**예시**:
- `github-education-pack-main.png`
- `vscode-extensions-marketplace.png`
- `elicit-search-interface.png`

## 기본 테스트

- [ ] **단순 웹사이트 캡처**
  ```
  example.com 웹사이트의 스크린샷을 캡처해주세요.
  ```
  - 예상 결과: v13.0_resources/images/example-com-screenshot.png
  - 저장 경로: v13.0_resources/images/

- [ ] **특정 URL 캡처**
  ```
  https://github.com/microsoft/vscode의 스크린샷을 찍어주세요.
  ```
  - 예상 결과: v13.0_resources/images/github-vscode-screenshot.png
  - 저장 경로: v13.0_resources/images/

## 프로젝트 특화 테스트

### Part 1 대상
- [ ] **GitHub Copilot 기능**
  ```
  https://github.com/features/copilot의 전체 페이지를 캡처하고 v13.0_resources/images/part1/copilot-features/fullpage.png로 저장해주세요.
  ```
  - 예상 결과: 전체 페이지 스크린샷
  - 저장 경로: v13.0_resources/images/part1/copilot-features/

- [ ] **VS Code 설정**
  ```
  https://code.visualstudio.com/docs의 뷰포트 스크린샷을 v13.0_resources/images/part1/vscode-setup/viewport.png로 저장해주세요.
  ```
  - 예상 결과: 현재 보이는 영역만 캡처
  - 저장 경로: v13.0_resources/images/part1/vscode-setup/

### Part 2 대상
- [ ] **GitHub Projects**
  ```
  https://github.com/features/issues의 스크린샷을 v13.0_resources/images/part2/github-projects/issues.png로 저장해주세요.
  ```
  - 예상 결과: 표준 스크린샷
  - 저장 경로: v13.0_resources/images/part2/

### Part 3 대상
- [ ] **연구 도구**
  ```
  https://scholar.google.com의 스크린샷을 v13.0_resources/images/part3/tools-ecosystem/google-scholar.png로 저장해주세요.
  ```
  - 예상 결과: 스크린샷
  - 저장 경로: v13.0_resources/images/part3/tools-ecosystem/

## 고급 옵션

- [ ] **풀페이지 캡처**
  ```
  https://www.npmjs.com의 전체 페이지를 캡처하고 v13.0_resources/images/advanced/fullpage.png로 저장해주세요.
  ```
  - 예상 결과: 스크롤된 전체 페이지
  - 저장 경로: v13.0_resources/images/advanced/

- [ ] **뷰포트 지정**
  ```
  https://reactjs.org의 1920x1080 뷰포트 스크린샷을 v13.0_resources/images/advanced/viewport-1920.png로 저장해주세요.
  ```
  - 예상 결과: 지정된 해상도의 스크린샷
  - 저장 경로: v13.0_resources/images/advanced/

## 배치 생성 예시

- [ ] **다중 URL 배치**
  ```
  다음 URL들의 스크린샷을 배치로 생성해주세요:
  1. https://github.com - v13.0_resources/images/batch/github.png
  2. https://stackoverflow.com - v13.0_resources/images/batch/stackoverflow.png
  3. https://developer.mozilla.org - v13.0_resources/images/batch/mdn.png
  ```
  - 예상 결과: 3개의 스크린샷 파일
  - 저장 경로: v13.0_resources/images/batch/

## 오류 재시도 지침

- [ ] **타임아웃 오류 시**
  - 프롬프트를 더 간단하게 만들기
  - URL이 유효한지 확인
  - 네트워크 연결 상태 확인

- [ ] **권한 오류 시**
  - 저장 경로가 존재하는지 확인
  - 폴더 쓰기 권한 확인
  - 절대 경로 대신 상대 경로 사용

- [ ] **Chromium 다운로드 실패 시**
  - Node.js 버전 확인 (20+ 권장)
  - 인터넷 연결 확인
  - 프록시 설정 확인

## 예상 결과 확인

모든 테스트 후 다음을 확인하세요:
- [ ] 파일이 지정된 경로에 생성됨
- [ ] 이미지 파일이 정상적으로 열림
- [ ] 해상도와 품질이 적절함
- [ ] 파일명이 올바르게 지정됨
