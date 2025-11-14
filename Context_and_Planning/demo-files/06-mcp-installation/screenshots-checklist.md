# 전체 프로젝트 스크린샷 마스터 체크리스트

**MCP 자동화 + 수동 캡처 통합 관리**

**목적**: 프로젝트 전체 스크린샷 생성 진행 상황 추적  
**저장 위치**: `resources/part{n}/images/` (Part별 하위 폴더)  
**해상도**: 1920x1080 이상  
**형식**: PNG

## 📊 전체 진행 현황

- **전체 스크린샷 수**: 61개
    - Part 1: 26개
    - Part 2: 15개
    - Part 3: 20개
- **완료**: 27/61 (44.3%)
    - Part 1: 13/26 (50%)
    - Part 2: 6/15 (40%)
    - Part 3: 8/20 (40%)

**생성 방법**:

- **MCP 자동화**: 웹페이지 기반 스크린샷 (Cline MCP webpageScreenshot 서버)
- **수동 캡처**: 데스크톱 애플리케이션 스크린샷 (macOS 스크린샷 도구)

**가이드 문서**:

- MCP 자동화: [`cline-screenshot-mcp-setup.md`](cline-screenshot-mcp-setup.md)
- 수동 캡처: [`manual-screenshot-guide.md`](../manual-screenshot-guide.md)

### MCP 자동화 현황

- **완료**: 4/15 (26.7%)
    - ⚠️ Part 1: 1/3 (2개 미생성: copilot-plans-comparison.png, vscode-download-page.png)
    - ✅ Part 2: 2/2
    - 🚧 Part 3: 1/8 (7개 대기: perplexity-main.png 등)
- **대기**: 11/15 (73.3%)
    - Part 1: 2개 재실행 필요
    - Part 3: 7개 배치 실행 필요

### 수동 캡처 현황

- **완료**: 23/46 (50%)
    - Part 1: 12/23 (52%)
    - Part 2: 4/13 (31%)
    - Part 3: 7/12 (58% - 다이어그램/폴더 구조)

## Part 1 체크리스트 (26개 - 13/26 완료, 50%)

### MCP 자동화 (1/3 완료) ⚠️

- [x] GitHub Education Pack 메인 페이지 (`github-education-pack-main.png`)
- [ ] Copilot Plans 비교 페이지 (`copilot-plans-comparison.png`) - 재실행 필요
- [ ] VS Code 다운로드 페이지 (`vscode-download-page.png`) - 재실행 필요

### 수동 캡처 완료 (12개) ✅

- [x] VS Code Extensions 마켓플레이스 (`extensions-marketplace-copilot.png`)
- [x] VS Code 폴더 구조 예시 (`vscode-folder-structure-example.png`)
- [x] Copilot Inline Completion (`copilot-inline-completion.png`)
- [x] Copilot Chat 패널 (`copilot-chat-panel.png`)
- [x] Model Picker (`copilot-model-picker.png`)
- [x] Copilot Edits Mode (`copilot-edits-mode.png`)
- [x] Agent Mode 표시 (`copilot-agent-mode.png`)
- [x] Vision 기능 이미지 첨부 (`copilot-vision-image-attach.png`)
- [x] MCP 아키텍처 다이어그램 (`mcp-architecture-diagram.png`)
- [x] Copilot 비활성화 상태 (`copilot-inactive-status.png`)
- [x] 로그인 프롬프트 (`copilot-login-prompt.png`)
- [x] 연구 컨텍스트 작성 실습 (`practice-context-writing.png`)

### 수동 캡처 필요 (13개)

- [ ] 학생 인증 폼 (민감정보 모자이크 필요)
- [ ] Copilot Pro 활성화 상태
- [ ] Copilot 확장 설치 완료
- [ ] Markdown 구조 제안
- [ ] Chat 컨텍스트 제공 예시
- [ ] Custom Instructions 파일
- [ ] AGENTS.md 파일
- [ ] Next Edit Suggestions
- [ ] Claude Desktop MCP 설정
- [ ] 제안 없음 상태
- [ ] Markdown 템플릿 사용
- [ ] Chat으로 문헌 키워드 생성
- [ ] Markdown 미리보기 (선택)

## Part 2 체크리스트 (15개 - 6/15 완료, 40%)

### MCP 자동화 완료 (2/2) ✅

- [x] MCP 프로토콜 소개 페이지 (`mcp-protocol-intro.png`)
    - ✅ **검증 완료**: 2025-11-13 13:39
    - **캡처 방법**: 2025-11-12 Chrome DevTools 수동 캡처
    - **저장 위치**: `resources/images/`
    - **해상도**: 1920x1080
    - **파일 크기**: 182KB
- [x] SpecKit 리포지토리 (`speckit-repository.png`)
    - ✅ **검증 완료**: 2025-11-13 13:39
    - **캡처 방법**: 2025-11-12 Chrome DevTools 수동 캡처
    - **저장 위치**: `resources/images/`
    - **해상도**: 1920x1080
    - **파일 크기**: 263KB

### 수동 캡처 완료 (4개) ✅

- [x] SpecKit 7단계 워크플로우 실행 (`speckit-7step-workflow.png`)
- [x] MCP 터미널 설치 과정 (`mcp-terminal-install.png`)
- [x] Copilot 워크북 Exercise 실습 (`copilot-workbook-exercise.png`)
- [x] Claude Desktop 설정 파일 (`claude-desktop-config.png`)

### 수동 캡처 필요 (9개)

- [ ] Node.js 설치 확인 터미널 화면
- [ ] MCP 서버 설치 완료 화면
- [ ] Claude Desktop MCP 연결 확인
- [ ] JSON 설정 파일 내용
- [ ] SpecKit 설치 완료
- [ ] 생성된 문서 예시 (Constitution, Spec, Plan)
- [ ] Exercise 3 코드 분석 화면
- [ ] Exercise 4 논문 작성 결과
- [ ] 일반적 오류 상황 및 해결 방법

## Part 3 체크리스트 (20개 - 8/20 완료, 40%)

### MCP 자동화 (1/8 완료) 🚧

- [x] Elicit 메인 인터페이스 (`elicit-main.png`)
    - ✅ **검증 완료**: 2025-11-13
    - **저장 위치**: `resources/images/tools-ecosystem/`
- [ ] Perplexity 메인 인터페이스 (`perplexity-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] NotebookLM 메인 인터페이스 (`notebooklm-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] Consensus 메인 인터페이스 (`consensus-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] Scite 메인 인터페이스 (`scite-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] ResearchRabbit 메인 인터페이스 (`researchrabbit-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] Connected Papers 메인 인터페이스 (`connectedpapers-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md
- [ ] Semantic Scholar 메인 인터페이스 (`semanticscholar-main.png`)
    - ⏳ **MCP 배치 대기**: part3-screenshot-generation-prompts.md

### 수동 캡처 완료 (7개) ✅

- [x] 연구 8단계 생애주기 다이어그램 (`research-8step-lifecycle.png`)
- [x] 2025년 AI 도구 생태계 전체 지도 (`ai-tools-ecosystem.png`)
- [x] 교육학 프로젝트 폴더 구조 (`education-project-folder.png`)
- [x] 생명과학 프로젝트 폴더 구조 (`life-science-project-folder.png`)
- [x] 컴퓨터공학 프로젝트 폴더 구조 (`cs-project-folder.png`)
- [x] 사회학 프로젝트 폴더 구조 (`sociology-project-folder.png`)
- [x] 음악학 프로젝트 폴더 구조 (`music-project-folder.png`)

### 수동 캡처 필요 (12개)

- [ ] 초기 연구 계획서 완성 화면
- [ ] 문헌 조사와 분석 진행 상황
- [ ] 데이터 수집 및 분석 결과
- [ ] 논문 초안 작성 진행 상황
- [ ] 최종 논문 완성 화면
- [ ] 도구 간 연결성 및 데이터 흐름
- [ ] AI 도구들이 함께 작동하는 화면
- [ ] 문제 해결 및 의사결정 과정
- [ ] 주간/월간 루틴 대시보드
- [ ] 진행 상황 추적 화면
- [ ] 품질 관리 체크리스트 실행
- [ ] 통합 폴더 구조 예시

## 📊 전체 진행 상황

- **전체**: 27/61 완료 (44.3%)
- **Part 1**: 13/26 완료 (50.0%)
- **Part 2**: 6/15 완료 (40.0%)
- **Part 3**: 8/20 완료 (40.0%)

## 🤖 MCP 자동화 현황

- **완료**: 4/15 (26.7%)
- **대기**: 11/15 (73.3%)

### 완료 내역

- ⚠️ Part 1: 1/3 (33.3%) - GitHub Education Pack 완료, 2개 재실행 필요
- ✅ Part 2: 2/2 (100%) - MCP 프로토콜 소개, SpecKit 리포지토리
- 🚧 Part 3: 1/8 (12.5%) - Elicit 완료, 7개 배치 실행 대기

### 대기 내역

- ⏳ Part 1: 2개 재실행 (copilot-plans-comparison, vscode-download-page) - ~2분 소요
- ⏳ Part 3: 7개 배치 실행 (part3-screenshot-generation-prompts.md 참조) - ~7분 소요

## 👤 수동 캡처 현황

- **완료**: 23/46 (50.0%)
- **대기**: 23/46 (50.0%)

### 완료 내역

- Part 1: 12/23 완료 (52.2%)
- Part 2: 4/13 완료 (30.8%)
- Part 3: 7/12 완료 (58.3%)

### 대기 내역

- Part 1: 11개 남음 (copilot-chat-inline-response, copilot-edits-diff-view, etc.)
- Part 2: 9개 남음 (nodejs-install-verify, mcp-server-install-complete, etc.)
- Part 3: 12개 남음 (research-plan-completion, literature-review-progress, etc.)

### 수동 캡처 가이드

상세한 단계별 가이드는 [`manual-screenshot-guide.md`](../manual-screenshot-guide.md) 참조:

- macOS 스크린샷 도구 사용법 (Cmd+Shift+4, Cmd+Shift+5)
- Part별 수동 캡처 대상 목록
- 단계별 캡처 가이드 (VS Code, Terminal, Claude Desktop)
- 품질 체크리스트 및 트러블슈팅

## 다음 단계

### 🔴 긴급 1: Part 1 MCP 재실행 (2개, ~2분)

- ⚠️ copilot-plans-comparison.png
- ⚠️ vscode-download-page.png
- **실행 방법**: `part1-screenshot-generation-prompts.md` 참조하여 MCP 배치 재실행

### 🔴 긴급 2: Part 3 MCP 배치 실행 (7개, ~7분)

- ⏳ Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar
- **실행 방법**: `part3-screenshot-generation-prompts.md` 참조
- **예상 소요 시간**: 약 7분

### 우선순위 3: Part 1 수동 캡처 (11개, ~30-40분)

- copilot-chat-inline-response, copilot-edits-diff-view, copilot-agent-command-palette 등
- VS Code 실제 사용 화면 캡처 필요
- **가이드**: [`manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.1 및 Section 7 참조

### 우선순위 4: Part 2 수동 캡처 (9개, ~20-30분)

- nodejs-install-verify, mcp-server-install-complete, claude-desktop-mcp-connection 등
- MCP 설치 과정 실제 화면 캡처 필요
- **가이드**: [`manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.2 및 Section 7 참조

### 우선순위 5: Part 3 수동 캡처 (12개, ~40-60분)

- research-plan-completion, literature-review-progress, data-collection-analysis 등
- 연구 시나리오 및 통합 워크플로우 구성 필요
- **가이드**: [`manual-screenshot-guide.md`](../manual-screenshot-guide.md) Section 6.3 및 Section 7 참조

## 📅 완료 로그

### 2025-11-13 (Part 1) - MCP 1/3, 수동 12/23

- ✅ MCP 자동화: GitHub Education Pack 완료
- ⚠️ MCP 재실행 필요: Copilot Plans, VS Code 다운로드 (Bootstrap permission denied)
- ✅ 수동 캡처 완료 (12개):
    - extensions-marketplace-copilot, vscode-folder-structure-example
    - copilot-inline-completion, copilot-chat-panel, copilot-model-picker
    - copilot-edits-mode, copilot-agent-mode, copilot-vision-image-attach
    - mcp-architecture-diagram, copilot-inactive-status
    - copilot-login-prompt, practice-context-writing

### 2025-11-13 (Part 2) - MCP 2/2, 수동 4/13

- ✅ MCP 자동화 완료 (2개): MCP 프로토콜 소개, SpecKit 리포지토리
- ✅ 수동 캡처 완료 (4개):
    - speckit-7step-workflow, mcp-terminal-install
    - copilot-workbook-exercise, claude-desktop-config

### 2025-11-13 (Part 3) - MCP 1/8, 수동 7/12

- ✅ MCP 자동화: Elicit 완료
- ⏳ MCP 배치 대기 (7개): Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar
- ✅ 수동 캡처 완료 (7개):
    - research-8step-lifecycle, ai-tools-ecosystem
    - education/life-science/cs/sociology/music-project-folder (5개 폴더 구조)

## 참고 문서

### MCP 자동화 관련

- `part1-screenshot-generation-prompts.md`: Part 1 MCP 프롬프트
- `part2-screenshot-generation-prompts.md`: Part 2 MCP 프롬프트
- `part3-screenshot-generation-prompts.md`: Part 3 MCP 프롬프트
- `cline-screenshot-mcp-setup.md`: MCP 설치 및 사용 가이드

### 수동 캡처 관련

- **`manual-screenshot-guide.md`**: 수동 스크린샷 캡처 가이드 (NEW)
  - macOS 스크린샷 도구 사용법
  - Part별 수동 캡처 대상 목록
  - 단계별 캡처 가이드
  - 품질 체크리스트 및 트러블슈팅

### 스크린샷 요구사항

- `resources/11_screenshot_descriptions.md`: Part 1 상세 가이드
- `resources/12_screenshot_descriptions.md`: Part 2 상세 가이드
- `resources/24-37_screenshot_descriptions.md`: Part 3 상세 가이드

## 🎉 MCP 자동화 현황 요약

### 🚧 총 4/15개 웹페이지 스크린샷 자동 생성 완료 (26.7%)

**Part 1 (1/3 완료, 33.3%)** ⚠️:
- ✅ GitHub Education Pack
- ⏳ Copilot Plans (재실행 필요)
- ⏳ VS Code 다운로드 (재실행 필요)

**Part 2 (2/2 완료, 100%)** ✅:
- ✅ MCP 프로토콜 소개
- ✅ SpecKit 리포지토리

**Part 3 (1/8 완료, 12.5%)** 🚧:
- ✅ Elicit
- ⏳ Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar (배치 실행 대기)

**총 소요 시간**: 완료분 ~4분, 대기분 ~9분 (예상)
**사용 도구**: Cline MCP `webpageScreenshot` 서버 (`@srigi/mcp-webpage-screenshot`)
**성공률**: 4/4 (100% - 실행된 것 중), 다음 작업: Part 1 재실행 2개 + Part 3 배치 7개

---

## 🚀 수동 캡처 빠른 참조

### macOS 스크린샷 단축키

- **Cmd + Shift + 3**: 전체 화면 캡처
- **Cmd + Shift + 4**: 영역 선택 캡처
- **Cmd + Shift + 4 + Space**: 창 단위 캡처
- **Cmd + Shift + 5**: 스크린샷 고급 옵션 (타이머, 저장 위치, 포인터 표시 등)

### 캡처 대상별 권장 방법

- **VS Code 인터페이스**: Cmd + Shift + 4 + Space (창 단위) 또는 Cmd + Shift + 4 (영역 선택)
- **Terminal 출력**: Cmd + Shift + 4 (영역 선택 - 명령어 + 결과만 포함)
- **Claude Desktop 대화**: Cmd + Shift + 4 (영역 선택 - 질문 + 답변 포함)
- **Copilot 기능**: Cmd + Shift + 4 (영역 선택 - 기능 강조)

### 품질 체크 빠른 확인

1. **해상도**: 1920x1080 이상 (Get Info로 확인)
2. **파일 형식**: PNG (Finder에서 확장자 확인)
3. **파일 크기**: 2MB 이하 (필요시 TinyPNG로 압축)
4. **파일명**: kebab-case, 설명적 (예: `copilot-chat-inline-response.png`)

### 상세 가이드

전체 단계별 가이드, 트러블슈팅, Part별 대상 목록은 [`manual-screenshot-guide.md`](../manual-screenshot-guide.md) 참조
