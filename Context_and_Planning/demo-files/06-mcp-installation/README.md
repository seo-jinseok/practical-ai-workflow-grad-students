# MCP 설치 시연 (Claude Desktop + task-master-mcp)

**목적**: Part 2 Section 4.1-4.2의 MCP 설치를 5분 시연  
**대상**: 초보자도 따라할 수 있는 단계별 설치 과정  
**도구**: Claude Desktop, VS Code (JSON 편집)  
**시연 시간**: 5분  

## 📁 Files in This Demo

- `installation-script.md`: 5분 시연 스크립트 (단계별 명령어)
- `config-template.json`: claude_desktop_config.json 템플릿
- `config-completed.json`: 완성된 설정 파일 예시 (4개 MCP 서버)
- `test-prompts.md`: 설치 확인용 테스트 프롬프트
- `troubleshooting-quick.md`: 빠른 문제 해결 가이드
- `screenshots-checklist.md`: 필요한 스크린샷 목록

## 🎯 Demonstration Flow (5 minutes)

### Step 1: Claude Desktop 확인 (1분)
- Claude Desktop 설치 및 실행 상태 확인
- 로그인 상태 및 메인 화면 소개
- "이미 설치되어 있다고 가정" 안내

### Step 2: 설정 파일 편집 (2분)
- 설정 파일 경로 설명 (macOS/Windows)
- VS Code에서 JSON 파일 편집 과정
- task-master-mcp 설정 추가 (복사-붙여넣기)
- JSON 문법 강조 (쉼표, 따옴표, 중괄호)

### Step 3: Claude 재시작 및 확인 (1분)
- Claude Desktop 완전 종료 후 재시작
- 새 대화에서 MCP 작동 확인
- 간단한 테스트 프롬프트 실행

### Step 4: 사용 예시 (1분)
- 간단한 프로젝트 정보 입력
- task-master-ai 응답 확인
- 대안 도구 언급 (ChatGPT, Claude Projects)

## 💡 Key Messages

- "MCP 설치는 생각보다 간단합니다"
- "JSON 파일 하나만 편집하면 됩니다"
- "설치 어려우면 대안 도구를 사용하세요"
- "도구가 아닌 원칙이 중요합니다"

## 🚨 Backup Plan

**Claude Desktop 없음**: 스크린샷으로 설명, "설치는 자료 참고"

**MCP 연결 실패**: 미리 준비한 응답 파일 사용, "기술적 문제"

**시간 부족**: Step 1-2만 시연, 나머지는 자료 참고 안내

## 🔄 Alternatives Mentioned

**필수 언급** (중요):
- ChatGPT Custom GPTs
- Claude Projects (MCP 없이)
- Notion AI
- "도구가 아닌 원칙이 중요합니다"

## 🔗 Connection to Part 2

- **Reference**: Part 2 Section 4.1 (MCP 설치 및 설정)
- **Resource**: `v13.0_resources/part2/15_mcp_installation_guide.md`
- **Next**: Section 4.2 (task-master-mcp 실습)

## ⚠️ Important Notes

### 초보자 친화적 접근
- "코딩을 모르셔도 괜찮습니다" 강조
- 복사-붙여넣기 중심 가이드
- 천천히, 단계별로 설명

### 대안 도구 반드시 언급
- 설치가 어려운 경우 자연스럽게 전환
- "개념만 이해해도 충분" 강조
- 실용성 vs 편의성 균형

### 트러블슈팅 준비
- JSON 문법 오류 → VS Code 문법 강조 활용
- MCP 인식 안 됨 → 재시작 방법 안내
- 완전 실패 → 백업 자료로 전환

---

**강사 팁**: "복잡해 보여도 실제로는 복사-붙여넣기입니다. 중요한 것은 개념을 이해하는 것입니다."
