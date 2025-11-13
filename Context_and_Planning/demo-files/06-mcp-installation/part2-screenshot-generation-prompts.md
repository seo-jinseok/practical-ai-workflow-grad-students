# Part 2 스크린샷 생성 프롬프트 스크립트

## 목적

Part 2의 2개 웹페이지 스크린샷을 MCP 자동화로 생성합니다.
MCP 관련 공식 문서 페이지를 대상으로 합니다.

## 대상 URL 목록

- [MCP Protocol Introduction](https://modelcontextprotocol.io/) → `mcp-protocol-intro.png` (v13.0_resources/part2/images/)
- [SpecKit Repository](https://github.com/github/spec-kit) → `speckit-repository.png` (v13.0_resources/part2/images/)

## 사전 확인 체크리스트

- [x] Cline MCP `webpageScreenshot` 서버 활성화 확인
- [x] Node.js 20+ 버전 확인
- [x] 디렉토리 구조 생성 확인 (`v13.0_resources/part2/images/`)
- [x] Playwright Chromium 다운로드 확인

## 디렉토리 생성 명령

```bash
mkdir -p v13.0_resources/part2/images
```

## 스크린샷 생성 프롬프트

### 프롬프트 1: MCP 프로토콜 소개 페이지

```text
https://modelcontextprotocol.io/의 스크린샷을 1920x1080 해상도로 캡처하고 v13.0_resources/part2/images/mcp-protocol-intro.png로 저장해주세요.
```

- URL: [MCP Protocol](https://modelcontextprotocol.io/)
- 저장 경로: `v13.0_resources/part2/images/mcp-protocol-intro.png`
- 캡처 옵션: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., protocol overview, key features) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- 설명: MCP(Model Context Protocol) 공식 소개 페이지, 프로토콜 개요 및 주요 기능 표시
- 예상 파일 크기: 1-2MB

### 프롬프트 2: SpecKit 리포지토리

```text
https://github.com/github/spec-kit의 스크린샷을 1920x1080 해상도로 캡처하고 v13.0_resources/part2/images/speckit-repository.png로 저장해주세요.
```

- URL: [SpecKit Repository](https://github.com/github/spec-kit)
- 저장 경로: `v13.0_resources/part2/images/speckit-repository.png`
- 캡처 옵션: Set viewport to 1920x1080 and capture the visible area after scrolling to ensure key elements (e.g., README content, repository description) are centered and fully visible within the viewport. 페이지 로드 완료 대기
- 설명: GitHub SpecKit 리포지토리 메인 페이지, README 및 프로젝트 설명 표시
- 예상 파일 크기: 1-2MB

## 실행 순서

- 각 프롬프트를 Cline 대화창에 순차적으로 입력
- MCP 서버가 `capture_screenshot` 도구를 호출하는지 확인
- 각 스크린샷 생성 완료 후 파일 존재 여부 확인
- 생성된 이미지를 미리보기로 열어 품질 확인

## 검증 체크리스트

- [ ] 2개 파일이 모두 지정된 경로에 생성됨
    - [ ] 각 파일이 PNG 포맷임
    - [ ] 이미지 해상도가 1920x1080임
    - [ ] 파일 크기가 2MB 이하임
    - [ ] 이미지가 정상적으로 열리고 내용이 선명함
    - [ ] 파일명이 kebab-case 규칙을 따름

## 트러블슈팅

- **타임아웃 오류**: 네트워크 연결 확인, URL 유효성 확인
- **저장 경로 오류**: 디렉토리가 존재하는지 확인
- **Chromium 오류**: `pnpm playwright install --with-deps --only-shell chromium` 실행
- **권한 오류**: macOS에서 `chmod -R 755 v13.0_resources/part2/images/` 실행

## 배치 실행 옵션 (선택사항)

단일 프롬프트로 2개 스크린샷을 한 번에 생성:

```text
다음 2개 URL의 스크린샷을 1920x1080 해상도로 캡처해주세요:
1. https://modelcontextprotocol.io/ → v13.0_resources/part2/images/mcp-protocol-intro.png
2. https://github.com/github/spec-kit → v13.0_resources/part2/images/speckit-repository.png
```

## 참고 문서

- `cline-screenshot-mcp-setup.md`: MCP 서버 설정 가이드
- `part1-screenshot-generation-prompts.md`: Part 1 프롬프트 예시
- `troubleshooting-quick.md`: 트러블슈팅 가이드
- `12_screenshot_descriptions.md`: Part 2 스크린샷 요구사항
