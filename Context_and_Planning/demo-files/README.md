# 시연용 데모 파일 모음 (v13.0 업데이트)

이 디렉토리는 강의 중 실시간 시연에 사용할 예제 파일들을 포함합니다.

## 🔗 관련 문서

이 시연 파일들은 다음 주요 문서와 연결되어 있습니다:

### 📋 프로젝트 기획 문서
- **[../idea.md](../idea.md)** - 강의 전체 기획안 및 주요 주제
- **[../AGENTS.md](../AGENTS.md)** - AI 에이전트 활용 규칙 및 가이드라인

### 🎯 시연 매핑 가이드

| 시연 파트 | 관련 문서 | 주요 내용 |
|----------|----------|----------|
| **Part 1** (Context Engineering) | `../idea.md` - 주제 1 | Markdown 구조화, MCP 활용 |
| **Part 2** (Planning & Management) | `../idea.md` - 주제 2 | Spec 문서, 작업 분해 |
| **Part 3** (통합 워크플로우) | `../idea.md` - 전체 | 3가지 원칙의 통합 활용 |

### 📚 추가 참고 자료
- **[../README.md](../README.md)** - 전체 강의 계획 및 문서 인덱스
- **[../lecture-structure.md](../lecture-structure.md)** - 강의 구조 및 시간 배분
- **[../content-flow.md](../content-flow.md)** - 콘텐츠 상세 흐름

---

## 🆕 v13.0 새로운 시연 (4개)

### Demo 5: Copilot 워크북 (Part 2)
- **내용**: Exercise 1 (문헌 조사 자동화)
- **시간**: 5분
- **도구**: VS Code + GitHub Copilot
- **핵심**: 키워드 생성, 논문 요약 템플릿
- **자료**: `v13.0_resources/part2/12_copilot_workbook_exercises.md`

### Demo 6: MCP 설치 (Part 2)
- **내용**: Claude Desktop + task-master-mcp 설치
- **시간**: 5분
- **도구**: Claude Desktop, JSON 편집
- **핵심**: 설정 파일 편집, MCP 서버 연결
- **자료**: `v13.0_resources/part2/15_mcp_installation_guide.md`

### Demo 7: SpecKit 실습 (Part 2)
- **내용**: 연구 프로젝트 Spec 작성
- **시간**: 5분
- **도구**: Terminal, specify CLI
- **핵심**: 7단계 워크플로우, constitution → spec
- **자료**: `v13.0_resources/part2/21_speckit_practice_project.md`
- **참고**: 선택적 도구, 간단한 프로젝트는 불필요

### Demo 8: 통합 워크플로우 (Part 3)
- **내용**: 6개월 석사논문 프로젝트 압축 시연
- **시간**: 5분
- **도구**: 모든 도구 통합
- **핵심**: Part 1-2-3 통합, 실제 프로젝트 구조
- **자료**: `v13.0_resources/part3/26_education_complete_scenario.md`

## 📁 디렉토리 구조

```
demo-files/
├── README.md (이 파일)
├── 01-vscode-markdown/ (기존)
├── 02-github-copilot/ (기존)
├── 03-github-projects/ (기존)
├── 04-task-master-mcp/ (기존)
├── 05-copilot-workbook/ (NEW v13.0)
│   ├── README.md
│   ├── literature-search-starter.md (시연용)
│   ├── literature-search-completed.md (백업)
│   ├── exercise1-prompts.md (프롬프트 가이드)
│   ├── exercise1-answers.md (완전한 해답)
│   └── setup-checklist.md (준비 체크리스트)
├── 06-mcp-installation/ (NEW v13.0)
│   ├── README.md
│   ├── installation-script.md (5분 시연 스크립트)
│   ├── config-template.json (최소 설정)
│   ├── config-completed.json (4개 서버)
│   ├── test-prompts.md (테스트 프롬프트)
│   ├── troubleshooting-quick.md (빠른 문제 해결)
│   └── screenshots-checklist.md (스크린샷 목록)
├── 07-speckit-practice/ (NEW v13.0)
│   ├── README.md
│   ├── terminal-commands.md (명령어 모음)
│   ├── spec-example.md (Spec 문서 예시)
│   └── setup-checklist.md (준비 체크리스트)
├── 08-integrated-workflow/ (NEW v13.0)
│   ├── README.md
│   ├── demo-script-5min.md (5분 시연 스크립트)
│   └── folder-structure-complete.md (완전한 구조)
├── backup/
│   ├── videos/
│   │   ├── demo1-vscode-markdown.mp4 (기존)
│   │   ├── demo2-github-copilot.mp4 (기존)
│   │   ├── demo3-github-projects.mp4 (기존)
│   │   ├── demo4-taskmaster-mcp.mp4 (기존)
│   │   ├── demo5-copilot-workbook.mp4 (NEW)
│   │   ├── demo6-mcp-installation.mp4 (NEW)
│   │   ├── demo7-speckit-practice.mp4 (NEW)
│   │   └── demo8-integrated-workflow.mp4 (NEW)
│   ├── screenshots/
│   │   ├── vscode/ (기존)
│   │   ├── copilot/ (기존)
│   │   ├── projects/ (기존)
│   │   ├── taskmaster/ (기존)
│   │   ├── copilot-workbook/ (NEW)
│   │   ├── mcp-installation/ (NEW)
│   │   ├── speckit/ (NEW)
│   │   └── integrated-workflow/ (NEW)
│   └── slides/ (백업 슬라이드)
├── rehearsal-guide.md (업데이트 필요)
├── demo-cheatsheet.md (업데이트 필요)
└── installation-guides.md (기존)
```

## 🎯 사용 방법 (v13.0 업데이트)

### 강의 구성
- **Part 1** (40분): Demo 1 (VS Code + Markdown)
- **Part 2** (40분): Demo 2 (Copilot), Demo 5 (Copilot 워크북), Demo 6 (MCP 설치)
- **Part 3** (20분): Demo 7 (SpecKit, 선택적), Demo 8 (통합 워크플로우)

### 시연 선택 가이드
- **필수 시연** (2시간 강의): Demo 1, 2, 5, 8
- **선택적 시연** (시간 여유 시): Demo 6, 7
- **생략 가능** (자료로 대체): Demo 3, 4 (기존 Projects, task-master는 Demo 8에 통합)

### v13.0 특징
- 2025년 최신 도구 반영 (Elicit, NotebookLM, Consensus)
- 실습 워크북 형태 (단계별 연습)
- 완전한 프로젝트 예시 (폴더 구조 + 파일 내용)
- 선택적 도구 명시 (SpecKit)

## ⚠️ v13.0 주의사항

### Demo 6 (MCP 설치)
- 터미널 사용 필요 → 초보자에게 어려울 수 있음
- 대안 도구 반드시 언급 (ChatGPT Custom GPTs, Claude Projects)
- "설치 어려우면 개념만 이해하고 대안 사용" 강조

### Demo 7 (SpecKit)
- Python 3.11+ 필요 → 설치 장벽 높음
- "선택적 도구" 명확히 강조
- 간단한 프로젝트는 Section 3 (Spec-driven Planning)으로 충분

### Demo 8 (통합 워크플로우)
- 6개월 → 5분 압축 → 핵심만 보여주기
- 모든 파일 내용 시연 불가 → 구조와 개념 중심
- 자세한 내용은 Part 3 자료 참고 안내

## 🎯 사용 방법

### 강의 준비 시
1. 각 디렉토리의 시연용 파일 확인
2. 백업 자료 준비 상태 점검
3. 리허설 진행 (v13.0 업데이트)

### 강의 중
1. 해당 시점에 맞는 디렉토리 열기
2. 시연용 빈 파일로 라이브 시연
3. 문제 발생 시 완성 예시 또는 백업 자료 사용
4. 선택적 도구 (Demo 6, 7) 시간 여유 시만 시연

### 강의 후
1. 학생들에게 예제 파일 공유
2. GitHub에 공개하여 지속적 접근 가능
3. v13.0 자료 다운로드 안내

## ⚠️ 주의사항

- 시연용 빈 파일은 강의 직전에 초기화
- 완성 예시는 백업용으로만 사용
- 모든 파일은 Git으로 버전 관리
- 민감한 정보 포함 금지
- v13.0 신규 도구는 선택적 시연 (시간 여유 시만)
- Demo 6, 7은 대안 도구 반드시 언급

---

*이 시연 파일들은 실제 강의에서 활용되는 예시로, v13.0 업데이트에 따라 기존 파일과 신규 파일이 포함되어 있습니다.*
