# Part 2 문제 해결 가이드

## 목적
- Part 2에서 다루는 도구들의 일반적 문제와 해결 방법
- 설치, 설정, 사용过程中的 주요 오류 해결
- 대안 방법 및 문제 예방 가이드

## MCP 관련 문제

### 설치 문제
**오류**: MCP 설치 실패
```
Error: Command not found: mcp
```
**해결 방법**:
1. **Node.js 설치 확인**: Node.js 18+ 필요
```bash
node --version
```
2. **NPM 권한 확인**: 관리자 권한으로 설치
```bash
sudo npm install -g @modelcontextprotocol/mcp
```
3. **대안 설치 방법**: `part2/15_mcp_installation_guide.md` 참조

**대안**: 도커 컨테이너 사용
```bash
docker run -it node:18 bash
npm install -g @modelcontextprotocol/mcp
```

### 연동 문제
**오류**: VS Code에서 MCP 서버 연결 실패
```
Failed to connect to MCP server
```
**해결 방법**:
1. **설정 파일 확인**: `~/.vscode/settings.json`
```json
{
  "mcp.servers": {
    "task-master": {
      "command": "npx",
      "args": ["-y", "--package=task-master-ai", "task-master-ai"]
    }
  }
}
```
2. **서버 재시작**: VS Code 완전 재시작
3. **로그 확인**: Developer Tools (Ctrl+Shift+I) → Console 탭

## Task Master 관련 문제

### 프로젝트 초기화 실패
**오류**: Task Master가 프로젝트를 인식하지 못함
```
No project found in current directory
```
**해결 방법**:
1. **프로젝트 폴더 확인**: 현재 디렉토리가 프로젝트 루트인지
2. **명시적 초기화**: `taskmaster init [project-name]`
3. **설정 파일 생성**: `.taskmaster/config.json` 수동 생성

### 작업 업데이트 오류
**오류**: 작업 상태 변경 시 오류 발생
```
Error: Invalid task ID or status
```
**해결 방법**:
1. **올바른 ID 형식**: `task-001`, `subtask-001.1` 형태
2. **유효한 상태**: `pending`, `in-progress`, `done`, `cancelled`
3. **권한 확인**: 프로젝트 폴더에 쓰기 권한 확인

## SpecKit 관련 문제

### 설치 및 설정
**오류**: SpecKit CLI 명령어 인식 불가
```
zsh: command not found: specify
```
**해결 방법**:
1. **Python 경로 확인**: `which python3`
2. **PATH 추가**: `export PATH="$HOME/.local/bin:$PATH"`
3. **재설치**: `pip uninstall specify-cli && pip install specify-cli`

### 프로젝트 생성 오류
**오류**: 프로젝트 폴더 생성 실패
```
PermissionError: [Errno 13] Permission denied
```
**해결 방법**:
1. **쓰기 권한 확인**: `ls -la`로 디렉토리 권한 확인
2. **다른 위치 시도**: 홈 디렉토리나 writable 폴더 사용
3. **소유자 변경**: `sudo chown -R $USER:$USER .`

### 템플릿 생성 실패
**오류**: 기본 템플릿 파일 생성 오류
```
TemplateNotFound: default template not found
```
**해결 방법**:
1. **템플릿 재설치**: `specify --reinstall-templates`
2. **수동 복사**: 템플릿을 `~/.specify/templates/`에 수동 복사
3. **대안 사용**: Markdown 템플릿으로 직접 작성

## AI 도구 연동 문제

### Copilot 연결 오류
**오류**: VS Code에서 Copilot 확장 오류
```
GitHub Copilot is not responding
```
**해결 방법**:
1. **확장 재시작**: VS Code 완전 재시작
2. **로그인 재확인**: GitHub 계정 재인증
3. **권한 확인**: GitHub Student Pack 혜택 유효성 확인

### API 키 오류
**오류**: AI 모델 API 키 유효성 오류
```
Invalid API key or insufficient credits
```
**해결 방법**:
1. **키 유효성 확인**: 제공업체 대시보드에서 확인
2. **크레딧 잔액**: API 크레딧 및 요금제 확인
3. **환경변수**: API 키가 올바르게 설정되었는지 확인

## 성능 및 최적화 문제

### 응답 속도 저하
**증상**: AI 응답이 매우 느림 (>30초)
**해결 방법**:
1. **요청 크기 축소**: 더 작은 단위로 요청 분할
2. **캐싱 활용**: 반복 작업은 캐시된 결과 활용
3. **네트워크 확인**: 인터넷 연결 상태 점검

### 메모리 사용량 과다
**증상**: 시스템 응답성 저하
**해결 방법**:
1. **프로세스 정리**: 필요 없는 AI 프로세스 종료
2. **프로젝트 분리**: 큰 프로젝트를 더 작은 단위로 분할
3. **리소스 모니터링**: `htop` 또는 `Activity Monitor`로 확인

## 데이터 및 문서 문제

### 파일 동기화 오류
**증상**: 로컬과 원격 파일 간 불일치
**해결 방법**:
1. **Git 상태 확인**: `git status`로 변경사항 확인
2. **강제 동기화**: `git pull --rebase` 또는 강제 푸시
3. **백업 생성**: 중요 변경사항은 백업 후 동기화

### 문서 형식 오류
**증상**: 생성된 문서의 형식 문제
**해결 방법**:
1. **템플릿 확인**: 올바른 템플릿을 사용했는지 확인
2. **Markdown 검증**: Markdown 문법 검증 도구 사용
3. **일관성 유지**: 전체 프로젝트에서 동일한 포맷팅 규칙 적용

## 대안 접근 방법

### 도구 사용 불가 시
1. ** manuelle 접근**: 전통적 방법 (문서 작성, 스프레드시트)
2. **경량 도구**: 더 간단한 AI 도구로 대체
3. **온라인 서비스**: 웹 기반 AI 도구 활용

### 시간 제약 상황
1. **핵심 기능만**: 필수 기능에 집중
2. **단계적 적용**: 복잡한 통합은 나중에
3. **템플릿 활용**: 기존 템플릿 적극 활용

## 예방 방법

### 정기 점검
- **주간 점검**: 설정 파일 및 권한 확인
- **백업**: 중요한 설정 및 문서 정기 백업
- **업데이트**: 도구 및 확장 프로그램 최신 버전 유지

### 문서화
- **작업 로그**: 문제 해결 과정 기록
- **설정 기록**: 성공적인 설정 환경 문서화
- **체크리스트**: 반복 작업용 체크리스트 작성

## 관련 리소스
- **MCP 설치**: `part2/15_mcp_installation_guide.md`
- **Task Master**: `16_task_master_mcp_tutorial.md`
- **SpecKit 설치**: `part2/19_speckit_installation_guide.md`
- **실습 프로젝트**: `21_speckit_practice_project.md`
- **전체 튜토리얼**: `../Context_and_Planning/demo-files/`

---
**마지막 업데이트**: 2025-11-11  
**버전**: Part 2
