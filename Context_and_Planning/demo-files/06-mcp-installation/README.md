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
- `cline-screenshot-mcp-setup.md`: Cline 전용 스크린샷 MCP 설치 가이드
- `cline-mcp-config-example.json`: Cline MCP 설정 파일 예시
- `screenshot-test-prompts.md`: 스크린샷 MCP 테스트 프롬프트 가이드
- `part1-screenshot-generation-prompts.md`: Part 1 웹페이지 스크린샷 생성 프롬프트 스크립트
- `part2-screenshot-generation-prompts.md`: Part 2 웹페이지 스크린샷 생성 프롬프트 스크립트

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

### Optional: Part 2 Screenshot Generation (3분)
- Part 2 스크린샷 생성 실습
- MCP 프로토콜 및 SpecKit 페이지 캡처
- 체크리스트 업데이트

## 📸 Cline Screenshot Automation

### Part 1 스크린샷 생성 실습 (5분)

**목표**: MCP 서버를 사용하여 Part 1에 필요한 3개 웹페이지 스크린샷 자동 생성

**Step 1**: 디렉토리 구조 확인 (30초)
- `v13.0_resources/images/part1/` 폴더 구조 확인
- 카테고리별 하위 폴더 존재 확인

**Step 2**: 프롬프트 스크립트 열기 (30초)
- `part1-screenshot-generation-prompts.md` 파일 열기
- 3개 프롬프트 확인

**Step 3**: Cline에서 스크린샷 생성 (3분)
- 각 프롬프트를 Cline 대화창에 입력
- MCP 서버가 스크린샷 생성하는 과정 관찰
- 생성된 파일 확인

**Step 4**: 결과 검증 (1분)
- 3개 PNG 파일이 올바른 경로에 생성되었는지 확인
- 이미지 미리보기로 품질 확인
- `11_screenshot_descriptions.md`의 체크리스트 업데이트

### Part 2 스크린샷 생성 실습 (3분)

**목표**: MCP 서버를 사용하여 Part 2에 필요한 2개 웹페이지 스크린샷 자동 생성

**Step 1**: 디렉토리 구조 확인 (30초)
- `v13.0_resources/part2/images/` 폴더 생성 확인
- Part 1 패턴과 동일한 구조 유지

**Step 2**: 프롬프트 스크립트 열기 (30초)
- `part2-screenshot-generation-prompts.md` 파일 열기
- 2개 프롬프트 확인 (MCP 프로토콜, SpecKit)

**Step 3**: Cline에서 스크린샷 생성 (1.5분)
- 각 프롬프트를 Cline 대화창에 입력
- MCP 서버가 스크린샷 생성하는 과정 관찰
- 생성된 파일 확인

**Step 4**: 결과 검증 (30초)
- 2개 PNG 파일이 올바른 경로에 생성되었는지 확인
- 이미지 미리보기로 품질 확인
- `12_screenshot_descriptions.md`의 체크리스트 업데이트

### 사전 준비 (Optional)
**Cline MCP 설정 파일 경로 (macOS)**:
```
~/Library/Application Support/Code/User/globalStorage/saoudrizwan.cline/cline_mcp_settings.json
```

### 단계별 흐름
1. **Node.js 버전 확인**: Node.js 20+ 설치 상태 확인 (`node --version`)
2. **설정 파일 편집**: 위 경로의 `cline_mcp_settings.json`에 webpageScreenshot 서버 추가
3. **Cline 재시작**: VS Code 재시작으로 설정 적용
4. **서버 Reload**: Cline 패널에서 MCP Servers 탭 확인
5. **테스트 실행**: 기본/고급 프롬프트로 스크린샷 생성 확인

### 관련 파일
- [설치 가이드](cline-screenshot-mcp-setup.md)
- [설정 예시](cline-mcp-config-example.json)
- [테스트 프롬프트](screenshot-test-prompts.md)
- [Part 1 프롬프트](part1-screenshot-generation-prompts.md)

## 💡 Key Messages

- "MCP 설치는 생각보다 간단합니다"
- "JSON 파일 하나만 편집하면 됩니다"
- "Cline에서도 MCP 스크린샷 자동화가 가능합니다"
- "MCP 자동화로 웹페이지 스크린샷을 몇 분 만에 생성할 수 있습니다"
- "Part 1과 Part 2에서 총 5개 웹페이지 스크린샷을 MCP 자동화로 완료"
- "수동 캡처 대비 시간 절약: 5개 스크린샷 약 25분 → 5분"
- "설치 어려우면 대안 도구를 사용하세요"
- "도구가 아닌 원칙이 중요합니다"

## 🚨 Backup Plan

**Claude Desktop 없음**: 스크린샷으로 설명, "설치는 자료 참고"

**MCP 연결 실패**: 미리 준비한 응답 파일 사용, "기술적 문제"

**Cline MCP 실패**: 수동 스크린샷 캡처로 대체, "자동화는 선택사항"

**MCP 자동화 실패**: 수동 캡처 가이드 참조 (`11_screenshot_descriptions.md`의 "캡처 가이드라인" 섹션)

**시간 부족**: Step 1-2만 시연, 나머지는 자료 참고 안내

## 🔄 Alternatives Mentioned

**필수 언급** (중요):
- ChatGPT Custom GPTs
- Claude Projects (MCP 없이)
- Notion AI
- "도구가 아닌 원칙이 중요합니다"

## 🔗 Connection to Part 1

Part 1 문서에서 사용할 스크린샷 생성:
- GitHub Education Pack 페이지 (Section 2.2)
- Copilot Plans 비교 (Resource 01, 06)
- VS Code 다운로드 페이지 (Section 2.3)

**관련 리소스**:
- `v13.0_resources/11_screenshot_descriptions.md`: 전체 스크린샷 목록
- `part1-screenshot-generation-prompts.md`: 생성 프롬프트

## 🔗 Connection to Part 2

Part 2 문서에서 사용할 스크린샷 생성:
- MCP 프로토콜 소개 페이지 (Section 3.1 MCP 개념 설명)
- SpecKit 리포지토리 (Section 3.3 SpecKit 소개)

**관련 리소스**:
- `v13.0_resources/part2/12_screenshot_descriptions.md`: Part 2 스크린샷 요구사항
- `part2-screenshot-generation-prompts.md`: 생성 프롬프트
- `v13.0_resources/part2/15_mcp_installation_guide.md`: MCP 설치 가이드
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
