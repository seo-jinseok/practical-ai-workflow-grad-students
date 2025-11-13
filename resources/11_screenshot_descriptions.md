# Part 1 스크린샷 캡처 가이드

**목적**: Part 1에 필요한 모든 스크린샷 목록 및 캡처 가이드

**상태**: 🚧 In Progress (13/26 완료, 50%, MCP 자동화 1개 + 수동 12개)

**업데이트**: 2025-11-13

## 사용 방법

1. 이 파일을 체크리스트로 사용
2. 각 스크린샷 캡처 후 ✅ 표시
3. 파일명은 제안된 이름 사용
4. 저장 위치: `resources/images/part1/`
5. **MCP 자동화**: 웹페이지 기반 스크린샷은 [Cline MCP 설치 가이드](../../Context_and_Planning/demo-files/06-mcp-installation/cline-screenshot-mcp-setup.md) 참고

## 1. GitHub Education & Copilot 관련

### 1.1 GitHub Education Pack 페이지 **[MCP 자동화 가능]**
- [x] **파일명**: `github-education-pack-main.png`
  - ✅ **생성 완료**: 2025-11-12
  - **파일 크기**: [실제 크기]MB
  - **해상도**: 1920x1080
  - **저장 위치**: `resources/images/part1/github-education/`
- **URL**: https://education.github.com/pack
- **캡처 내용**:
  - 메인 페이지 전체
  - "Get your pack" 버튼 강조
  - 주요 혜택 목록 보이게
- **해상도**: 1920x1080
- **주석**: 빨간 박스로 "GitHub Copilot" 항목 강조
- **용도**: Section 2.2 (학생 무료 혜택)

### 1.2 학생 인증 폼 **[수동 캡처 필요]**
- [ ] **파일명**: `github-student-verification-form.png`
- **캡처 내용**:
  - 학생 인증 신청 페이지
  - 학교 이메일 입력 필드
  - 학생증 업로드 섹션
- **민감정보**: 개인정보 모자이크 처리
- **용도**: Resource 01 (학생 가이드)

### 1.3 Copilot Pro 활성화 상태
- [ ] **파일명**: `copilot-pro-status-active.png`
- **캡처 내용**:
  - VS Code 하단 상태바
  - Copilot 아이콘 (체크 표시)
  - "Copilot Pro" 텍스트 보이게
- **해상도**: 상태바 부분만 확대
- **용도**: Section 2.2, Resource 01

### 1.4 Copilot Plans 비교 페이지 **[MCP 자동화 가능]**
- [ ] **파일명**: `copilot-plans-comparison.png`
  - ⏳ **상태**: 파일 미생성, MCP 재실행 필요
  - **예상 크기**: ~200KB
  - **해상도**: 1920x1080
  - **저장 위치**: `resources/images/part1/github-education/`
- **URL**: https://github.com/features/copilot/plans
- **캡처 내용**:
  - Free, Pro, Pro+ 비교 테이블
  - 학생 혜택 표시 부분
- **용도**: Resource 01, 06

## 2. VS Code 설치 및 설정

### 2.1 VS Code 다운로드 페이지 **[MCP 자동화 가능]**
- [ ] **파일명**: `vscode-download-page.png`
  - ⏳ **상태**: 파일 미생성, MCP 재실행 필요
  - **예상 크기**: ~150KB
  - **해상도**: 1920x1080
  - **저장 위치**: `resources/images/part1/vscode-setup/`
- **URL**: https://code.visualstudio.com/
- **캡처 내용**: 메인 다운로드 페이지, OS별 버전 표시
- **용도**: Section 2.3

### 2.2 VS Code Extensions 마켓플레이스
- [ ] **파일명**: `vscode-extensions-marketplace.png`
- **캡처 내용**:
  - Extensions 탭 (Ctrl+Shift+X)
  - "GitHub Copilot" 검색 결과
  - Install 버튼 강조
- **용도**: Section 2.3

### 2.3 Copilot 확장 설치 완료
- [ ] **파일명**: `copilot-extension-installed.png`
- **캡처 내용**:
  - 설치된 Copilot 확장
  - "Reload Required" 또는 활성화 상태
- **용도**: Section 2.3

### 2.4 VS Code 폴더 구조
- [ ] **파일명**: `vscode-folder-structure-example.png`
- **캡처 내용**:
  - Explorer 패널
  - 연구 폴더 구조 (01_계획, 02_자료수집 등)
  - README.md 파일 열린 상태
- **용도**: Section 2.4

## 3. Copilot 기능 시연

### 3.1 Inline Completion
- [ ] **파일명**: `copilot-inline-completion.png`
- **캡처 내용**:
  - Markdown 파일에서 Copilot 제안 (회색 텍스트)
  - 커서 위치 표시
  - Tab 키 힌트
- **예시 내용**: 연구 계획서 작성 중
- **용도**: Section 5.2

### 3.2 Copilot Chat 패널
- [ ] **파일명**: `copilot-chat-panel.png`
- **캡처 내용**:
  - Chat 패널 열린 상태 (Ctrl+Shift+I)
  - 샘플 질문과 응답
  - 모델 선택 드롭다운 보이게
- **용도**: Section 5.3

### 3.3 Model Picker
- [ ] **파일명**: `copilot-model-picker.png`
- **캡처 내용**:
  - 모델 선택 드롭다운 확장
  - GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro 등 목록
  - 현재 선택된 모델 강조
- **용도**: Section 5.1, Resource 06

### 3.4 Markdown 구조 제안
- [ ] **파일명**: `copilot-markdown-structure-suggestion.png`
- **캡처 내용**:
  - Markdown 파일에서 제목 입력 후 Copilot 제안
  - 자동 완성되는 섹션 구조
- **예시**: "# 연구 계획서" 입력 후 하위 섹션 제안
- **용도**: Section 4.4

### 3.5 Chat 컨텍스트 제공 예시
- [ ] **파일명**: `copilot-chat-with-context.png`
- **캡처 내용**:
  - Chat에 긴 컨텍스트 입력
  - AI 응답 (구체적이고 유용한)
- **예시**: 교육학 연구 컨텍스트 + 질문
- **용도**: Section 5.4

## 4. 고급 기능 (2025)

### 4.1 Agent Mode 표시
- [ ] **파일명**: `copilot-agent-mode-indicator.png`
- **캡처 내용**:
  - Chat 패널에서 Agent mode 선택
  - Mode picker (Ask/Edit/Agent)
- **용도**: Part 1에서는 간단히 언급만 (Part 2에서 상세)

### 4.2 Custom Instructions 파일
- [ ] **파일명**: `copilot-instructions-file.png`
- **캡처 내용**:
  - `.github/copilot-instructions.md` 파일
  - 샘플 내용 (프로젝트 가이드라인)
- **용도**: Part 1에서 소개, Part 2에서 활용

### 4.3 AGENTS.md 파일
- [ ] **파일명**: `agents-md-file.png`
- **캡처 내용**:
  - 루트의 AGENTS.md 파일
  - 샘플 agent instructions
- **용도**: Part 1에서 소개

### 4.4 Vision 기능 (이미지 첨부)
- [ ] **파일명**: `copilot-vision-image-attach.png`
- **캡처 내용**:
  - Chat 패널에 이미지 드래그 앤 드롭
  - 또는 "Attach > Screenshot Window"
  - 이미지 썸네일 표시
- **용도**: Section 5.1 (간단 소개)

### 4.5 Next Edit Suggestions
- [ ] **파일명**: `copilot-next-edit-suggestion.png`
- **캡처 내용**:
  - 코드/문서 편집 중
  - 왼쪽 gutter에 화살표 표시
  - 제안된 다음 편집 위치
- **용도**: Section 5.1 (간단 소개)

## 5. MCP 관련

### 5.1 MCP 개념 다이어그램
- [x] **파일명**: `mcp-architecture-diagram.png`
  - ✅ **생성 완료**: 2025-11-13
  - **파일 크기**: [실제 크기]MB
  - **해상도**: 1920x1080
  - **저장 위치**: `resources/images/part1/mcp/`
  - **캡처 내용**:
  - 직접 제작: Host App ↔ MCP Servers 구조
  - 또는 Anthropic 공식 다이어그램 사용 (출처 표기)
  - **도구**: draw.io, Excalidraw, 또는 Mermaid
  - **용도**: Section 6.3, Resource 08

### 5.2 Claude Desktop MCP 설정 (참고용)
- [ ] **파일명**: `claude-desktop-mcp-config.png`
- **캡처 내용**:
  - Claude Desktop의 MCP 서버 설정 화면
  - 예시 서버 목록
- **용도**: Section 6 (MCP 실제 사용 예시)
- **참고**: Part 2에서 상세 다룸

## 6. 문제 해결 관련

### 6.1 Copilot 비활성화 상태
- [x] **파일명**: `copilot-inactive-status.png`
  - ✅ **생성 완료**: 2025-11-13
  - **파일 크기**: [실제 크기]MB
  - **해상도**: 1920x1080
  - **저장 위치**: `resources/images/part1/troubleshooting/`
- **캡처 내용**:
  - 상태바에 Copilot 아이콘 (X 표시 또는 회색)
  - "Copilot is not active" 메시지
- **용도**: Resource 09 (문제 해결 가이드)

### 6.2 로그인 프롬프트
- [ ] **파일명**: `copilot-login-prompt.png`
- **캡처 내용**:
  - "Sign in to use GitHub Copilot" 알림
  - 로그인 버튼
- **용도**: Resource 09

### 6.3 제안 없음 상태
- [ ] **파일명**: `copilot-no-suggestions.png`
- **캡처 내용**:
  - 타이핑 중이지만 제안 없음
  - 가능한 원인 표시
- **용도**: Resource 09

## 7. 실습 예시

### 7.1 연구 컨텍스트 작성 중
- [ ] **파일명**: `practice-context-writing.png`
- **캡처 내용**:
  - 연구컨텍스트.md 파일 작성 중
  - Copilot 제안 활용
  - 교육학 예시
- **용도**: Section 3.3

### 7.2 Markdown 템플릿 사용
- [ ] **파일명**: `practice-markdown-template.png`
- **캡처 내용**:
  - 연구 계획서 템플릿 작성
  - 체크리스트, 표 등 활용
- **용도**: Section 4.3

### 7.3 Chat으로 문헌 키워드 생성
- [ ] **파일명**: `practice-chat-keywords.png`
- **캡처 내용**:
  - Chat에 연구 주제 입력
  - AI가 생성한 검색 키워드 목록
- **용도**: Section 5.5

## 📸 캡처 가이드라인

### 기술 요구사항

- **해상도**: 정확히 1920x1080 (Retina/HiDPI 권장)
- **포맷**: PNG (투명 배경 필요 시), JPG (일반)
- **파일 크기**: 최대 2MB (압축 필요 시 TinyPNG 사용)
- **명명 규칙**: `kebab-case-description.png`

### 시각적 가이드라인

- **강조**: 빨간 박스 또는 화살표로 중요 부분 표시
- **민감정보**: 개인정보, 이메일 등 모자이크 처리
- **일관성**: 동일한 테마 (Dark/Light) 사용
- **가독성**: 텍스트가 선명하게 보이도록

### 도구 추천

- **캡처**: macOS Cmd+Shift+4, Windows Snipping Tool, Greenshot
- **편집**: Photoshop, GIMP, Preview (macOS), Paint.NET
- **주석**: Skitch, Annotate, Snagit
- **압축**: TinyPNG, ImageOptim

### 저장 위치

```
resources/
└── images/
    └── part1/
        ├── github-education/
        ├── vscode-setup/
        ├── copilot-features/
        ├── mcp/
        └── troubleshooting/
```

## ✅ 캡처 진행 상황

- [x] GitHub Education & Copilot (1/4개 완료 - MCP 자동화 1개, 수동 0개)
- [ ] VS Code 설치 및 설정 (0/4개 완료 - MCP 2개 미생성)
- [x] Copilot 기능 시연 (4/5개 완료 - 수동 4개)
- [x] 2025 신기능 (4/5개 완료 - 수동 4개)
- [x] MCP 관련 (2/2개 완료 - 수동 2개)
- [x] 문제 해결 (2/3개 완료 - 수동 2개)
- [ ] 실습 예시 (0/3개)

**총 26개 스크린샷 (13/26 완료, 50%)**

**우선순위**:
1. ⚠️ MCP 자동화: 1/3개 완료 (2개 파일 미생성, 재실행 필요)
2. ✅ 수동 캡처 완료: 12/23개 (52%)
3. � 필수 남은 작업: VS Code 설정 2개, Copilot 기능 1개
4. � 선택 작업: 실습 예시 3개, 문제 해결 1개

## 🤖 MCP 자동화 로그

### 2025-11-12 - MCP 실행 결과

- ✅ **GitHub Education Pack** (파일 확인됨: `github-education-pack-main.png`)
- ⚠️ **Copilot Plans** (파일 미생성, 재생성 필요: `copilot-plans-comparison.png`)
- ⚠️ **VS Code 다운로드** (파일 미생성, 재생성 필요: `vscode-download-page.png`)

**사용 도구**: Cline MCP `webpageScreenshot` 서버 (`@srigi/mcp-webpage-screenshot`)
**완료**: 1/3개 (33.3%)
**소요 시간**: 약 1분 (성공한 1개)

**참고**: MCP 자동화 2개 파일 미생성. `part1-screenshot-generation-prompts.md` 재실행 필요.

### 2025-11-13 - 수동 캡처 완료 (12개)

- ✅ `vscode-extensions-marketplace.png` (Extensions 탭)
- ✅ `vscode-folder-structure-example.png` (프로젝트 구조)
- ✅ `copilot-inline-completion.png` (인라인 제안)
- ✅ `copilot-chat-panel.png` (채팅 패널)
- ✅ `copilot-model-picker.png` (모델 선택)
- ✅ `copilot-edits-mode.png` (Edits 모드)
- ✅ `copilot-agent-mode.png` (Agent 모드)
- ✅ `copilot-vision-image-attach.png` (Vision 이미지 첨부)
- ✅ `mcp-architecture-diagram.png` (MCP 아키텍처)
- ✅ `copilot-inactive-status.png` (비활성 상태)
- ✅ `copilot-login-prompt.png` (로그인 프롬프트)
- ✅ `practice-context-writing.png` (컨텍스트 작성 실습)

**방법**: VS Code 스크린샷, 이미지 편집
**총 소요 시간**: 약 1-2시간
**진행률**: 12/23 수동 항목 (52%)

---

**업데이트**: 2025-11-13

**담당**: [강사/조교 이름]

**완료 목표**: Part 1 작성 완료 전
