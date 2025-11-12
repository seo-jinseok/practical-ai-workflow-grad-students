# 전체 프로젝트 스크린샷 마스터 체크리스트

**목적**: v13.0 프로젝트 전체 스크린샷 생성 진행 상황 추적  
**저장 위치**: `v13.0_resources/images/`  
**해상도**: 1920x1080 이상  
**형식**: PNG  

## 개요

- **전체 스크린샷 수**: Part 1 (26개), Part 2 (추정 15개), Part 3 (추정 20개)
- **MCP 자동화 가능**: 약 15개 (웹페이지 기반)
- **수동 캡처 필요**: 약 46개 (데스크톱 애플리케이션, 터미널 등)

## Part 1 체크리스트 (26개)

### MCP 자동화 완료 (3개)
- [x] GitHub Education Pack 메인 페이지
- [x] Copilot Plans 비교 페이지
- [x] VS Code 다운로드 페이지

### 수동 캡처 필요 - GitHub/Copilot (2개)
- [ ] 학생 인증 폼 (민감정보 모자이크 필요)
- [ ] Copilot Pro 활성화 상태

### 수동 캡처 필요 - VS Code 설정 (3개)
- [ ] VS Code Extensions 마켓플레이스
- [ ] Copilot 확장 설치 완료
- [ ] VS Code 폴더 구조 예시

### 수동 캡처 필요 - Copilot 기능 (5개)
- [ ] Inline Completion
- [ ] Copilot Chat 패널
- [ ] Model Picker
- [ ] Markdown 구조 제안
- [ ] Chat 컨텍스트 제공 예시

### 수동 캡처 필요 - 2025 신기능 (5개)
- [ ] Agent Mode 표시
- [ ] Custom Instructions 파일
- [ ] AGENTS.md 파일
- [ ] Vision 기능 (이미지 첨부)
- [ ] Next Edit Suggestions

### 수동 캡처 필요 - MCP (2개)
- [ ] MCP 개념 다이어그램 (직접 제작 또는 공식 다이어그램)
- [ ] Claude Desktop MCP 설정

### 수동 캡처 필요 - 문제 해결 (3개)
- [ ] Copilot 비활성화 상태
- [ ] 로그인 프롬프트
- [ ] 제안 없음 상태

### 수동 캡처 필요 - 실습 예시 (3개)
- [ ] 연구 컨텍스트 작성 중
- [ ] Markdown 템플릿 사용
- [ ] Chat으로 문헌 키워드 생성

## Part 2 체크리스트 (추정 15개)

### MCP 자동화 완료 (2개)
- [x] [MCP 프로토콜 소개 페이지](https://modelcontextprotocol.io/)
  - ✅ **생성 완료**: 2025-11-12
  - **파일명**: `mcp-protocol-intro.png`
  - **저장 위치**: `v13.0_resources/part2/images/`
- [x] [SpecKit 리포지토리](https://github.com/github/spec-kit)
  - ✅ **생성 완료**: 2025-11-12
  - **파일명**: `speckit-repository.png`
  - **저장 위치**: `v13.0_resources/part2/images/`

### 수동 캡처 필요 - MCP 설치 (4개)
- [ ] Node.js 설치 확인 터미널 화면
- [ ] MCP 서버 설치 완료 화면
- [ ] Claude Desktop MCP 연결 확인
- [ ] JSON 설정 파일 내용

### 수동 캡처 필요 - SpecKit 워크플로우 (3개)
- [ ] SpecKit 설치 완료
- [ ] 7단계 워크플로우 실행
- [ ] 생성된 문서 예시 (Constitution, Spec, Plan)

### 수동 캡처 필요 - Copilot 워크북 (2개)
- [ ] Exercise 3 코드 분석 화면
- [ ] Exercise 4 논문 작성 결과

### 수동 캡처 필요 - 문제 해결 (2개)
- [ ] 일반적 오류 상황 및 해결 방법
- [ ] 설정 파일 검증 과정

## Part 3 체크리스트 (추정 20개)
- [ ] Elicit 메인 인터페이스 (MCP 자동화 가능)
- [ ] Perplexity 메인 인터페이스 (MCP 자동화 가능)
- [ ] NotebookLM 메인 인터페이스 (MCP 자동화 가능)
- [ ] Consensus 메인 인터페이스 (MCP 자동화 가능)
- [ ] Scite 메인 인터페이스 (MCP 자동화 가능)
- [ ] ResearchRabbit, Connected Papers, Semantic Scholar (MCP 자동화 가능)
- [ ] 기타 수동 캡처 항목 (Part 3 작업 시 추가)

## 📊 전체 진행 상황

- **전체**: 5/61 완료 (8.2%)
- **Part 1**: 3/26 완료 (11.5%)
- **Part 2**: 2/15 완료 (13.3%)
- **Part 3**: 0/20 완료 (0%)

## 🤖 MCP 자동화 현황

- **완료**: 5/15 (33.3%)
- **대기**: 10/15 (66.7%)

### 완료 내역
- ✅ Part 1: 3/3 (100%)
- ✅ Part 2: 2/2 (100%)
- ⏳ Part 3: 0/10 (0%)

## 👤 수동 캡처 현황

- **완료**: 0/46 (0%)
- **대기**: 46/46 (100%)

## 다음 단계

### 우선순위 1: Part 3 MCP 자동화 (10개)
- Elicit, Perplexity, NotebookLM 등 연구 도구 웹페이지
- 예상 소요 시간: 약 10분

### 우선순위 2: Part 2 수동 캡처 (13개)
- MCP 설치 과정, SpecKit 워크플로우, Copilot 워크북
- 예상 소요 시간: 약 30-40분

### 우선순위 3: Part 1 수동 캡처 (23개)
- VS Code 설정, Copilot 기능, 실습 예시
- 예상 소요 시간: 약 60-90분

## 참고 문서

- `v13.0_resources/11_screenshot_descriptions.md`: Part 1 상세 가이드
- `v13.0_resources/part2/12_screenshot_descriptions.md`: Part 2 상세 가이드
- `v13.0_resources/part3/24-37_screenshot_descriptions.md`: Part 3 상세 가이드
## 📅 완료 로그

### 2025-11-10 (Part 1)
- ✅ Part 1 MCP 자동화 완료 (3개)
  - GitHub Education Pack, Copilot Plans, VS Code 다운로드

### 2025-11-12 (Part 2)
- ✅ Part 2 MCP 자동화 완료 (2개)
  - MCP 프로토콜 소개, SpecKit 리포지토리

## 참고 문서

- `v13.0_resources/11_screenshot_descriptions.md`: Part 1 상세 가이드
- `v13.0_resources/part2/12_screenshot_descriptions.md`: Part 2 상세 가이드
- `v13.0_resources/part3/24-37_screenshot_descriptions.md`: Part 3 상세 가이드
- `Context_and_Planning/demo-files/06-mcp-installation/part1-screenshot-generation-prompts.md`: Part 1 MCP 프롬프트
- `Context_and_Planning/demo-files/06-mcp-installation/part2-screenshot-generation-prompts.md`: Part 2 MCP 프롬프트
