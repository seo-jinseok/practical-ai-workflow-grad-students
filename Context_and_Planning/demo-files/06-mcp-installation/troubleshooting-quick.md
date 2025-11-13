# MCP 설치 빠른 문제 해결 가이드

## 🚨 가장 자주 발생하는 MCP 설치 문제들

### 1. JSON 구문 오류 (가장 일반적)

**증상**:
- Claude Desktop 재시작 후 MCP가 인식되지 않음
- "구문 오류" 또는 "파싱 실패" 메시지

**원인**:
- 쉼표(,) 누락 또는 과다 사용
- 마지막 쉼표 포함
- 불균형한 중괄호 `{}` 또는 대괄호 `[]`
- 따옴표 내부에 이스케이프되지 않은 따옴표

**해결 방법**:
1. VS Code에서 JSON 파일 열기
2. Command Palette (Cmd+Shift+P) → "Format Document"
3. VS Code가 빨간색으로 표시하는 위치 확인
4. 가장자리까지 잘라내어 붙여넣기 (복사 오류 방지)

**올바른 JSON 형식 예시**:
```json
{
  "mcpServers": {
    "taskmaster": {
      "command": "npx",
      "args": ["-y", "--package=task-master-ai", "task-master-ai"]
    }
  }
}
```

### 2. Claude Desktop 재시작 문제

**증상**:
- 설정 변경 후에도 새 MCP가 보이지 않음
- 기존 MCP만 작동, 새 MCP 인식 안됨

**올바른 재시작 단계**:
1. Claude Desktop 완전 종료 ( dock에서 우클릭 → Quit)
2. 5초간 대기
3. 다시 실행 후 새 대화 시작
4. 기존 대화는 이전 설정을 사용하므로 새 대화에서만 새 MCP 확인 가능

**주의사항**:
- 창 닫기만으로는 충분하지 않음
- 시스템 Tray 완전히 종료 확인
- 관리자 권한 필요시 "，실행 중인 모든 Claude 프로세스 종료"

### 3. npm/npx 권한 문제

**증상**:
- "permission denied" 오류
- "command not found: npx"

**해결 방법**:
```bash
# npm 권한 수정
sudo chown -R $USER ~/.npm
sudo chown -R $USER /usr/local/bin

# npx 다시 설치
npm install -g npx
```

### 4. 경로 문제 (Windows)

**증상**:
- 설정 파일을 찾을 수 없음
- 권한 거부 오류

**해결 방법**:
1. `%APPDATA%` 폴더로 이동
2. `Claude` 폴더 생성 (없는 경우)
3. `claude_desktop_config.json` 파일 생성
4. 관리자 권한으로 실행하여 파일 저장

### 5. 방화벽/네트워크 문제

**증상**:
- npx 설치 후 응답 없음
- 연결 제한 오류

**해결 방법**:
```bash
# 프록시 환경이 아닌지 확인
env | grep -i proxy

# npm 레지스트리 교체
npm config set registry https://registry.npmjs.org/
```

## 🔧 단계별 진단 체크리스트

### 기본 확인
- [ ] Claude Desktop 최신 버전 실행 중
- [ ] 설정 파일 위치 올바름 (OS별 경로 확인)
- [ ] JSON 파일 문법 유효성 (VS Code Format Document)
- [ ] 파일 권한 (읽기/쓰기 가능)

### 고급 확인
- [ ] npx 전역 설치 확인: `npx --version`
- [ ] npm 캐시 정리: `npm cache clean --force`
- [ ] 노드 버전 확인: `node --version` (v20+ 권장)
- [ ] 백그라운드 프로세스 중지 후 재시작

## 🚀 빠른 해결 순서

1. **JSON 문법 먼저 확인** (90% 문제 해결)
2. **완전 재시작** (새 대화 포함)
3. **명령줄에서 테스트**: `npx -y --package=task-master-ai task-master-ai`
4. **권한 문제 확인**
5. **최후 수단**: 설정 파일 전체 삭제 후 다시 생성

## 💡 예방 팁

### 설치 전
- JSON 포맷터를 VS Code에서 활성화
- 기존 설정 파일 백업
- 버전 호환성 확인 (Claude Desktop + npx)

### 설치 중
- 한 번에 하나의 MCP 서버만 추가
- 작업 완료 후 즉시 재시작 테스트
- 테스트 프롬프트로 즉시 확인

### 설치 후
- 설정 파일 변경 시마다 재시작 확인
- 정기적인 백업 설정
- 버전 업데이트 전 준비

## 🆘 대안 도구 사용

MCP 설치가 어려운 경우:
- **ChatGPT**: Custom GPTs (기능 제한 있음)
- **Claude Projects**: MCP 없이 작업 관리
- **Notion AI**: 간단한 작업 추적
- **Obsidian**: 로컬 노트 관리

## 📞 추가 지원

문제 지속 시:
1. Claude Desktop 로그 확인
2. npx 버전 업그레이드: `npm update -g npx`
3. OS별 권한 설정 재검토
4. 백업 도구로 대체 고려

## 📸 Cline MCP 스크린샷 서버 문제 해결

### 6. Chromium 다운로드 실패

**증상**:
- 스크린샷 캡처 시 "Chromium download failed" 오류
- 네트워크 타임아웃 메시지

**해결 방법**:
```bash
# Chromium 캐시 정리
rm -rf ~/.cache/puppeteer
rm -rf ~/Library/Caches/puppeteer

# 수동 Chromium 설치
npm install puppeteer --save
npx puppeteer browsers install chromium

# 또는 환경 변수 설정
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
export PUPPETEER_EXECUTABLE_PATH=$(which chromium)
```

### 7. 타임아웃 오류

**증상**:
- 스크린샷 생성이 오래 걸리다가 타임아웃
- "Navigation timeout" 또는 "Page load timeout" 메시지

**해결 방법**:
```bash
# 타임아웃 설정 증가 (프롬프트에서 지정)
스크린샷을 생성할 때 타임아웃을 30초로 설정해주세요.

# 네트워크 속도 확인
ping -c 4 google.com

# 캐시 정리
npm cache clean --force
```

### 8. 경로 권한 문제

**증상**:
- 스크린샷 저장 시 "permission denied" 오류
- 지정된 폴더에 파일이 생성되지 않음

**해결 방법**:
```bash
# 저장 경로 권한 확인
ls -la v13.0_resources/images/

# 권한 부여
chmod 755 v13.0_resources/images/
chmod 755 v13.0_resources/images/part1/

# 절대 경로 사용
mkdir -p /absolute/path/to/v13.0_resources/images/
```

### 9. MCP Inspector 실행 및 도구 테스트

**MCP Inspector 실행**:
```bash
# MCP Inspector 설치 및 실행
npx -y @modelcontextprotocol/inspector npx -y @srigi/mcp-webpage-screenshot
```

**도구 테스트 방법**:
1. MCP Inspector 브라우저에서 열기
2. "Tools" 탭에서 `capture_screenshot` 확인
3. 테스트 입력:
   ```json
   {
     "url": "https://example.com",
     "outputPath": "test-screenshot.png"
   }
   ```
4. "Run Tool" 클릭하여 결과 확인

### 10. Cline 설정 파일 경로 (macOS)

**설정 파일 위치**:
```
~/Library/Application Support/Code/User/globalStorage/saoudrizwan.cline/cline_mcp_settings.json
```

**편집 후 적용**:
1. Cline 확장 재시작 (VS Code 재시작)
2. Cline 패널에서 "MCP Servers" 탭 확인
3. 서버 상태가 "Connected"인지 확인

### 11. MCP 자동화 실패 시 수동 캡처 대체 (2025-11-12)

**증상**:
- Cline MCP `webpageScreenshot` 서버가 설정되지 않아 자동화 실패
- MCP 설정 파일이 존재하지 않음
- 스크린샷 생성 요청이 처리되지 않음

**원인**:
- `cline_mcp_settings.json` 파일이 생성되지 않음
- webpageScreenshot 서버가 설치/설정되지 않음
- Node.js 버전은 25.1.0으로 호환되나 MCP 서버 미설정

**해결 방법 (수동 캡처)**:
1. Chrome 브라우저에서 대상 URL 열기:
   - https://modelcontextprotocol.io/ (MCP 프로토콜 소개)
   - https://github.com/github/spec-kit (SpecKit 리포지토리)

2. 개발자 도구로 해상도 설정:
   - F12 키로 DevTools 열기
   - Device Toolbar 활성화 (Ctrl+Shift+M / Cmd+Shift+M)
   - 해상도 1920x1080으로 설정
   - 페이지 스크롤하여 주요 콘텐츠 표시

3. 스크린샷 캡처:
   - 우클릭 → "Save as" 또는 "스크린샷 캡처"
   - PNG 형식으로 저장
   - 파일명: `mcp-protocol-intro.png`, `speckit-repository.png`
   - 저장 경로: `v13.0_resources/part2/images/`

4. 품질 검증:
   - 파일 크기 2MB 이하 확인
   - 해상도 1920x1080 확인
   - 콘텐츠 선명도 및 완전성 확인

**결과**:
- 2025-11-12 Chrome DevTools 수동 캡처로 2개 PNG 파일 생성
- 파일 크기: mcp-protocol-intro.png (182KB), speckit-repository.png (263KB)
- 해상도: 1920x1080, PNG 형식 확인
- 2025-11-13 검증 결과에 따라 문서 및 체크리스트 갱신

**예방 조치**:
- 향후 MCP 자동화 재시도 시 설정 파일 우선 확인
- 수동 캡처를 백업 방법으로 유지
- 문서에 자동화/수동 방법 모두 명시

### 12. Python Playwright 실행 시 macOS `bootstrap_check_in` 오류 (2025-11-13)

**증상**:
- `python3 capture_screenshots.py` 실행 즉시 Chromium/Chrome 프로세스가 종료되며
  `bootstrap_check_in ... Permission denied (1100)` 로그 출력
- WebKit 백엔드 사용 시 `Abort trap: 6`로 종료

**원인**:
- macOS 보안 정책(TCC/Quarantine)으로 CLI에서 실행된 Playwright 브라우저가
  Mach 포트 등록에 실패

**시도한 해결**:
1. Playwright 런타임 설치
   - `python3 -m pip install --user playwright`
   - `python3 -m playwright install chromium`
   - `python3 -m playwright install webkit`
2. 실행 권한 해제
   - `xattr -dr com.apple.quarantine /Users/truestone/Library/Caches/ms-playwright`
   - `xattr -dr com.apple.quarantine /Users/truestone/Library/Caches/ms-playwright/webkit-2215`
3. 런처 옵션 변경
   - `channel="chrome"` 및 WebKit 백엔드 시도

**결과**:
- 모든 런처에서 동일 오류 발생 → 자동화 캡처 미완료
- 기존 수동 캡처(2025-11-12) PNG 자산을 검증 후 유지

**대안**:
- macOS GUI 세션 또는 Codesigned 환경에서 Playwright 실행
- Chrome DevTools 수동 캡처 절차 문서화 및 백업 유지

---

**참고**: "도구가 중요한 것이 아니라 원칙을 이해하는 것이 중요합니다. 설치에 시간이 너무 오래 걸리면 대안을 먼저 사용해보세요."
