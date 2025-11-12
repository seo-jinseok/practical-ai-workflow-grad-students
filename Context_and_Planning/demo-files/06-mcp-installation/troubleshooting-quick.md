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
- [ ] 노드 버전 확인: `node --version` (v14 이상 권장)
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

---

**참고**: "도구가 중요한 것이 아니라 원칙을 이해하는 것이 중요합니다. 설치에 시간이 너무 오래 걸리면 대안을 먼저 사용해보세요."
