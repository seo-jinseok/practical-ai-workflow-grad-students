# MCP 설치 시연 스크린샷 체크리스트

**목적**: 시연 백업용 스크린샷 목록 및 캡처 가이드  
**저장 위치**: `demo-files/backup/screenshots/mcp-installation/`  
**해상도**: 1920x1080 이상  
**형식**: PNG  

## 📸 스크린샷 목록 (12개)

### 필수 스크린샷 (8개)

#### Claude Desktop 관련 (3개)
- [ ] `mcp-01-claude-desktop-main.png`
  - 내용: Claude Desktop 메인 화면
  - 강조: 새 대화 버튼
  - 용도: Step 1 (Claude 확인)

- [ ] `mcp-02-claude-new-chat.png`
  - 내용: 새 대화 창
  - 강조: 입력 필드
  - 용도: Step 1 (대화 시작)

- [ ] `mcp-03-claude-mcp-active.png`
  - 내용: MCP 서버 활성화 표시
  - 강조: 설정 메뉴 또는 서버 목록
  - 용도: Step 3 (설치 확인)

#### 설정 파일 편집 (3개)
- [ ] `mcp-04-config-file-location.png`
  - 내용: Finder/탐색기에서 설정 파일 위치
  - 강조: 파일 경로
  - 용도: Step 2 (파일 찾기)

- [ ] `mcp-05-config-file-empty.png`
  - 내용: 빈 설정 파일 또는 기본 설정
  - 강조: JSON 구조
  - 용도: Step 2 (편집 전)

- [ ] `mcp-06-config-file-edited.png`
  - 내용: task-master-ai 추가된 설정 파일
  - 강조: 추가된 부분
  - 용도: Step 2 (편집 후)

#### 테스트 및 확인 (2개)
- [ ] `mcp-07-test-prompt.png`
  - 내용: "task-master-ai를 사용할 수 있나요?" 프롬프트
  - 강조: 프롬프트 텍스트
  - 용도: Step 3 (테스트)

- [ ] `mcp-08-test-response.png`
  - 내용: AI의 긍정 응답
  - 강조: "사용할 수 있습니다" 부분
  - 용도: Step 3 (성공 확인)

### 선택적 스크린샷 (4개)

#### 사용 예시 (2개)
- [ ] `mcp-09-project-init-prompt.png`
  - 내용: 프로젝트 초기화 프롬프트
  - 용도: Step 4 (사용 예시)

- [ ] `mcp-10-project-init-response.png`
  - 내용: AI의 작업 제안 응답
  - 용도: Step 4 (결과 확인)

#### 트러블슈팅 (2개)
- [ ] `mcp-11-error-not-found.png`
  - 내용: "찾을 수 없습니다" 오류 메시지
  - 용도: 트러블슈팅 설명

- [ ] `mcp-12-json-syntax-error.png`
  - 내용: VS Code에서 JSON 문법 오류 (빨간 밑줄)
  - 용도: 트러블슈팅 설명

## 📸 캡처 가이드라인

### 기술 요구사항
- **해상도**: 최소 1920x1080 (Retina/HiDPI 권장)
- **포맷**: PNG (투명 배경 불필요)
- **파일 크기**: 최대 2MB (압축 필요 시 TinyPNG)
- **명명 규칙**: `mcp-[번호]-[설명].png`

### 시각적 가이드라인
- **강조**: 빨간 박스 또는 화살표로 중요 부분 표시
- **민감정보**: 개인정보, API 키 등 모자이크 처리
- **일관성**: 동일한 테마 (Dark/Light) 사용
- **가독성**: 텍스트가 선명하게 보이도록

### 캡처 도구
- **macOS**: Cmd+Shift+4 (영역 선택)
- **Windows**: Snipping Tool, Greenshot
- **편집**: Skitch, Annotate, Photoshop

### 저장 위치
```
demo-files/backup/screenshots/mcp-installation/
├── mcp-01-claude-desktop-main.png
├── mcp-02-claude-new-chat.png
├── mcp-03-claude-mcp-active.png
├── mcp-04-config-file-location.png
├── mcp-05-config-file-empty.png
├── mcp-06-config-file-edited.png
├── mcp-07-test-prompt.png
├── mcp-08-test-response.png
├── mcp-09-project-init-prompt.png
├── mcp-10-project-init-response.png
├── mcp-11-error-not-found.png
└── mcp-12-json-syntax-error.png
```

## ✅ 캡처 진행 상황

- [ ] **필수 스크린샷** (8개)
- [ ] **선택적 스크린샷** (4개)
- [ ] **모든 이미지 품질 확인**
- [ ] **파일명 일관성 확인**
- [ ] **백업 슬라이드에 삽입 테스트**

### 우선순위
1. 🔴 **필수** (Step 1-3): 8개
2. 🟡 **중요** (Step 4): 2개
3. 🟢 **선택** (트러블슈팅): 2개

## 🎯 각 스크린샷 상세 가이드

### mcp-01-claude-desktop-main.png
- **화면**: Claude Desktop 메인 화면
- **강조**: 새 대화 버튼 (빨간 박스)
- **캡처 시기**: 시연 시작 전
- **용도**: "Claude Desktop이 이미 설치되어 있다고 가정" 설명

### mcp-02-claude-new-chat.png
- **화면**: 새 대화 창 열림
- **강조**: 입력 필드 (빨간 박스)
- **캡처 시기**: 새 대화 클릭 후
- **용도**: "새 대화를 시작하겠습니다" 설명

### mcp-03-claude-mcp-active.png
- **화면**: MCP 서버가 활성화된 상태
- **강조**: 설정 메뉴나 서버 목록 (화살표)
- **캡처 시기**: MCP 설치 완료 후
- **용도**: "MCP가 정상 작동하는 것을 확인" 설명

### mcp-04-config-file-location.png
- **화면**: Finder에서 설정 파일 위치
- **강조**: 파일 경로 (빨간 박스)
- **캡처 시기**: 설정 파일 찾기 시
- **용도**: "설정 파일은 여기 있습니다" 설명

### mcp-05-config-file-empty.png
- **화면**: 빈 설정 파일 내용
- **강조**: JSON 구조 (빨간 박스)
- **캡처 시기**: 편집 전
- **용도**: "여기에 설정을 추가하겠습니다" 설명

### mcp-06-config-file-edited.png
- **화면**: task-master-ai 추가된 설정
- **강조**: 추가된 부분 (빨간 박스)
- **캡처 시기**: 편집 완료 후
- **용도**: "설정을 추가했습니다" 설명

### mcp-07-test-prompt.png
- **화면**: 테스트 프롬프트 입력 화면
- **강조**: "task-master-ai를 사용할 수 있나요?" (빨간 박스)
- **캡처 시기**: 프롬프트 입력 후
- **용도**: "MCP가 작동하는지 확인하겠습니다" 설명

### mcp-08-test-response.png
- **화면**: AI의 긍정적 응답
- **강조**: "사용할 수 있습니다" 부분 (빨간 박스)
- **캡처 시기**: AI 응답 후
- **용도**: "성공적으로 설치되었습니다" 설명

## 🚨 긴급 상황 스크린샷

### 설치 실패 시 (mcp-11-error-not-found.png)
- **화면**: "task-master-ai를 찾을 수 없습니다" 오류
- **용도**: "기술적 문제가 발생할 수 있습니다" 설명
- **대안**: "설치 가이드를 자료로 제공합니다"

### JSON 문법 오류 시 (mcp-12-json-syntax-error.png)
- **화면**: VS Code에서 빨간 밑줄 표시
- **용도**: "JSON 문법에 주의해야 합니다" 설명
- **대안**: "복사-붙여넣기를 권장합니다"

## 📊 품질 관리 체크리스트

### 각 파일 생성 후
- [ ] 해상도 1920x1080 이상 확인
- [ ] 텍스트가 선명하게 보임
- [ ] 강조 부분이 명확히 표시됨
- [ ] 파일명 규칙 준수
- [ ] 용도에 맞는 내용

### 전체 배치 후
- [ ] 백업 슬라이드에 삽입 확인
- [ ] 프로젝트 공유 시 포함 확인
- [ ] 로컬 백업과 동기화 확인
