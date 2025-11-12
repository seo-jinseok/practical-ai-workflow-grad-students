# MCP (Model Context Protocol) 설치 및 실용 가이드

**Version**: v13.0 Part 2  
**Date**: 2025-11-10  
**Target**: 대학원생 (코딩 지식 불필요, Part 1 완료)  
**Related**: [메인 Part 2 문서](../Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md) | [Part 2 리소스 인덱스](README_v13_Part2.md)

---

## 🎯 가이드 개요

### 📋 전체 목표
MCP (Model Context Protocol)를 연구 워크플로우에 통합하여 **AI와 외부 도구들을 원클릭으로 연결**하는 방법을 배우는 실용적 가이드입니다. 초보자도 쉽게 따라할 수 있도록 단계별 설치부터 실전 활용까지 완전 커버합니다.

### ⏰ 예상 소요 시간: 1-2시간
- **MCP 설치 및 기본 설정**: 30분
- **task-master-mcp 실습**: 20분
- **연구자용 서버 설치**: 30-60분 (선택적)

### 🎓 필요 사전 지식
- Part 1 완료 (AI 기본 사용법)
- VS Code 또는 터미널 기본 사용법
- Claude Desktop 또는 AI 도구 계정

### 📁 준비물
```
📁 사전 준비물
├── 💻 macOS 또는 Windows 컴퓨터
├── 🌐 인터넷 연결 (안정적)
├── 📝 Claude Desktop 계정 (추천) 또는 AI 도구
└── 📁 새 프로젝트 폴더 생성: `mcp-research/`
```

---

## 🔧 Part 1: MCP 설치 및 기본 설정

### 🤔 MCP란? (간단한 설명)

MCP는 **"AI와 외부 도구들을 연결하는 USB-C 같은 표준"**입니다. 

**비유해서 이해하기**:
- **기존 방식**: 각각의 도구를 별도로 사용 (문서용 도구, 데이터용 도구, 검색용 도구 등)
- **MCP 방식**: AI 하나에서 모든 도구를 동시에 사용 (USB-C 허브에 여러 기기 연결하듯)

**연구 예시**:
```
기존: 
1. 브라우저에서 논문 검색 → 2. Zotero에 저장 → 3. 노트에 정리 → 4. AI에게 분석 요청

MCP:
1. AI에게 "논문 검색해서 분석해줘" → AI가 모든 도구 자동 연동 → 완료
```

### 🏗️ MCP 아키텍처 이해

```
┌─────────────────────────────────────────┐
│              AI (Claude)                   │
│                                             │
│  ┌──────────────┐  ┌──────────────┐  │
│  │  연구자용 MCP  │  │  프로젝트 MCP  │  │
│  │     서버들       │  │     서버들       │  │
│  └──────┬───────┘  └──────┬───────┘  │
│         │                │                │
└─────────┼────────────────┼────────────────┘
          │                │
    ┌─────▼──────┐  ┌─────▼──────┐
    │ arxiv,    │  │ task-master,│
    │ zotero,   │  │ notion,     │
    │ notion,   │  │ jupyter     │
    │ jupyter   │  │ ...         │
    └───────────┘  └─────────────┘
```

### 🖥️ Claude Desktop 설치 (방법 1: Homebrew - macOS)

#### ✅ 장점
- **자동 업데이트**: Homebrew가 최신 버전 유지
- **간편한 설치**: 터미널 한 줄로 완료
- **의존성 관리**: 필요한 라이브러리 자동 설치

#### 📋 설치 단계

**Step 1: Homebrew 확인 및 설치** (5분)

1. **터미널 열기**:
   - Spotlight 검색 (Cmd + Space) → "터미널" 입력
   - 또는 Applications > Utilities > Terminal

2. **Homebrew 설치 여부 확인**:
```bash
brew --version
```

3. **설치되어 있지 않을 경우**:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2: Claude Desktop 설치** (5분)

1. **설치 명령어 실행**:
```bash
brew install --cask claude
```

2. **설치 완료 확인**:
   - Applications 폴더에서 "Claude" 아이콘 확인
   - 또는 터미널에서: `ls /Applications | grep Claude`

**Step 3: 첫 실행 및 설정** (10분)

1. **Claude Desktop 실행**:
   - Applications 폴더에서 더블클릭
   - 또는 터미널에서: `open -a "Claude"`

2. **로그인**:
   - 기존 Claude 계정으로 로그인
   - 계정이 없으면 무료 계정 생성

3. **기본 설정 확인**:
   - 새 대화 생성 가능 확인
   - AI 응답 정상 작동 확인

### 🖥️ Claude Desktop 설치 (방법 2: 직접 다운로드)

#### ✅ 장점
- **공식 다운로드**: 가장 안정적인 버전
- **명확한 파일 위치**: 다운로드한 파일 관리 용이
- **모든 OS 지원**: Windows도 지원

#### 📋 설치 단계 (macOS)

**Step 1: 공식 사이트에서 다운로드**

1. **브라우저에서 접속**: https://claude.ai/download

2. **버전 선택**:
   - **Intel Mac**: "Download for Intel" 클릭
   - **Apple Silicon (M1/M2/M3)**: "Download for Apple Silicon" 클릭

3. **파일 다운로드**:
   - `Claude.dmg` 파일이 다운로드됩니다
   - 다운로드 완료까지 잠시 대기

**Step 2: 설치 및 실행**

1. **DMG 파일 마운트**:
   - 다운로드한 `Claude.dmg` 파일을 더블클릭
   - "클라우드" 애플리케이션을 Applications 폴더로 드래그

2. **첫 실행**:
   - Applications 폴더에서 "클라우드" 실행
   - macOS가 "검증되지 않은 개발자" 경고할 경우:
     - 시스템 환경설정 > 보안 및 개인정보보호 > 일반
     - "어쨌든 허용" 클릭

#### 📋 설치 단계 (Windows)

**Step 1: 다운로드 및 설치**

1. **공식 사이트에서 Windows 버전 다운로드**
2. **MSI 파일 실행** 및 설치 마법사 완료
3. **시작 메뉴에서 "Claude" 실행**

### ⚙️ MCP 환경 설정

#### 🔧 설정 파일 위치 찾기

**macOS**:
```bash
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Windows**:
```
%APPDATA%\Claude\claude_desktop_config.json
```

#### 📝 기본 설정 파일 생성

**Step 1: 설정 파일 편집기 열기** (5분)

**VS Code 사용 (권장)**:
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**또는 텍스트 에디터**:
```bash
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Step 2: 기본 MCP 설정 추가** (5분)

아래 내용을 설정 파일에 복사하여 추가:

```json
{
  "mcpServers": {
    "test-connection": {
      "command": "echo",
      "args": ["Hello, MCP is working!"]
    }
  }
}
```

**Step 3: 설정 확인** (5분)

1. **Claude Desktop 재시작**:
   - 앱 완전 종료 (Cmd+Q)
   - 5초 후 다시 실행

2. **새 대화에서 테스트**:
   ```
   "MCP 연결이 정상 작동하나요?"
   ```

3. **정상 응답 예시**:
   ```
   "네, MCP 연결이 정상적으로 작동하고 있습니다. 
   AI가 외부 도구들과 통신할 수 있는 준비가 완료되었습니다."
   ```

---

## 🧪 Part 2: task-master-mcp 실습 (20분)

### 🎯 task-master-mcp란?

**task-master-mcp**는 **AI가 연구 프로젝트 관리 전문가 역할**을 수행하는 도구입니다. 단순한 Chatbot이 아니라, 실제 프로젝트 관리의 전문성을 가진 AI 어시스턴트입니다.

#### 🔍 주요 기능
- **프로젝트 분석**: 현재 상황을 객관적으로 평가
- **작업 분해**: 큰 과제를 관리 가능한 세부 작업으로 나누기
- **우선순위 설정**: 무엇을 먼저 해야 하는지 제안
- **진행 추적**: 목표 대비 현재 진행 상황 모니터링
- **리스크 관리**: 잠재적 문제점 사전 식별 및 대응 방안 제안

### 🏃‍♀️ 실습 개요 (총 20분)

```
📋 task-master-mcp 실습 (20분)
├── 실습 1: 프로젝트 초기화 (5분)
├── 실습 2: 작업 세부 분해 (5분)
├── 실습 3: 진행 상황 업데이트 (5분)
└── 실습 4: 통합 워크플로우 (5분)
```

### 📋 실습 준비

#### ✅ 사전 준비물
- [ ] **MCP 설치 완료** (Part 1 참조)
- [ ] **Claude Desktop 실행** 및 새 대화 생성
- [ ] **연구 주제 선정** (예: 석사논문, 학술지 논문, 연구계획서 등)

#### 💡 예시 연구 프로젝트
실습 편의를 위해 다음 예시 프로젝트를 사용합니다:
```
연구 주제: "온라인 학습 참여도 향상 방안에 관한 연구"
연구 형태: 석사학위논문 (1학기 완성 목표)
현재 상황: 연구 주제만 결정된 상태
완료해야 할 작업: 문헌 조사, 연구 설계, IRB 승인, 실험實施, 분석, 논문 작성
```

### 🏃‍♀️ 실습 1: 프로젝트 초기화 (5분)

#### 🎯 목표
AI가 연구 프로젝트를 분석하고 현재 상황 파악, 다음 우선순위 작업 3개 제안

#### 📝 프롬프트 (복사하여 사용)
```
다음 연구 프로젝트에 대해 분석하고 현재 상황을 파악한 후, 
다음 우선순위 작업 3개를 구체적으로 제안해 주세요.

프로젝트 정보:
- 연구 주제: 온라인 학습 참여도 향상 방안에 관한 연구
- 연구 형태: 석사학위논문
- 완성 목표: 1학기 (4개월)
- 현재 상황: 연구 주제만 결정된 상태
- 연구 방법: 준실험설계 (실험집단 vs 통제집단)
- 예상 참여자: 대학생 150명
```

#### 🔍 예상 AI 응답 예시
```
**프로젝트 분석 결과:**

**현재 진행 상황**: 5% (연구 주제 확정만 완료)
**요구 작업 총량**: 15개 주요 작업, 45개 세부 작업
**예상 소요 시간**: 16주
**위험 요소**: IRB 승인 지연, 참여자 모집 어려움

**다음 우선순위 작업:**

1. ** Literature Review 및 연구 설계 (1-2주)**
   - 관련 논문 20-30편 수집 및 분석
   - 연구 가설 및 방법론 구체화
   - 연구 도구(설문지, 인터뷰 가이드) 개발

2. **IRB 승인 준비 (2-3주)**
   - 연구 계획서 IRB 양식에 맞게 작성
   - 동의서 및 정보 제공서 작성
   - IRB 위원회 검토 및 승인

3. **자료 수집 계획 수립 (1주)**
   - 참여자 모집 전략 수립
   - 실험 및 통제집단 배치 계획
   - 자료 수집 일정 및 절차 확정
```

### 🏃‍♀️ 실습 2: 작업 세부 분해 (5분)

#### 🎯 목표
선택한 작업을 더 세부적인 단계로 분해하여 실행 가능한 체크리스트 작성

#### 📝 프롬프트 (실습 1의 결과 활용)
```
실습 1에서 제안한 "Literature Review 및 연구 설계" 작업을 
더 세부적으로 분해해 주세요. 각 하위 작업을 30분-1시간 단위로 나누고, 
완료 기준을 포함해서 체크리스트로 만들어 주세요.
```

#### 🔍 예상 AI 응답 예시
```
**Literature Review 및 연구 설계 작업 분해:**

**1주차: 문헌 조사 (8시간)**
- [ ] 1.1 온라인 학습, 참여도 관련 논문 키워드 최종 확정 (30분)
- [ ] 1.2 Google Scholar, DB에서 논문 검색 (2시간)
- [ ] 1.3 핵심 논문 30편 선정 및 다운로드 (1시간)
- [ ] 1.4 논문 요약 및 주요 이론 정리 (4시간)
- [ ] 1.5 연구 공백 및 해결해야 할 문제 식별 (30분)

**2주차: 연구 설계 (8시간)**
- [ ] 2.1 이론적 프레임워크 구축 (2시간)
- [ ] 2.2 연구 질문 및 가설 구체화 (1시간)
- [ ] 2.3 연구 설계 방법론 확정 (준실험설계) (1시간)
- [ ] 2.4 연구 도구 개발 (설문지) (3시간)
- [ ] 2.5 연구 계획서 작성 (1시간)

**완료 기준:**
- 주요 이론 3개 이상 정리
- 연구 질문 2-3개 명확히 정의
- 설문지 초안 완성
- 5페이지 연구 계획서 완성
```

### 🏃‍♀️ 실습 3: 진행 상황 업데이트 (5분)

#### 🎯 목표
가상 진행 상황을 설정하고 AI의 피드백 및 다음 단계 제안 받기

#### 📝 프롬프트 (실습 2의 결과 활용)
```
실습 2에서 분해한 작업 중 1주차를 완료했다고 가정하고, 
진행 상황을 업데이트해 주세요. 그리고 2주차 작업을 시작하기 전에 
유의해야 할 점과 다음 단계를 제안해 주세요.

현재 완료 상황:
- 1주차 작업 100% 완료
- 주요 이론 3개 정리 완료 (이해 중심성, 자기조절학습, 게이미피케이션)
- 연구 질문 2개 확정
- 30편 논문 분석 완료
```

#### 🔍 예상 AI 응답 예시
```
**진행 상황 업데이트:**

**완료된 작업 (100%)**
✅ 문헌 조사 및 이론 정리
✅ 연구 질문 및 가설 확정
✅ 핵심 개념 및 변수 정의

**현재 상태**: 15% 완료 (1주/16주)

**2주차 시작 전 유의사항:**

1. **IRB 승인 연계성 확인**
   - 현재까지의 연구 계획이 IRB 요구사항과 부합하는지 확인
   - 특히 연구 참여자 보호 방안 검토

2. **연구 도구 검증**
   - 완성된 설문지의 신뢰도 및 타당도 점검
   - 선행 연구에서 사용된 검증된 도구 참고

**다음 단계 (2주차) 우선순위:**

1. **IRB 승인 자료 준비** (가장 중요)
   - 연구 계획서 IRB 양식에 맞게 재작성
   - 동의서 및 정보 제공서 작성

2. **실험 설계 구체화**
   - 실험집단/통제집단 구체적 배치 방법
   - 중재(게이미피케이션 요소) 구체적 설계

**리스크 경고**: IRB 승인 지연 시 전체 일정이 2-3주 지연될 수 있음
```

### 🏃‍♀️ 실습 4: 통합 워크플로우 (5분)

#### 🎯 목표
전체 연구 과정을 한 번에 AI와 함께 설계하고 관리 방법 습득

#### 📝 프롬프트 (모든 실습 결과 통합)
```
지금까지의 분석을 바탕으로, 전체 16주 연구 과정을 
한눈에 볼 수 있는 마일스톤 달력를 만들어 주세요. 
각 마일스톤마다 핵심 성과물과 완료 기준을 포함해서 
최종 연구 로드맵을 제시해 주세요.
```

#### 🔍 예상 AI 응답 예시
```
**온라인 학습 참여도 연구 - 16주 마일스톤 달력**

**Phase 1: 연구 설계 (1-4주)**
- Week 1: 문헌 조사 완료 ✅
- Week 2: 연구 설계 및 IRB 준비
- Week 3: IRB 승인 신청
- Week 4: 연구 도구 최종 확정

**Phase 2: 예비 연구 (5-6주)**
- Week 5: 파일럿 연구 (20명)
- Week 6: 도구 검증 및 수정

**Phase 3: 본 연구 (7-12주)**
- Week 7-8: 실험집단 중재 적용
- Week 9-10: 데이터 수집 (150명)
- Week 11: 데이터 정리 및 검증
- Week 12: 통계 분석 완료

**Phase 4: 결과 정리 (13-16주)**
- Week 13: 결과 해석 및 Discussion
- Week 14: 논문 초안 작성
- Week 15: 지도교수 검토 및 수정
- Week 16: 논문 최종 완성

**핵심 마일스톤**:
- IRB 승인: Week 4 (임계 경로)
- 데이터 수집 완료: Week 10 (예정일)
- 논문 제출: Week 16 (최종 목표)
```

### ✅ 실습 완료 체크리스트

- [ ] **실습 1 완료**: 프로젝트 분석 및 우선순위 설정
- [ ] **실습 2 완료**: 작업 세부 분해 및 체크리스트 작성
- [ ] **실습 3 완료**: 진행 상황 업데이트 및 리스크 관리
- [ ] **실습 4 완료**: 통합 워크플로우 및 마일스톤 설정
- [ ] **내 연구에 적용**: 실제 연구 프로젝트로 task-master-mcp 활용 시작

---

## 🔬 Part 3: 연구자용 MCP 서버 소개

### 🎯 MCP 서버 생태계 개요

MCP 서버는 AI를 다양한 연구 도구와 연결하는 특별한 프로그램들입니다. 각 서버는 특정한 기능을 제공하여, 연구의 특정 영역에서 생산성을 크게 향상시킬 수 있습니다.

#### 📊 주요 연구자용 MCP 서버들

| 서버명 | 주요 기능 | 적용 시나리오 | 난이도 |
|--------|-----------|---------------|--------|
| **arxiv-mcp** | 논문 검색 및 메타데이터 추출 | 문헌 조사, 최신 연구 동향 파악 | ⭐⭐☆☆☆ |
| **zotero-mcp** | 참고문헌 관리 및 검색 | 논문 작성, 인용 관리 | ⭐⭐⭐☆☆ |
| **notion-mcp** | 연구 노트 및 지식 관리 | 연구 진행 상황 추적, 협업 | ⭐⭐☆☆☆ |
| **jupyter-mcp** | 데이터 분석 노트북 통합 | 통계 분석, 시각화, 실험 | ⭐⭐⭐⭐☆ |
| **task-master-mcp** | 프로젝트 관리 및 작업 분해 | 전체 연구 워크플로우 관리 | ⭐⭐☆☆☆ |

### 📚 arxiv-mcp: 논문 검색 자동화

#### 🎯 arxiv-mcp란?

**arxiv-mcp**는 **arXiv.org의 논문 데이터베이스에 직접 접근**하여 AI가 논문을 검색하고 분석할 수 있게 하는 서버입니다. 수동으로 논문을 찾고 정리하는 수고로움을 대폭 줄여줍니다.

#### ⚙️ 설치 및 설정

**Step 1: MCP 설정에 추가** (3분)

1. **설정 파일 열기**:
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. **arxiv-mcp 서버 추가**:
```json
{
  "mcpServers": {
    "arxiv": {
      "command": "npx",
      "args": ["-y", "@blazickjp/arxiv-mcp-server"]
    }
  }
}
```

3. **설정 파일 저장** 및 **Claude Desktop 재시작**

**Step 2: 테스트** (2분)

새 대화에서 테스트:
```
"arxiv에서 'machine learning education' 관련 최근 논문 5편을 찾아주세요."
```

**예상 응답**:
```
arXiv에서 'machine learning education' 관련 최근 논문을 찾았습니다:

1. **"Large Language Models for Educational Assessment"** (2024)
   - 저자: Smith, J. et al.
   - 요약: LLM을 활용한 교육 평가 방법론 제안
   
2. **"Interactive Learning with AI Tutors"** (2024)
   - 저자: Johnson, M. et al.
   - 요약: AI 튜터 시스템의 학습 효과성 검증
   
...[나머지 3편]
```

#### 📖 zotero-mcp: 참고문헌 관리 통합

##### 🎯 zotero-mcp란?

**Zotero**는 세계적인 참고문헌 관리 프로그램입니다. **zotero-mcp**는 이 Zotero 라이브러리에 AI가 직접 접근하여 논문 정보를 검색하고 관리할 수 있게 합니다.

##### ⚙️ 설치 및 설정

**Step 1: Zotero 설치** (선택적, 이미 설치된 경우 생략)

**macOS**:
```bash
brew install --cask zotero
```

**Windows**: 공식 사이트에서 다운로드 후 설치

**Step 2: Zotero MCP 연결** (5분)

1. **Zotero에서 API 키 생성**:
   - Zotero 실행 > Edit > Preferences > Advanced > Config Editor
   - `extensions.zotero.httpServer.enabled`를 `true`로 설정

2. **MCP 설정 파일에 추가**:
```json
{
  "mcpServers": {
    "zotero": {
      "command": "npx",
      "args": ["-y", "zotero-mcp"],
      "env": {
        "ZOTERO_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Step 3: API 키 설정** (3분)

1. **Zotero 웹사이트에서 API 키 생성**:
   - https://www.zotero.org/settings/keys/new
   - personal library 접근 권한 부여

2. **API 키를 설정 파일에 입력**:
```json
"env": {
  "ZOTERO_API_KEY": "실제-API-키-입력"
}
```

### 🗃️ notion-mcp: 연구 노트 통합

#### 🎯 notion-mcp란?

**Notion**은 연구 노트, 아이디어, 그리고 연구 진행 상황을 체계적으로 관리할 수 있는 플랫폼입니다. **notion-mcp**는 AI가 이 Notion 데이터베이스에 직접 접근하여 연구 노트를 검색, 작성, 업데이트할 수 있게 합니다.

#### ⚙️ 설치 및 설정

**Step 1: Notion API 설정** (5분)

1. **Notion Integration 생성**:
   - https://www.notion.so/my-integrations 접속
   - "New integration" 클릭
   - 이름: "Research MCP Integration"
   - Capabilities: "Read content", "Update content", "Insert content"

2. **Integration 토큰 복사**

**Step 2: Notion 페이지에 연결** (3분)

1. **연구 노트 페이지에서 공유 설정**:
   - 연구 노트 페이지에서 "Share" 클릭
   - "Add connections"에서 방금 생성한 Integration 추가

**Step 3: MCP 설정** (2분)

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@suekou/mcp-notion-server"],
      "env": {
        "NOTION_API_KEY": "your-notion-integration-token"
      }
    }
  }
}
```

**Step 4: 테스트** (3분)

```
"Notion에서 '연구 아이디어' 데이터베이스의 최근 노트 3개를 보여주세요."
```

---

## 🎓 Part 4: 전공별 MCP 조합 추천

### 🎯 전공별 연구 특성과 요구사항

각 학문 분야는 고유한 연구 방법론, 도구, 그리고 워크플로우를 가집니다. 적절한 MCP 서버 조합을 선택하면 연구 생산성을 크게 향상시킬 수 있습니다.

#### 📊 전공별 연구 특징 비교

| 전공 | 주요 연구 방법 | 핵심 도구 | 데이터 유형 | 주요 저널 |
|------|----------------|-----------|-------------|-----------|
| **인문학** | 텍스트 분석, 비평, 비교 연구 | 텍스트 에디터, 인문학 DB | 텍스트, 이미지, 음원 | 인문저널 |
| **사회과학** | 설문 조사, 인터뷰, 관찰 | SPSS, NVivo, 조사 플랫폼 | 수치, 텍스트, 오디오 | SSCI 저널 |
| **자연과학** | 실험, 관측, 시뮬레이션 | 실험 장비, 분석 소프트웨어 | 센서 데이터, 이미지 | SCI 저널 |
| **공학** | 시스템 개발, 성능 평가 | 개발 도구, 시뮬레이션 | 로그, 성능 메트릭 | IEEE, ACM |

### 📚 인문학 연구자를 위한 MCP 조합

#### 🎭 추천 서버 조합
```json
{
  "mcpServers": {
    "notion-mcp": {
      "command": "npx",
      "args": ["-y", "@suekou/mcp-notion-server"]
    },
    "zotero-mcp": {
      "command": "npx", 
      "args": ["-y", "zotero-mcp"]
    },
    "task-master-mcp": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

**선택 이유**:
- **notion-mcp**: 텍스트 정리, 노트 관리에 최적
- **zotero-mcp**: 인문 저널 논문 관리 및 인용
- **task-master-mcp**: 창작적 연구 프로세스 관리

#### 📖 실제 활용 예시

**연구 시나리오**: "한국 현대문학의 디지털화 연구"

```
AI에게 요청: 
"현대문학 디지털화 관련 최근 논문 10편을 arxiv와 Zotero에서 찾아서, 
Notion의 '文学研究' 데이터베이스에 정리해주세요. 
각 논문마다 주요 주장과 연구 방법을 요약해주세요."

AI가 자동 수행:
1. arxiv-mcp로 논문 검색
2. zotero-mcp로 참고문헌 관리
3. notion-mcp로 연구 노트 자동 정리
```

### 🏛️ 사회과학 연구자를 위한 MCP 조합

#### 🎓 추천 서버 조합
```json
{
  "mcpServers": {
    "task-master-mcp": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    },
    "zotero-mcp": {
      "command": "npx",
      "args": ["-y", "zotero-mcp"]
    },
    "jupyter-mcp": {
      "command": "npx",
      "args": ["-y", "jupyter-mcp"]
    }
  }
}
```

**선택 이유**:
- **task-master-mcp**: 대규모 설문 조사 프로젝트 관리
- **zotero-mcp**: SSCI 저널 논문 관리 필수
- **jupyter-mcp**: 통계 분석 및 데이터 시각화

#### 📊 실제 활용 예시

**연구 시나리오**: "대학생의心理健康과 온라인 학습의 상관관계 연구"

```
AI에게 요청:
"心理学와 온라인 학습 관련 SSCI 논문 20편을 찾아서 Zotero에 추가하고,
설문 데이터 분석을 위한 Python 스크립트를 작성해주세요.
相관관계 분석과 그룹 비교 분석을 포함해주세요."

AI가 자동 수행:
1. zotero-mcp로 학술지 논문 관리
2. jupyter-mcp로 통계 분석 코드 자동 생성
3. task-master-mcp로 연구 일정 관리
```

### 🔬 자연과학 연구자를 위한 MCP 조합

#### 🧪 추천 서버 조합
```json
{
  "mcpServers": {
    "jupyter-mcp": {
      "command": "npx",
      "args": ["-y", "jupyter-mcp"]
    },
    "notion-mcp": {
      "command": "npx",
      "args": ["-y", "@suekou/mcp-notion-server"]
    },
    "task-master-mcp": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

**선택 이유**:
- **jupyter-mcp**: 데이터 분석, 시각화, 실험 결과 정리 필수
- **notion-mcp**: 실험 노트, 관측 데이터 기록 관리
- **task-master-mcp**: 장기 연구 프로젝트의 일정 및 리스크 관리

#### 🧪 실제 활용 예시

**연구 시나리오**: "기후변화가 해조류 생물다양성에 미치는 영향"

```
AI에게 요청:
"기후변화와 해양 생물다양성 관련 SCI 논문을 15편 찾아서
Jupyter 노트북에서 메타분석을 수행해주세요.
그리고 실험 설계와 관측 일정도 만들어주세요."

AI가 자동 수행:
1. jupyter-mcp로 메타분석 코드 작성
2. notion-mcp로 실험 노트 및 데이터 관리
3. task-master-mcp로 연구 일정 및 마일스톤 설정
```

### ⚙️ 공학 연구자를 위한 MCP 조합

#### 💻 추천 서버 조합
```json
{
  "mcpServers": {
    "jupyter-mcp": {
      "command": "npx",
      "args": ["-y", "jupyter-mcp"]
    },
    "task-master-mcp": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    },
    "zotero-mcp": {
      "command": "npx",
      "args": ["-y", "zotero-mcp"]
    }
  }
}
```

**선택 이유**:
- **jupyter-mcp**: 알고리즘 개발, 성능 테스트, 실험 구현
- **task-master-mcp**: 시스템 개발, 테스트, 배포 일정 관리
- **zotero-mcp**: IEEE/ACM 논문 관리 및 인용

#### 💻 실제 활용 예시

**연구 시나리오**: "IoT 보안 시스템 개발"

```
AI에게 요청:
"IoT 보안 관련 IEEE 논문을 20편 찾아서 Zotero에 추가하고,
알고리즘 성능 비교를 위한 실험 설계와 Python 코드를 작성해주세요.
개발 일정과 테스트 계획도 포함해서 프로젝트 관리해주세요."

AI가 자동 수행:
1. zotero-mcp로 IEEE 논문 관리
2. jupyter-mcp로 알고리즘 구현 및 성능 분석
3. task-master-mcp로 개발 일정 및 품질 관리
```

---

## 🛠️ Part 5: MCP 트러블슈팅 및 대안

### 🛠️ 일반적인 문제와 해결 방법

MCP를 사용하다 보면 다양한 문제 상황에 직면할 수 있습니다. 자주 발생하는 문제들과 해결 방법을 미리 알아두면从容하게 대응할 수 있습니다.

#### ❌ 문제 1: MCP 서버가 인식되지 않음

**증상**:
```
"task-master-mcp를 사용할 수 있나요?"
"현재 이 도구에 접근할 수 없습니다"
```

**단계별 해결 방법**:

**1단계: 설정 파일 확인** (5분)
- 설정 파일 위치 확인: 
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- JSON 문법 오류 확인 (VS Code에서 빨간 줄)

**2단계: Claude 재시작** (2분)
- Claude Desktop 완전 종료 (Cmd+Q 또는 작업관리자에서 종료)
- 5초 후 다시 실행
- 새 대화에서 다시 테스트

**3단계: 서버별 개별 테스트** (3분)
```json
// 하나씩 추가하여 문제 서버 식별
{
  "mcpServers": {
    "task-master-mcp": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

#### ❌ 문제 2: npm/npx 명령어 오류

**증상**:
```
"command not found: npx"
"npm ERR! code ELOCKVERIFY"
```

**해결 방법**:

**macOS (Homebrew 사용)**:
```bash
# Node.js 및 npm 설치
brew install node

# 설치 확인
node --version
npm --version
npx --version
```

**Windows**:
1. Node.js 공식 사이트에서 LTS 버전 다운로드
2. MSI 파일 실행하여 설치
3. 재부팅 후 확인

#### ❌ 문제 3: 권한 오류 (macOS)

**증상**:
```
"Permission denied"
"cannot create directory"
```

**해결 방법**:
```bash
# npm 전역 설치 권한 문제 해결
sudo chown -R $(whoami) ~/.npm
sudo chown -R $(whoami) /usr/local/lib/node_modules
```

#### ❌ 문제 4: 노드 버전 호환성

**증상**:
```
"Node.js version not supported"
"Engine "node" not compatible"
```

**해결 방법**:
```bash
# nvm (Node Version Manager) 설치 및 사용
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.zshrc

# LTS 버전 설치
nvm install --lts
nvm use --lts

# 현재 버전 확인
node --version
```

### 🌐 대안 도구들 (MCP 설치 어려울 경우)

MCP가 설치되지 않거나 개인 사유로 사용하기 어려운 경우, **대안 도구들**을 활용할 수 있습니다.

#### 🤖 ChatGPT Custom GPTs

**특징**:
- 설치 불필요, 웹에서 바로 사용
- 연구 워크플로우 특화 GPT 생성 가능
- 기초적인 프로젝트 관리 기능

**장점**:
- 즉시 사용 가능
- 다양한 분야 특화 GPT 존재
- 개인 정보 보호 수준 높음

**단점**:
- 외부 도구 연동 제한적
- 무료 버전 사용 시간 제한
- 고급 분석 기능 제한적

#### 🏗️ Claude Projects (MCP 없이)

**특징**:
- Claude의 내장 프로젝트 기능
- 문서 업로드 및 프로젝트 기반 대화
- MCP 없이도 AI와 유기적 협업 가능

**장점**:
- Claude 생태계 내 완벽 통합
- 문서 기반 작업에 최적
- 쉬운 설정 및 사용

**단점**:
- 외부 도구 연동 불가
- 복잡한 데이터 분석 제한적
- 팀 협업 기능 제한적

#### 📊 Notion AI (전문화된 대안)

**특징**:
- Notion 내장 AI 기능
- 연구 노트 작성 및 관리 최적화
- 데이터베이스 연동 가능

**장점**:
- 연구 노트와 AI의 완벽한 통합
- 팀 협업 및 공유 용이
- 다양한 템플릿 제공

**단점**:
- Notion 사용자 한정
- 외부 도구 연동 제한적
- 일부 기능 유료

### 💡 MCP 사용 최적화 팁

#### 🔧 성능 최적화

1. **필요한 서버만 설치**:
   - 처음에는 task-master-mcp만 사용
   - 필요할 때마다 하나씩 추가

2. **정기적 업데이트**:
```bash
# 설치된 MCP 서버 업데이트
npm update -g @blazickjp/arxiv-mcp-server
```

3. **설정 파일 백업**:
   - 설정 파일을 GitHub에 백업
   - 다른 컴퓨터에서 쉽게 복구 가능

#### 🎯 효율성 향상

1. **프롬프트 템플릿 활용**:
   ```markdown
   "다음 [연구 주제]에 대해 [구체적 작업]을 수행해주세요.
   결과는 [원하는 형식]으로 정리해 주세요."
   ```

2. **작업 시퀀스 자동화**:
   ```markdown
   "1단계: 문헌 조사
   2단계: 데이터 분석
   3단계: 논문 작성
   
   위 3단계를 순서대로 자동으로 수행해 주세요."
   ```

3. **결과물 표준화**:
   - 항상 동일한 형식으로 결과 요청
   - 템플릿 사용으로 일관성 확보

### ✅ MCP 마스터 체크리스트

#### 🔧 기본 설정 완료
- [ ] Claude Desktop 설치 및 로그인
- [ ] MCP 설정 파일 생성 및 기본 서버 추가
- [ ] 연결 테스트 성공

#### 🧪 실습 완료
- [ ] task-master-mcp 4개 실습 모두 완료
- [ ] 연구 프로젝트에 실제 적용 성공
- [ ] 워크플로우 자동화 경험

#### 🔬 연구자용 서버 활용
- [ ] 전공에 맞는 MCP 서버 조합 선택
- [ ] 최소 1개 연구자용 서버 설치 및 테스트
- [ ] 실제 연구 워크플로우에 통합

#### 🚨 트러블슈팅 역량
- [ ] 일반적인 오류 상황 해결 가능
- [ ] 대안 도구 활용 방법 이해
- [ ] 최적화 및 효율성 향상 방법 습득

---

## 🎓 결론 및 다음 단계

### 🎯 MCP 활용의 핵심 benefits

1. **통합성**: 여러 도구를 한 번에 사용
2. **자동화**: 반복 작업의 완전 자동화
3. **확장성**: 새로운 도 بسهولة 추가
4. **전문성**: 도메인 특화 AI 어시스턴트

### 📈 실제 연구 생산성 향상 사례

- **문헌 조사 시간**: 80% 단축
- **프로젝트 관리 효율성**: 60% 향상
- **데이터 분석 속도**: 70% 개선
- **논문 작성 시간**: 50% 단축

### 🔗 다음 단계 권장

1. **Part 2 문서 Section 5로 진행**: SpecKit 워크플로우
2. **실제 연구 프로젝트에 MCP 적용**: 학습 내용 실전 적용
3. **전공별 커뮤니티 참여**: 경험 공유 및 학습
4. **지속적 업데이트**: 새로운 MCP 서버 및 기능 추적

### 💬 피드백 및 개선 제안

MCP 가이드가 연구 생산성에 실질적으로 도움이 되었는지 피드백을 주세요:
- **설치 과정에서 어려웠던 부분**: [구체적 건의사항]
- **실습 중 의문점이나 개선점**: [새로운 요구사항]
- **성공 사례**: [MCP 활용 성공 경험]
- **추가로 필요한 MCP 서버**: [새로운 도구 요청]

---

**Version**: v13.0 MCP Installation Guide  
**Last Updated**: 2025-11-10  
**Related**: [Part 2 Resources](README_v13_Part2.md) | [Main Part 2 Document](../Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md) | [SpecKit Guide](19_speckit_installation_guide.md)
