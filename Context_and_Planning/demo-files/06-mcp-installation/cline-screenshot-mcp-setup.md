# Cline Screenshot MCP 설치 가이드

## 사전 준비

### Node.js 버전 확인
Cline MCP 서버를 사용하기 위해서는 Node.js 20+ 버전이 필요합니다.

```bash
node --version
```

버전이 20 미만인 경우, 다음 명령어로 최신 LTS 버전을 설치하세요:

```bash
# macOS에서 Homebrew 사용
brew install node

# 또는 nvm 사용
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
nvm use --lts
```

## Cline MCP 설정 파일 경로

macOS에서 Cline MCP 설정 파일은 다음 경로에 위치합니다:

```
~/Library/Application Support/Code/User/globalStorage/saoudrizwan.cline/cline_mcp_settings.json
```

## webpageScreenshot 서버 추가

1. Cline 설정 파일을 열고 `mcpServers` 섹션을 찾습니다.
2. 다음 서버 설정을 추가합니다:

```json
{
  "mcpServers": {
    "webpageScreenshot": {
      "command": "npx",
      "args": ["-y", "@srigi/mcp-webpage-screenshot"],
      "env": {}
    }
  }
}
```

3. `autoApprove` 설정에 스크린샷 관련 도구를 추가합니다:

```json
{
  "autoApprove": [
    "webpageScreenshot-capture_screenshot",
    "webpageScreenshot-capture_full_page_screenshot"
  ]
}
```

## 스크린샷 저장 경로 지정

프롬프트에서 저장 경로를 지정할 때는 다음과 같이 사용합니다:

```
스크린샷을 v13.0_resources/images/ 폴더에 저장해주세요.
```

## 설치 후 확인 절차

1. Cline을 재시작합니다 (VS Code 재시작).
2. Cline 패널에서 "MCP Servers" 섹션을 확인합니다.
3. webpageScreenshot 서버가 정상적으로 로드되었는지 확인합니다.
4. 도구 목록에서 다음 도구들이 표시되는지 확인:
   - capture_screenshot
   - capture_full_page_screenshot

## 기본 테스트 시나리오

### 기본 테스트
```
example.com 웹사이트의 스크린샷을 캡처해주세요.
```

### 고급 옵션 테스트
```
https://github.com의 전체 페이지를 캡처하고 v13.0_resources/images/github-fullpage.png로 저장해주세요.
```

## 관련 문서

- [트러블슈팅 가이드](troubleshooting-quick.md)
- [테스트 프롬프트](screenshot-test-prompts.md)
- [설정 예시](cline-mcp-config-example.json)
