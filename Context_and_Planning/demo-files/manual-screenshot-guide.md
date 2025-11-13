# 수동 스크린샷 캡처 가이드 (Manual Screenshot Capture Guide)

**버전**: v13.0  
**날짜**: 2025-11-13  
**상태**: 📋 Guide (가이드 문서)  
**대상**: Part 1, Part 2, Part 3의 데스크톱 스크린샷 캡처

---

## 목차 (Table of Contents)

1. [개요 (Overview)](#개요-overview)
2. [MCP 자동화 vs 수동 캡처 비교](#mcp-자동화-vs-수동-캡처-비교)
3. [macOS 스크린샷 도구 사용법](#macos-스크린샷-도구-사용법)
4. [Part별 수동 캡처 대상 목록](#part별-수동-캡처-대상-목록)
5. [단계별 캡처 가이드](#단계별-캡처-가이드)
6. [품질 체크리스트](#품질-체크리스트)
7. [트러블슈팅](#트러블슈팅)
8. [관련 문서](#관련-문서)
9. [부록: 빠른 참조 카드](#부록-빠른-참조-카드)

---

## 개요 (Overview)

### 목적

이 가이드는 MCP 자동화로 생성할 수 없는 데스크톱 애플리케이션 스크린샷을 수동으로 캡처하는 방법을 안내합니다.

### MCP 자동화의 한계

Cline MCP `webpageScreenshot` 서버는 웹페이지 기반 스크린샷만 생성할 수 있습니다. 다음과 같은 데스크톱 애플리케이션 화면은 수동 캡처가 필요합니다:

- **VS Code 실행 화면**: Extensions 마켓플레이스, Copilot 활성화 상태, 실시간 제안
- **Terminal 명령어 결과**: Node.js 설치 확인, MCP 서버 설치 과정
- **Claude Desktop 설정**: MCP 서버 설정 화면, JSON 설정 파일
- **Copilot 기능 시연**: Inline completion, Chat 패널, Agent mode

### 이 가이드의 사용 방법

1. **Part별 캡처 대상 확인**: Section 4에서 필요한 스크린샷 목록 확인
2. **도구 사용법 숙지**: Section 3에서 macOS 스크린샷 단축키 학습
3. **단계별 실행**: Section 5의 애플리케이션별 캡처 가이드 따라하기
4. **품질 검증**: Section 6의 체크리스트로 결과물 확인
5. **문제 해결**: Section 7의 트러블슈팅 참조

---

## MCP 자동화 vs 수동 캡처 비교

| 구분 | MCP 자동화 | 수동 캡처 |
|------|-----------|----------|
| **대상** | 웹페이지 (URL 기반) | 데스크톱 애플리케이션 |
| **도구** | Cline MCP webpageScreenshot | macOS 스크린샷 도구 |
| **장점** | 빠르고 일관된 품질, 배치 실행 가능 | 유연한 캡처 영역 선택, 실시간 UI 캡처 |
| **단점** | 웹페이지만 가능, JavaScript 렌더링 필요 | 수동 작업 필요, 시간 소요 |
| **예시** | GitHub 페이지, 공식 문서, 연구 도구 | VS Code, Terminal, Claude Desktop |
| **예상 시간** | 1개당 ~1분 | 1개당 ~2-5분 (편집 포함) |

---

## macOS 스크린샷 도구 사용법

### 3.1 기본 단축키

- **`Cmd + Shift + 3`**: 전체 화면 캡처
  - 모든 모니터의 화면을 개별 파일로 저장
  - 즉시 캡처되며 썸네일이 우측 하단에 표시

- **`Cmd + Shift + 4`**: 영역 선택 캡처
  - 십자선 커서로 드래그하여 영역 선택
  - `Space` 누르면 윈도우 캡처 모드로 전환
  - `Esc` 누르면 캡처 취소

- **`Cmd + Shift + 4` → `Space`**: 특정 윈도우 캡처
  - 윈도우 위로 커서 이동 시 하이라이트 표시
  - 클릭하여 해당 윈도우만 캡처 (그림자 포함)
  - `Option` 누르면 그림자 제외

- **`Cmd + Shift + 5`**: 스크린샷 도구 (고급 옵션)
  - 캡처 영역 선택, 저장 위치 설정, 타이머 설정 가능
  - 화면 녹화 기능도 제공

### 3.2 고급 옵션 (Cmd + Shift + 5)

스크린샷 도구 패널에서 다음 설정 가능:

**캡처 영역 선택**:
- 전체 화면
- 선택한 윈도우
- 선택한 영역 (드래그)

**저장 위치 설정**:
- 데스크톱 (기본값)
- 문서
- 클립보드
- 메일
- 메시지
- 미리보기
- Other Location → 프로젝트 폴더 선택 가능

**타이머 설정**:
- 없음 (즉시 캡처)
- 5초 지연
- 10초 지연
- **사용 시나리오**: 메뉴 펼침 상태, 툴팁, Copilot 제안 캡처 시 유용

**마우스 포인터 표시**:
- 체크: 캡처에 마우스 커서 포함
- **사용 시나리오**: 클릭 위치 강조, 튜토리얼 화면

**썸네일 표시**:
- 체크: 캡처 후 우측 하단에 썸네일 표시 (편집 가능)
- 체크 해제: 즉시 저장

### 3.3 캡처 후 편집

썸네일 클릭 시 Markup 도구 사용 가능:

**도구 모음**:
- 🖊️ **스케치**: 자유 그리기
- 🔴 **도형**: 사각형, 원, 화살표, 선
- 📝 **텍스트**: 텍스트 상자 추가
- 🖍️ **서명**: 서명 추가
- 🔍 **확대**: 특정 영역 확대

**편집 기능**:
- **크롭**: 이미지 자르기
- **회전**: 90도 회전
- **색상 조정**: 자동 보정
- **저장/공유**: 편집 완료 후 저장 또는 공유

### 3.4 추가 도구

**Preview (미리보기)**:
- macOS 기본 이미지 뷰어
- Tools → Annotate → Markup 도구 사용
- Tools → Adjust Size → 해상도/파일 크기 조정
- **사용 시나리오**: 캡처 후 세밀한 편집, 해상도 확인

**Skitch** (선택사항):
- 화살표, 텍스트, 도형 추가에 특화
- 픽셀 단위 정밀 편집
- **다운로드**: https://evernote.com/products/skitch

**Snagit** (선택사항):
- 전문적인 스크린샷 및 화면 녹화 도구
- 스크롤 캡처, 파노라마 캡처 지원
- **다운로드**: https://www.techsmith.com/screen-capture.html (유료)

**Chrome DevTools** (웹페이지 전용):
- `Cmd + Shift + P` → "Capture screenshot" 입력
- Full size screenshot (전체 페이지), Capture area (영역 선택) 가능
- **사용 시나리오**: 긴 웹페이지 전체 캡처, MCP 자동화 백업

---

## 4. Part별 수동 캡처 대상 목록

### 4.1 Part 1 수동 캡처 대상 (13개 대기)

#### VS Code 관련 (4개)

- **`github-student-verification-form.png`**
  - 내용: GitHub Student Developer Pack 학생 인증 신청 페이지
  - 주의사항: 개인정보 (이름, 이메일, 학교명) 모자이크 처리

- **`copilot-pro-status-active.png`**
  - 내용: VS Code 하단 상태바, Copilot Pro 활성화 표시
  - 캡처 위치: 상태바 우측 Copilot 아이콘

- **`copilot-extension-installed.png`**
  - 내용: Extensions 탭에서 GitHub Copilot 설치 완료 상태
  - 캡처 위치: Extensions 사이드바, "Installed" 섹션

- **`copilot-login-prompt.png`**
  - 내용: "Sign in to use GitHub Copilot" 알림 팝업
  - 캡처 타이밍: VS Code 최초 실행 시 또는 로그아웃 상태

#### Copilot 기능 시연 (5개)

- **`copilot-markdown-structure-suggestion.png`**
  - 내용: Markdown 파일에서 제목, 목록 구조 자동 제안
  - 캡처 타이밍: 타이핑 중 회색 제안 텍스트 표시될 때

- **`copilot-chat-with-context.png`**
  - 내용: Chat 패널에 긴 컨텍스트 입력 및 AI 응답
  - 캡처 범위: Chat 입력창 + 응답 전체 (스크롤 필요 시 여러 장)

- **`copilot-agent-mode-indicator.png`**
  - 내용: Chat 패널 상단의 Agent mode 선택 드롭다운
  - 캡처 타이밍: Mode picker 펼쳐진 상태

- **`copilot-instructions-file.png`**
  - 내용: `.github/copilot-instructions.md` 파일 내용
  - 캡처 범위: 파일 전체 (강조 구문 포함)

- **`agents-md-file.png`**
  - 내용: 프로젝트 루트의 `AGENTS.md` 파일 내용
  - 캡처 범위: 파일 상단 주요 섹션

#### 2025 신기능 (2개)

- **`copilot-next-edit-suggestion.png`**
  - 내용: 코드 편집기 왼쪽 gutter에 화살표 표시, 다음 편집 위치 제안
  - 캡처 위치: Gutter + 해당 코드 줄

- **`claude-desktop-mcp-config.png`**
  - 내용: Claude Desktop → Settings → Developer → MCP Servers
  - 주의사항: API 키, 경로 모자이크 처리

#### 문제 해결 (1개)

- **`copilot-no-suggestions.png`**
  - 내용: 타이핑 중이지만 Copilot 제안이 나타나지 않는 상태
  - 캡처 타이밍: 5-10초 타이핑 후에도 제안 없을 때

#### 실습 예시 (2개)

- **`practice-markdown-template.png`**
  - 내용: 연구 계획서 템플릿 작성 (체크리스트, 표 활용)
  - 캡처 범위: Markdown 에디터 전체, 미리보기 포함 가능

- **`practice-chat-keywords.png`**
  - 내용: Chat에 연구 주제 입력, AI 생성 검색 키워드
  - 캡처 범위: 질문 + 키워드 리스트 응답

**총 13개 항목** (VS Code 4 + Copilot 기능 5 + 2025 신기능 2 + 문제 해결 1 + 실습 1개는 선택사항)

### 4.2 Part 2 수동 캡처 대상 (9개 대기)

#### MCP 설치 과정 (3개)

- **`mcp-installation-2-node-version.png`**
  - 내용: Terminal에서 `node --version` 실행 결과
  - 캡처 범위: 프롬프트 + 명령어 + 버전 출력

- **`mcp-installation-3-server-install.png`**
  - 내용: MCP 서버 설치 완료 화면 (`npm install` 성공 메시지)
  - 캡처 범위: 설치 로그 마지막 부분

- **`mcp-installation-4-json-config.png`**
  - 내용: JSON 설정 파일 내용 (구문 강조 적용)
  - 편집기: VS Code 또는 텍스트 에디터
  - 주의사항: 경로, API 키 모자이크 처리

#### MCP 테스트 (2개)

- **`mcp-test-success.png`**
  - 내용: MCP 연결 테스트 성공 화면
  - 캡처 범위: 테스트 명령어 + "Connection successful" 메시지

- **`mcp-error-common.png`**
  - 내용: 일반적인 오류 메시지 및 해결 방법
  - 예시: "Bootstrap check_in Permission denied"

#### SpecKit 워크플로우 (2개)

- **`speckit-installation-complete.png`**
  - 내용: SpecKit 설치 완료 화면
  - 캡처 범위: `npm install @github/spec-kit` 성공 메시지

- **`speckit-documents-example.png`**
  - 내용: 생성된 Constitution, Spec, Plan 문서 예시
  - 캡처 방법: 3개 파일을 VS Code 탭으로 나란히 열거나 파일 트리 + 내용 미리보기

#### Copilot 워크북 (2개)

- **`copilot-workbook-exercise-detail.png`**
  - 내용: Exercise 3-4 상세 실행 화면
  - 캡처 범위: 문제 설명 + 코드 작성 + Copilot 지원

- **`copilot-workbook-paper-result.png`**
  - 내용: 논문 작성 지원 결과
  - 캡처 범위: 논문 초안 일부 + AI 제안 사항

### 4.3 Part 3 수동 캡처 대상 (12개 대기)

Part 3의 상세한 스크린샷 목록은 [`v13.0_resources/part3/24-37_screenshot_descriptions.md`](../../v13.0_resources/part3/24-37_screenshot_descriptions.md) 문서를 참조하세요.

**주요 카테고리**:
- 통합 워크플로우 (5개): 도구 간 연결성, 데이터 흐름
- 전공별 시나리오 (5개): 교육학, 생명과학, 컴퓨터공학, 사회학, 음악학 연구 과정
- 연구 관리 (2개): 주간/월간 루틴, 품질 관리 체크리스트

---

## 단계별 캡처 가이드

### 5.1 사전 준비

#### 1단계: 캡처 환경 설정

- **애플리케이션 실행**: VS Code, Terminal, Claude Desktop 등
- **화면 정리**: 불필요한 창 닫기, 알림 끄기 (Do Not Disturb 모드)
- **테마 설정**: 일관된 테마 사용 (Dark 또는 Light, 프로젝트 전체 통일)
- **해상도 확인**: 1920x1080 이상 권장 (Retina 디스플레이의 경우 자동 조정)

#### 2단계: 저장 위치 설정

1. `Cmd + Shift + 5` 누르기
2. **Options** 클릭
3. **Save to** → **Other Location** 선택
4. 프로젝트 폴더 선택: `v13.0_resources/part[1-3]/images/`

**팁**: 한 번 설정하면 이후 캡처에도 동일 위치로 저장됩니다.

### 5.2 VS Code 스크린샷 캡처

#### Step 1: 화면 준비

- VS Code 윈도우를 적절한 크기로 조정 (전체 화면 또는 1920x1080 비율)
- 캡처할 내용이 명확히 보이도록 확대/축소 (`Cmd + +` / `Cmd + -`)
- 불필요한 패널 닫기:
  - Terminal: `Cmd + J` 토글
  - Output: View → Output 패널 닫기
  - Problems: `Cmd + Shift + M` 토글

#### Step 2: 캡처 실행

**전체 윈도우 캡처** (권장):
1. `Cmd + Shift + 4` 누르기
2. `Space` 누르기 (커서가 카메라 아이콘으로 변경)
3. VS Code 윈도우 위로 마우스 이동 (하이라이트 표시)
4. 클릭하여 캡처

**부분 캡처** (특정 영역만):
1. `Cmd + Shift + 4` 누르기
2. 십자선 커서로 드래그하여 영역 선택
3. 마우스 버튼 놓으면 캡처

#### Step 3: 편집 및 주석

1. 우측 하단 썸네일 클릭 (5초 내)
2. Markup 도구 사용:
   - **화살표**: 중요 부분 강조
   - **텍스트 상자**: 설명 추가
   - **도형**: 민감정보 모자이크 (사각형, 불투명도 100%)
3. 편집 완료 후 **Done** 클릭

#### Step 4: 저장 및 검증

- **파일명 변경**: 자동 생성된 이름을 `kebab-case-description.png` 형식으로 변경
  - 예: `Screenshot 2025-11-13 at 14.30.45.png` → `copilot-chat-panel.png`
- **저장 위치 확인**: Finder에서 `v13.0_resources/part1/images/` 경로 확인
- **해상도 확인**: Preview에서 열기 → Tools → Adjust Size → 1920x1080 이상 확인

### 5.3 Terminal 스크린샷 캡처

#### Step 1: 명령어 실행

- Terminal에서 캡처할 명령어 실행:
  ```bash
  node --version
  npm install @srigi/mcp-webpage-screenshot
  ```
- 출력 결과가 완전히 표시될 때까지 대기 (스크롤 완료)

#### Step 2: 화면 정리

- 불필요한 이전 명령어 출력 제거:
  ```bash
  clear
  ```
  또는 위로 스크롤하여 원하는 명령어만 보이도록 조정

- 프롬프트, 명령어, 결과가 모두 보이도록 배치:
  ```
  user@macbook ~ % node --version
  v20.10.0
  user@macbook ~ % 
  ```

#### Step 3: 캡처

**영역 선택 캡처** (권장):
1. `Cmd + Shift + 4` 누르기
2. Terminal 윈도우에서 캡처할 영역 드래그
3. 프롬프트 + 명령어 + 결과 포함

**전체 윈도우 캡처**:
1. `Cmd + Shift + 4` → `Space`
2. Terminal 윈도우 클릭

#### Step 4: 편집

- **민감정보 모자이크**: 
  - 사용자명: `user@macbook` → 검은색 사각형으로 가리기
  - 경로: `/Users/truestone/` → 모자이크 처리
- **중요한 출력 하이라이트**: 
  - 버전 번호, 성공 메시지에 화살표 추가

### 5.4 Claude Desktop 설정 화면 캡처

#### Step 1: 설정 열기

1. Claude Desktop 실행
2. **Settings** (⚙️ 아이콘) 클릭
3. **Developer** 탭 선택
4. **MCP Servers** 섹션 이동

#### Step 2: 화면 준비

- 설정 내용이 명확히 보이도록 스크롤
- JSON 설정 파일이 있다면:
  - VS Code 또는 텍스트 에디터에서 열기
  - 구문 강조 (Syntax Highlighting) 적용 확인
  - 들여쓰기 (Indentation) 정렬

#### Step 3: 캡처

- `Cmd + Shift + 4` 사용
- 설정 패널 전체 또는 JSON 코드 영역 선택

#### Step 4: 민감정보 처리

- **모자이크 대상**:
  - API 키: `"apiKey": "sk-..."` → `"apiKey": "••••••••"`
  - 토큰: `"token": "ghp_..."` → 모자이크
  - 경로: `"/Users/truestone/"` → `"/Users/[username]/"`
- **예시 값으로 대체 가능**: 실제 키 대신 `YOUR_API_KEY_HERE` 텍스트 삽입

### 5.5 Copilot 기능 시연 캡처

#### Step 1: 시나리오 준비

- **실제 사용 사례 설정**:
  - 연구 계획서 작성 (Markdown)
  - 데이터 분석 코드 작성 (Python)
  - 논문 초록 작성 (Text)
- **샘플 데이터 준비**: 실제 연구 내용 또는 가상의 연구 주제

#### Step 2: Copilot 기능 활성화

**Inline completion**:
- 코드 또는 텍스트 타이핑 시작
- 제안 나타날 때까지 대기 (회색 텍스트)
- `Tab` 누르지 말고 캡처

**Chat**:
1. `Cmd + I` (Quick Chat) 또는 `Cmd + Shift + I` (Chat 패널)
2. 질문 입력: "연구 계획서의 목차 구조를 제안해주세요"
3. AI 응답 완료 대기

**Agent mode**:
1. Chat 패널 열기
2. 상단의 Mode picker 클릭 (드롭다운 펼침)
3. `@workspace`, `@vscode`, `@terminal` 등 옵션 표시 시 캡처

#### Step 3: 캡처 타이밍

- **Inline completion**: 회색 제안 텍스트가 표시될 때 즉시
  - **주의**: 제안은 몇 초 후 사라질 수 있으므로 타이머 사용 권장
  - `Cmd + Shift + 5` → Options → Timer → 5 seconds

- **Chat**: AI 응답이 완료된 후
  - 응답이 길면 스크롤하여 여러 장 캡처

- **Agent mode**: Mode picker가 펼쳐진 상태

#### Step 4: 주석 추가

- **제안 텍스트 강조**: 화살표로 회색 제안 부분 표시
- **힌트 추가**: "Tab to accept" 텍스트 상자 삽입
- **기능 설명**: "Agent mode allows querying workspace context" 등 주석

---

## 품질 체크리스트

### 6.1 기술적 요구사항

- [ ] **해상도**: 1920x1080 이상
  - 확인 방법: Preview → Tools → Adjust Size
  - Retina 디스플레이의 경우 2배 해상도 (3840x2160) 자동 적용

- [ ] **포맷**: PNG (투명 배경 필요 시) 또는 JPG (일반)
  - PNG 권장: VS Code, Terminal 등 UI 캡처
  - JPG 사용 가능: 사진 또는 복잡한 이미지

- [ ] **파일 크기**: 2MB 이하
  - 확인 방법: Finder → Get Info (`Cmd + I`) 또는 Preview → Tools → Show Inspector
  - 압축 필요 시: [TinyPNG](https://tinypng.com/) 또는 ImageOptim 사용

- [ ] **명명 규칙**: `kebab-case-description.png`
  - 예: `copilot-chat-panel.png`, `mcp-installation-node-version.png`
  - 소문자, 하이픈으로 단어 구분, 확장자 포함

- [ ] **저장 위치**: `v13.0_resources/part[1-3]/images/`
  - Part 1: `v13.0_resources/part1/images/`
  - Part 2: `v13.0_resources/part2/images/`
  - Part 3: `v13.0_resources/part3/images/`

### 6.2 시각적 품질

- [ ] **텍스트 가독성**: 모든 텍스트가 선명하게 보임
  - 확대하여 확인: 최소 12pt 폰트 크기
  - 흐릿한 경우 재캡처 (Retina 해상도 확인)

- [ ] **색상 대비**: 충분한 대비로 내용 구분 가능
  - Dark 테마: 흰색/밝은 회색 텍스트 선명하게
  - Light 테마: 검은색/어두운 회색 텍스트 명확하게

- [ ] **강조 표시**: 중요 부분에 화살표, 텍스트 상자, 하이라이트 추가
  - 화살표: 빨간색 또는 주황색 (눈에 띄는 색상)
  - 텍스트 상자: 배경 흰색/노란색, 테두리 검은색
  - 하이라이트: 형광펜 효과 (투명도 50%)

- [ ] **일관성**: 동일한 테마 (Dark/Light) 사용
  - 프로젝트 전체 스크린샷 일관성 유지
  - VS Code 테마: 예) "Dark+ (default dark)" 고정

- [ ] **정렬**: 캡처 영역이 정렬되고 균형잡힘
  - 윈도우 테두리 포함 여부 일관성
  - 여백 최소화하되 콘텐츠 잘리지 않도록

### 6.3 내용 정확성

- [ ] **민감정보 처리**: 개인정보, API 키, 경로 등 모자이크
  - 사용자명, 이메일, 학교명
  - API 키, 토큰, 비밀번호
  - 절대 경로 (`/Users/username/`)
  - IP 주소, 포트 번호 (필요 시)

- [ ] **오류 없음**: 오타, 잘못된 명령어 없음
  - 명령어 재확인: `node --version` (철자 정확)
  - 출력 결과 검증: 예상 결과와 일치

- [ ] **컨텍스트 명확**: 캡처 내용이 문서 설명과 일치
  - 스크린샷 설명 문서의 요구사항 재확인
  - 캡처 범위 적절: 너무 넓거나 좁지 않게

- [ ] **버전 일치**: 최신 버전의 도구 사용 (2025년 기준)
  - VS Code: 1.85+ (2025년 최신)
  - Node.js: v20+ LTS
  - Copilot: 최신 확장 버전

### 6.4 접근성

- [ ] **대체 텍스트**: 문서에 이미지 설명 추가
  - Markdown: `![Copilot Chat 패널에서 Agent mode 선택](copilot-agent-mode-indicator.png)`
  - 설명: 이미지 내용을 텍스트로 명확히 표현

- [ ] **색맹 고려**: 색상만으로 정보 전달하지 않음
  - 화살표 + 텍스트 라벨 함께 사용
  - 색상 대비 확인: WebAIM Contrast Checker 사용

- [ ] **텍스트 크기**: 최소 14pt 이상
  - 작은 텍스트는 확대하여 캡처
  - VS Code 폰트 크기: 14-16pt 권장

---

## 트러블슈팅

### 7.1 스크린샷이 흐릿하게 보임

**원인**: Retina 디스플레이에서 저해상도 캡처

**해결**:
1. `Cmd + Shift + 5` → **Options** → **Show Mouse Pointer** 체크
2. Retina 해상도로 캡처 (자동 2배 해상도)
3. Preview에서 확인: Tools → Adjust Size → 실제 해상도 확인 (예: 3840x2160)

**확인**: 
- 캡처 후 100% 확대하여 텍스트 선명도 확인
- 필요 시 재캡처

### 7.2 파일 크기가 너무 큼 (2MB 초과)

**원인**: 고해상도 또는 압축되지 않은 PNG

**해결**:
- **TinyPNG** 사용: https://tinypng.com/
  1. 사이트 접속
  2. 이미지 업로드 (드래그 앤 드롭)
  3. 압축 완료 후 다운로드 (평균 70% 크기 감소)

- **ImageOptim** 사용 (macOS 앱):
  1. 다운로드: https://imageoptim.com/
  2. 앱에 이미지 드래그 앤 드롭
  3. 자동 압축 (무손실 압축)

**대안**: JPG 포맷으로 저장
- Preview에서 열기 → File → Export → Format: JPEG, Quality: 90%

### 7.3 민감정보 모자이크 처리 방법

**도구**: Preview Markup 도구

**단계**:
1. Preview에서 이미지 열기
2. **Show Markup Toolbar** 아이콘 클릭 (또는 `Cmd + Shift + A`)
3. **도형 (사각형)** 선택
4. 모자이크할 영역에 사각형 그리기
5. **불투명도 100%** 설정 (투명도 슬라이더 최대)
6. **색상**: 검은색 또는 회색 선택
7. 저장: `Cmd + S`

**확인**: 모자이크 아래 텍스트가 완전히 가려졌는지 확대하여 확인

**팁**: 
- 여러 영역 모자이크 시 복사/붙여넣기 (`Cmd + C`, `Cmd + V`) 사용
- 일관된 색상 사용 (모든 모자이크 동일한 검은색)

### 7.4 Copilot 제안이 캡처되지 않음

**원인**: 제안이 사라지기 전에 캡처하지 못함

**해결**:
1. `Cmd + Shift + 5` 누르기
2. **Options** → **Timer** → **5 seconds** 선택
3. 캡처 영역 선택 후 **Capture** 클릭
4. 5초 카운트다운 동안 Copilot 제안 나타나도록 타이핑
5. 자동 캡처

**대안**: 화면 녹화 후 프레임 추출
1. `Cmd + Shift + 5` → **Record Selected Portion** 선택
2. 제안 나타나는 과정 녹화 (5-10초)
3. QuickTime Player에서 열기
4. View → Show Movie Inspector → 원하는 프레임으로 이동
5. Edit → Copy → Preview에 붙여넣기 → 저장

### 7.5 Terminal 출력이 잘림

**원인**: Terminal 윈도우 크기가 작음

**해결**:
- **Terminal 윈도우 확대**: 드래그하여 넓게 조정
- **폰트 크기 축소**: Terminal → Preferences → Profiles → Text → Font Size (12pt → 10pt)
- **스크롤**: 출력이 긴 경우 위로 스크롤하여 시작 부분부터 캡처

**대안**: 여러 장으로 나누어 캡처 후 이어붙이기
1. 상단 부분 캡처 (명령어 + 시작 출력)
2. 중간 부분 캡처 (계속 출력)
3. 하단 부분 캡처 (마지막 출력 + 프롬프트)
4. Preview 또는 이미지 편집 도구로 세로 결합

### 7.6 저장 위치를 찾을 수 없음

**원인**: 기본 저장 위치가 데스크톱으로 설정됨

**해결**:
1. `Cmd + Shift + 5` 누르기
2. **Options** → **Save to** → **Other Location** 선택
3. Finder에서 프로젝트 폴더 찾아 선택: `v13.0_resources/part1/images/`
4. **Choose** 클릭

**확인**: 
- 캡처 후 썸네일 클릭 → **Show in Finder** (`Cmd + R`)
- Finder에서 파일 경로 확인 (상단 경로 바)

**팁**: 
- 한 번 설정하면 다음 캡처부터 동일 위치로 저장
- 프로젝트 폴더를 Dock에 추가하여 빠르게 접근

---

## 관련 문서

### 8.1 내부 링크

**스크린샷 가이드 문서**:
- [Part 1 스크린샷 가이드](../../v13.0_resources/11_screenshot_descriptions.md): 26개 스크린샷 상세 설명
- [Part 2 스크린샷 가이드](../../v13.0_resources/part2/12_screenshot_descriptions.md): 15개 스크린샷 상세 설명
- [Part 3 스크린샷 가이드](../../v13.0_resources/part3/24-37_screenshot_descriptions.md): 20개 스크린샷 상세 설명

**MCP 자동화 관련**:
- [Cline MCP 스크린샷 설정](06-mcp-installation/cline-screenshot-mcp-setup.md): MCP 서버 설치 및 사용법
- [스크린샷 체크리스트](06-mcp-installation/screenshots-checklist.md): 전체 진행 상황 추적

### 8.2 외부 참조

**macOS 공식 가이드**:
- [macOS 스크린샷 공식 가이드](https://support.apple.com/guide/mac-help/take-a-screenshot-mh26782/mac): Apple 공식 문서

**이미지 최적화 도구**:
- [TinyPNG](https://tinypng.com/): 온라인 이미지 압축 (무료)
- [ImageOptim](https://imageoptim.com/): macOS 이미지 최적화 앱 (무료)

**접근성 도구**:
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): 색상 대비 확인

---

## 부록: 빠른 참조 카드

### 9.1 macOS 스크린샷 단축키

| 단축키 | 기능 | 용도 |
|--------|------|------|
| `Cmd + Shift + 3` | 전체 화면 캡처 | 모든 모니터 캡처 |
| `Cmd + Shift + 4` | 영역 선택 캡처 | 드래그하여 영역 선택 |
| `Cmd + Shift + 4` → `Space` | 윈도우 캡처 | 특정 윈도우만 캡처 |
| `Cmd + Shift + 5` | 스크린샷 도구 | 고급 옵션 (타이머, 저장 위치) |

### 9.2 저장 위치 빠른 변경

1. `Cmd + Shift + 5`
2. **Options** → **Save to** → **Other Location**
3. 프로젝트 폴더 선택: `v13.0_resources/part[1-3]/images/`
4. **Choose** 클릭

### 9.3 편집 도구 빠른 접근

- 캡처 후 **썸네일 클릭** (5초 내)
- Markup 도구 사용:
  - 화살표: 강조
  - 텍스트 상자: 설명
  - 도형: 모자이크

### 9.4 품질 체크 빠른 확인

1. **Preview**에서 이미지 열기
2. **Tools** → **Adjust Size** → 해상도 확인 (1920x1080 이상)
3. **Tools** → **Show Inspector** → 파일 크기 확인 (2MB 이하)
4. 100% 확대하여 텍스트 선명도 확인
5. 민감정보 모자이크 확인

### 9.5 자주 사용하는 캡처 시나리오

| 대상 | 권장 방법 | 타이머 | 주의사항 |
|------|-----------|--------|----------|
| **VS Code 전체** | `Cmd+Shift+4` → `Space` → 클릭 | 없음 | 그림자 포함 |
| **VS Code 부분** | `Cmd+Shift+4` → 드래그 | 없음 | 정확한 영역 선택 |
| **Terminal** | `Cmd+Shift+4` → 드래그 | 없음 | 민감정보 주의 |
| **Copilot 제안** | `Cmd+Shift+5` | 5초 | 제안 나타날 때까지 대기 |
| **Claude Desktop** | `Cmd+Shift+4` → 드래그 | 없음 | API 키 모자이크 |
| **메뉴 펼침** | `Cmd+Shift+5` | 5초 | 타이머 설정 필수 |

---

**Version**: v13.0 Manual Screenshot Guide  
**Last Updated**: 2025-11-13  
**Author**: [강사/조교 이름]  
**Next Review**: v13.1 업데이트 시

---

## 📞 문의사항

스크린샷 캡처 과정에서 문제가 발생하면:
1. 이 가이드의 [트러블슈팅](#트러블슈팅) 섹션 참조
2. [스크린샷 체크리스트](06-mcp-installation/screenshots-checklist.md)의 진행 상황 확인
3. 조교 또는 강사에게 문의 (이메일/슬랙)

**성공적인 스크린샷 캡처를 기원합니다!** 🎉
