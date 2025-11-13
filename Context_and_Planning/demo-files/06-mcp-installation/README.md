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
- `part3-screenshot-generation-prompts.md`: Part 3 연구 도구 웹페이지 스크린샷 생성 프롬프트 스크립트 (8개)
- `../manual-screenshot-guide.md`: 수동 스크린샷 캡처 가이드 (MCP 자동화 불가능한 데스크톱 애플리케이션)

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

## 📸 Cline Screenshot Automation

### Part 1 스크린샷 생성 실습 (5분)

**목표**: MCP 서버를 사용하여 Part 1에 필요한 3개 웹페이지 스크린샷 자동 생성

**Step 1**: 디렉토리 구조 확인 (30초)

    - `v13.0_resources/part1/images/` 폴더 구조 확인
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
    - 2개 프롬프트 확인

**Step 3**: Cline에서 스크린샷 생성 (1.5분)

    - 각 프롬프트를 Cline 대화창에 입력
    - MCP 서버가 스크린샷 생성하는 과정 관찰
    - 생성된 파일 확인

**Step 4**: 결과 검증 (30초)

    - 2개 PNG 파일이 올바른 경로에 생성되었는지 확인
    - 이미지 미리보기로 품질 확인
    - `12_screenshot_descriptions.md`의 체크리스트 업데이트

### Part 3 스크린샷 생성 실습 (10분)

**목표**: MCP 서버를 사용하여 Part 3에 필요한 8개 연구 도구 웹페이지 스크린샷 자동 생성 준비

**Step 1**: 디렉토리 구조 확인 (30초)
- `v13.0_resources/part3/images/tools-ecosystem/` 폴더 생성 확인
- Part 1/Part 2 패턴과 동일한 구조 유지

**Step 2**: 프롬프트 스크립트 열기 (30초)
- `part3-screenshot-generation-prompts.md` 파일 열기
- 8개 연구 도구 프롬프트 확인 (Elicit, Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar)
- 배치 프롬프트 옵션 확인 (권장)

**Step 3**: Cline에서 배치 스크린샷 생성 준비 (8분)
- 배치 프롬프트를 Cline 대화창에 입력할 준비
- MCP 서버가 8개 스크린샷을 순차적으로 생성하는 과정 관찰 준비
- 각 도구별 로딩 시간 차이 확인 예정 (일부 도구는 느릴 수 있음)
- 생성될 파일 확인 예정

**Step 4**: 결과 검증 준비 (1분)
- 8개 PNG 파일이 올바른 경로에 생성될 예정 확인
- 이미지 미리보기로 품질 확인 예정 (각 도구의 핵심 기능이 보이는지)
- `24-37_screenshot_descriptions.md`의 체크리스트 업데이트 예정
- `screenshots-checklist.md`의 진행 상황 업데이트 예정

**주의사항**:
- 일부 도구(NotebookLM)는 Google 쿠키 배너가 나타날 수 있음
- 로딩 시간이 긴 도구는 타임아웃 가능성 있음 (재시도 필요)
- 로그인이 필요한 페이지는 메인 랜딩 페이지만 캡처됨

### 사전 준비 (Optional)

**Cline MCP 설정 파일 경로 (macOS)**:

```bash
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
- [Part 2 프롬프트](part2-screenshot-generation-prompts.md)
- [Part 3 프롬프트](part3-screenshot-generation-prompts.md)

## 📸 Manual Screenshot Capture

### 목적

MCP 자동화로 생성할 수 없는 데스크톱 애플리케이션 스크린샷을 수동으로 캡처하는 방법을 안내합니다.

### 대상 스크린샷

- **VS Code 실행 화면**: Extensions 마켓플레이스, Copilot 활성화 상태, 폴더 구조
- **Terminal 명령어 결과**: Node.js 설치 확인, MCP 서버 설치 과정
- **Claude Desktop 설정**: MCP 서버 설정 화면, JSON 설정 파일
- **Copilot 기능 시연**: Inline completion, Chat 패널, Agent mode

### macOS 스크린샷 도구

- **기본 단축키**: `Cmd + Shift + 4` (영역 선택), `Cmd + Shift + 5` (고급 옵션)
- **편집 도구**: Preview Markup, Skitch, Snagit
- **품질 요구사항**: 1920x1080 이상, PNG 포맷, 2MB 이하

### 가이드 문서

상세한 단계별 가이드는 [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md) 참조

## 💡 Key Messages

- "MCP 설치는 생각보다 간단합니다"
- "JSON 파일 하나만 편집하면 됩니다"
- "Cline에서도 MCP 스크린샷 자동화가 가능합니다"
- "MCP 자동화로 웹페이지 스크린샷을 몇 분 만에 생성할 수 있습니다"
- "MCP 자동화는 웹페이지만 가능, 데스크톱 애플리케이션은 수동 캡처 필요"
- "수동 캡처 가이드로 일관된 품질의 스크린샷 생성 가능"
- "macOS 스크린샷 도구 마스터하면 캡처 시간 대폭 단축"
- "✅ 현재 진행: Part 1-3 총 4개 완료 (11개 대기)"
    - **MCP 자동화**: 4/15 (26.7%)
    - **Part 3**: 1/8 완료, 7개 배치 실행 필요
    - **⚠️ Part 1**: 2개 재실행 필요 (copilot-plans-comparison.png, vscode-download-page.png)
- "✅ 전체 진행률: 27/61 (44.3%)"
    - MCP 4/15, 수동 23/46
    - Part 1: 13/26 (50%), Part 2: 6/15 (40%), Part 3: 8/20 (40%)
- "시간 절약: MCP 4개 약 4분 (수동 대비 20분 → 4분)"
- "설치 어려우면 대안 도구를 사용하세요"
- "도구가 아닌 원칙이 중요합니다"

## 🚨 Backup Plan

### MCP 자동화 실패 시

**웹페이지 스크린샷**:
- Chrome DevTools 사용: `Cmd + Shift + P` → "Capture screenshot"
- 또는 macOS 기본 도구로 브라우저 윈도우 캡처

**데스크톱 애플리케이션 스크린샷**:
- [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md) 참조
- macOS 스크린샷 도구 (`Cmd + Shift + 4`) 사용
- 단계별 캡처 가이드 및 품질 체크리스트 제공

### Part 1 미생성 파일 (2개)

- **copilot-plans-comparison.png**
    - URL: <https://github.com/features/copilot/plans>
    - 수동 방법: Chrome DevTools (Cmd+Shift+P → Screenshot) 또는 macOS (Cmd+Shift+4)
    - 저장 위치: `v13.0_resources/part1/images/github-education/`
- **vscode-download-page.png**
    - URL: <https://code.visualstudio.com/>
    - 수동 방법: Chrome DevTools 또는 macOS 스크린샷
    - 저장 위치: `v13.0_resources/part1/images/vscode-setup/`

### Part 3 MCP 배치 대기 (7개)

- Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar
- 저장 위치: `v13.0_resources/part3/images/tools-ecosystem/`
- 파일명 규칙: kebab-case (예: `perplexity-main.png`)

### 일반 MCP 실패 시

**Claude Desktop 없음**: 스크린샷으로 설명, "설치는 자료 참고"

**MCP 연결 실패**: 미리 준비한 응답 파일 사용, "기술적 문제"

**Cline MCP 실패**: 수동 스크린샷 캡처로 대체, "자동화는 선택사항"

---

## 📊 현재 상태 (2025-11-13)

### 전체 진행률

- **총 61개**: 27/61 완료 (44.3%)
- **MCP 자동화**: 4/15 (26.7%)
- **수동 캡처**: 23/46 (50%)

### 파트별 상세

- **Part 1**: 13/26 완료 (50%)
    - MCP: 1/3 (⚠️ 2개 재실행 필요)
    - 수동: 12/23
- **Part 2**: 6/15 완료 (40%)
    - MCP: 2/2 (✅ 완료)
    - 수동: 4/13
- **Part 3**: 8/20 완료 (40%)
    - MCP: 1/8 (🚧 7개 배치 실행 필요)
    - 수동: 7/12 (다이어그램/폴더 구조)

### 다음 작업 우선순위

1. 🔴 **Part 1 MCP 재실행** (2개, ~2분)
2. 🔴 **Part 3 MCP 배치** (7개, ~7분)
3. **Part 1 수동 캡처** (11개, 30-40분)
4. **Part 2 수동 캡처** (9개, 20-30분)
5. **Part 3 수동 캡처** (12개, 40-60분)

**참고**: 상세 체크리스트는 `screenshots-checklist.md` 참조

---

## 🔄 Alternatives Mentioned

**필수 언급** (중요):

    - ChatGPT Custom GPTs
    - Claude Projects (MCP 없이)
    - Notion AI
    - "도구가 아닌 원칙이 중요합니다"

## 🔗 Connection to Parts

### Part 1

- **MCP 자동화**: 3개 (GitHub Education Pack, Copilot Plans, VS Code 다운로드)
- **수동 캡처**: 23개 (VS Code 실행 화면, Copilot 기능 시연, 실습 예시)
- **가이드**: [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.1

**관련 리소스**:

    - `v13.0_resources/11_screenshot_descriptions.md`: 전체 스크린샷 목록
    - `part1-screenshot-generation-prompts.md`: 생성 프롬프트

### Part 2

- **MCP 자동화**: 2개 (MCP 프로토콜, SpecKit 리포지토리)
- **수동 캡처**: 13개 (MCP 설치 과정, SpecKit 워크플로우, Copilot 워크북)
- **가이드**: [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.2

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

### Part 3

- **MCP 자동화**: 8개 (연구 도구 생태계)
  - Elicit, Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar
- **수동 캡처**: 12개 (통합 워크플로우, 전공별 시나리오)
- **가이드**: [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.3

**관련 리소스**:

- `v13.0_resources/part3/24-37_screenshot_descriptions.md`: Part 3 스크린샷 요구사항
- `part3-screenshot-generation-prompts.md`: 생성 프롬프트
- `screenshots-checklist.md`: 전체 진행 상황 (27/61 완료)

## 🕐 Time Breakdown

### MCP Automation Time

- Part 1 Screenshot Generation: 5분
- Part 2 Screenshot Generation: 3분
- Part 3 Screenshot Generation: ⏳ [Pending File Generation] (10분 예상)
- **Total MCP Automation**: 18분

### Manual Capture Time

- **Part 1**: 12/23 완료 (약 1-2시간), 11개 대기 (약 30-40분)
- **Part 2**: 4/13 완료 (약 30분), 9개 대기 (약 20-30분)
- **Part 3**: 7/12 완료 (약 1시간), 5개 대기 (약 20-30분)
- **Total Manual**: 2-3시간 완료, 1-2시간 대기 (총 3-5시간 예상)

### Time Savings with Guide

- **사전 준비 및 품질 체크**로 재작업 최소화
- **단계별 가이드**로 초보자도 빠른 캡처
- **예상 시간 절약**: 약 30-50%
- **참고**: [`../manual-screenshot-guide.md`](../manual-screenshot-guide.md)

### Demonstration Flow Options

**Option 1: MCP Installation Only (5분)**
- Claude Desktop MCP 설치 시연만 진행
- 스크린샷 자동화는 자료로 제공

**Option 2: Installation + Part 1 Screenshots (10분)**
- MCP 설치 + Part 1 스크린샷 생성 실습
- Part 2-3는 자료로 제공

**Option 3: Complete Automation Demo (23분)**
- MCP 설치 + Part 1-3 전체 스크린샷 자동화
- 전체 워크플로우 시연
