# Part 1 스크린샷 생성 프롬프트 스크립트

Part 1의 3개 웹페이지 스크린샷을 생성하기 위한 Cline MCP 프롬프트 스크립트를 작성합니다.

## 대상 URL 목록

- https://education.github.com/pack → `github-education-pack-main.png` (resources/images/part1/github-education/)
- https://github.com/features/copilot/plans → `copilot-plans-comparison.png` (resources/images/part1/github-education/)
- https://code.visualstudio.com/ → `vscode-download-page.png` (resources/images/part1/vscode-setup/)

## 사전 확인 체크리스트

- [ ] Cline MCP `webpageScreenshot` 서버가 활성화되어 있는지 확인
- [ ] Node.js 20+ 버전 확인
- [ ] 디렉토리 구조가 생성되었는지 확인
- [ ] Playwright Chromium이 다운로드되었는지 확인 (첫 실행 시 자동)

### 디렉토리 생성 명령

```bash
mkdir -p resources/images/part1/github-education resources/images/part1/vscode-setup
```

## 스크린샷 생성 프롬프트 (3개)

각 프롬프트는 다음 형식을 따릅니다:
```
[URL]의 스크린샷을 1920x1080 해상도로 캡처하고 [저장경로/파일명.png]로 저장해주세요.
```

### 프롬프트 1: GitHub Education Pack
```
https://education.github.com/pack의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/part1/github-education/github-education-pack-main.png로 저장해주세요.
```
- URL: https://education.github.com/pack
- 저장 경로: `resources/images/part1/github-education/github-education-pack-main.png`
- 캡처 옵션: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., 'Get your pack' button) are centered and fully visible within the viewport. 페이지 로드 완료 대기 후 쿠키 배너 수락
- 예상 파일 크기: 1-2MB

### 프롬프트 2: Copilot Plans 비교
```
https://github.com/features/copilot/plans의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/part1/github-education/copilot-plans-comparison.png로 저장해주세요.
```
- URL: https://github.com/features/copilot/plans
- 저장 경로: `resources/images/part1/github-education/copilot-plans-comparison.png`
- 캡처 옵션: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., comparison table) are centered and fully visible within the viewport. 페이지 로드 완료 대기 후 쿠키 배너 수락
- 예상 파일 크기: 1-2MB

### 프롬프트 3: VS Code 다운로드 페이지
```
https://code.visualstudio.com/의 스크린샷을 1920x1080 해상도로 캡처하고 resources/images/part1/vscode-setup/vscode-download-page.png로 저장해주세요.
```
- URL: https://code.visualstudio.com/
- 저장 경로: `resources/images/part1/vscode-setup/vscode-download-page.png`
- 캡처 옵션: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., download section) are centered and fully visible within the viewport. 페이지 로드 완료 대기 후 메인 다운로드 페이지, OS별 버전 표시 부분 포함
- 예상 파일 크기: 1-2MB

## 실행 순서

- 각 프롬프트를 Cline 대화창에 순차적으로 입력
- MCP 서버가 `capture_screenshot` 도구를 호출하는지 확인 (뷰포트 모드)
- 각 스크린샷 생성 완료 후 파일 존재 여부 확인
- 생성된 이미지를 미리보기로 열어 품질 확인

## 검증 체크리스트

- [ ] 3개 파일이 모두 지정된 경로에 생성됨
- [ ] 각 파일이 PNG 포맷임
- [ ] 이미지 해상도가 정확히 1920x1080임
- [ ] 파일 크기가 2MB 이하임 (압축 필요 시 TinyPNG 사용)
- [ ] 이미지가 정상적으로 열리고 내용이 선명함
- [ ] 파일명이 kebab-case 규칙을 따름

## 트러블슈팅

- **타임아웃 오류**: 네트워크 연결 확인, URL 유효성 확인
- **저장 경로 오류**: 디렉토리가 존재하는지 확인, 절대 경로 대신 상대 경로 사용
- **Chromium 오류**: `pnpm playwright install --with-deps --only-shell chromium` 실행
- **권한 오류**: macOS에서 `chmod -R 755 resources/images/` 실행

## 배치 실행 옵션 (선택사항)

단일 프롬프트로 3개 스크린샷을 한 번에 생성하는 방법:
```
다음 3개 URL의 스크린샷을 1920x1080 해상도로 캡처해주세요:
1. https://education.github.com/pack → resources/images/part1/github-education/github-education-pack-main.png
2. https://github.com/features/copilot/plans → resources/images/part1/github-education/copilot-plans-comparison.png
3. https://code.visualstudio.com/ → resources/images/part1/vscode-setup/vscode-download-page.png
```

## 참고 문서

- `cline-screenshot-mcp-setup.md`: MCP 서버 설정 가이드
- `screenshot-test-prompts.md`: 일반 테스트 프롬프트 예시
- `troubleshooting-quick.md`: 트러블슈팅 가이드
