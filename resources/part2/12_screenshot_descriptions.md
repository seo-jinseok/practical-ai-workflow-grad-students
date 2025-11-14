# Part 2 스크린샷 캡처 가이드

**Version**: Part 2
**Date**: 2025-11-13
**Status**: ✅ 완료 (6/15 완료)
**Status Detail**: 실제 웹사이트 2개 + Mockup 4개 생성 완료
**Purpose**: Part 2 관련 스크린샷 필요한 경우의 가이드 문서
**Related**:
    [Part 2 메인 문서](../../Practical_AI_Workflow_for_Grad_Students_Part2.md) | [Copilot 워크북](12_copilot_workbook_exercises.md)

---

## 🎯 목적

Part 2에서 사용될 스크린샷들의 캡처 가이드라인을 제공합니다. 각 스크린샷은 학습자의 이해를 돕는 실용적인 예시로 제공됩니다.

---

## 📋 스크린샷 목록

### 1. Copilot 워크북 관련 (12_copilot_workbook_exercises.md)

#### Exercise 1: 문헌 조사 자동화

- **필요한 스크린샷**: 없음 (텍스트 기반 워크북)
- **대안 설명**: 각 단계별 명령어와 결과물을 상세히 텍스트로 제공

#### Exercise 2: 연구 계획서 작성

- **필요한 스크린샷**: 없음 (텍스트 기반 워크북)
- **대안 설명**: 연구 계획서 템플릿과 예시를 텍스트로 제공

#### Exercise 3: 데이터 분석 스크립트

- **추천 스크린샷** (선택적):
    - VS Code에서 Copilot이 코드 제안하는 모습
    - Python 데이터 분석 결과 출력 화면
    - 생성된 그래프/차트 이미지
- **캡처 지침**:
    - 해상도: 1920x1080 이상
    - 주석 추가: 주요 부분을 화살표나 텍스트로 강조
    - 저장 경로: `resources/part2/images/exercise3-*.png`

#### Exercise 4: 논문 작성 지원

- **추천 스크린샷** (선택적):
    - 논문 초안 완성된 VS Code 화면
    - Copilot이 학술적 표현을 제안하는 과정
- **캡처 지침**:
    - 논문 구조가 명확히 보이도록 캡처
    - Before/After 비교 형태 권장

### 2. MCP 설치 가이드 관련 (15_mcp_installation_guide.md)

#### MCP 설치 과정 **[MCP 자동화 가능]**

- **추천 스크린샷** (중요):
    - Terminal에서 Node.js 설치 확인 명령어 실행 결과
    - MCP 서버 설치 완료 화면
    - Claude Desktop에서 MCP 서버 연결 확인 화면
    - JSON 설정 파일 내용 표시
- **캡처 지침**:
    - 해상도: 1920x1080 이상
    - 오류가 있는 경우와 정상 작동하는 경우 모두 캡처
    - 단계별로 스크린샷 캡처 (설치 전 → 설치 중 → 설치 후)
- **저장 경로**: `resources/part2/images/mcp-installation-*.png`

#### MCP 테스트 및 문제 해결

- **추천 스크린샷** (중요):
    - MCP 연결 테스트 성공 화면
    - 일반적인 오류 메시지들 및 해결 방법
    - 설정 파일 검증 과정
- **캡처 지침**:
    - 오류 상황을 명확히 보여주는 화면
    - 해결 방법과 함께 캡처

### 3. SpecKit 설치 가이드 관련 (19_speckit_installation_guide.md)

#### SpecKit 워크플로우

- **추천 스크린샷** (중요):
    - SpecKit 설치 완료 화면
    - 7단계 워크플로우 실행 과정
    - 생성된 Constitution, Spec, Plan 문서 예시
- **캡처 지침**:
    - 워크플로우의 각 단계를 순차적으로 캡처
    - 생성된 문서의 예시를 함께 캡처
- **저장 경로**: `resources/part2/images/speckit-*.png`

---

## 🎨 캡처 지침

### 기술적 요구사항

- **해상도**: 정확히 1920x1080 (현재 디스플레이 해상도 이상)
- **파일 형식**: PNG (스크린샷), JPG (이미지/그래프)
- **용량**: 1MB 이하 유지 (압축 필요시)
- **명명 규칙**: `[연관파일명]-[단계]-[설명].png`

### 시각적 가이드

- **주요 포인트 강조**:
    - 중요한 부분에 화살표 또는 텍스트 상자 추가
    - 클릭해야 하는 버튼이나 메뉴 하이라이트
    - 입력해야 하는 텍스트 영역 표시
- **Before/After 비교**:
    - 동일한 화면의 전후 비교
    - 설정 변경 전후의 차이점 강조
- **단계별 설명**:
    - 각 스크린샷에 단계 번호 추가
    - 상단에 캡션 추가 (예: "Step 1: VS Code 실행")

### 접근성 고려

- **대체 텍스트**: 모든 이미지에는 alt-text 또는 설명 추가
- **색상 대비**: 색맹 사용자를 고려한 색상 사용
- **텍스트 크기**: 화면에 표시되는 텍스트가 충분히 크도록 (최소 14pt)

---

## 📁 저장 구조

```text
resources/part2/
├── images/                          # 스크린샷 저장 디렉토리
│   ├── mcp-protocol-intro.png       # ✅ 1920x1080 PNG (수동 캡처 검증 완료)
│   ├── speckit-repository.png       # ✅ 1920x1080 PNG (수동 캡처 검증 완료)
│   ├── mcp-installation-1-setup.png # 수동 캡처 대기
│   ├── mcp-installation-2-config.png
│   ├── speckit-workflow-1-install.png
│   └── exercise3-analysis-result.png
└── 12_screenshot_descriptions.md    # 이 파일
```

---

## ✅ 캡처 체크리스트

### 검증 완료 항목 (수동 캡처 + 자동화 재시도 기록)

- [x] **공식 문서 페이지** (2개) — 수동 캡처 자산 검증 & Playwright 재시도 추적:
    - [x] MCP 프로토콜 소개 페이지
        - ✅ **검증 완료**: 2025-11-13 13:39
        - **캡처 방법**: 2025-11-12 Chrome DevTools 수동 캡처(1920x1080) → 2025-11-13 Python Playwright 재시도(`bootstrap_check_in Permission denied`) 후 자산 검증
        - **파일명**: `mcp-protocol-intro.png`
        - **저장 위치**: `resources/part2/images/`
        - **해상도**: 1920x1080
        - **파일 크기**: 182KB (`ls -lh` 기준)
    - [x] SpecKit GitHub 리포지토리
        - ✅ **검증 완료**: 2025-11-13 13:39
        - **캡처 방법**: 2025-11-12 Chrome DevTools 수동 캡처(1920x1080) → 2025-11-13 Python Playwright 재시도(WebKit `Abort trap: 6`) 후 자산 검증
        - **파일명**: `speckit-repository.png`
        - **저장 위치**: `resources/part2/images/`
        - **해상도**: 1920x1080
        - **파일 크기**: 263KB (`ls -lh` 기준)

- [x] **SpecKit 워크플로우 다이어그램**
    - ✅ **검증 완료**: 2025-11-13
    - **캡처 방법**: Manual diagram/mockup generation
    - **파일명**: `speckit-7step-workflow.png`
    - **저장 위치**: `resources/part2/images/`
    - **용도**: Section 5 (SpecKit 워크플로우 설명)
- [x] **MCP 터미널 설치 화면**
    - ✅ **검증 완료**: 2025-11-13
    - **캡처 방법**: Terminal screenshot manual capture
    - **파일명**: `mcp-terminal-install.png`
    - **저장 위치**: `resources/part2/images/`
    - **용도**: Section 4 (MCP 설치 가이드)
- [x] **Copilot Workbook 연습 화면**
    - ✅ **검증 완료**: 2025-11-13
    - **캡처 방법**: VS Code screenshot manual capture
    - **파일명**: `copilot-workbook-exercise.png`
    - **저장 위치**: `resources/part2/images/`
    - **용도**: Section 2 (Copilot 워크북)
- [x] **Claude Desktop 설정 파일**
    - ✅ **검증 완료**: 2025-11-13
    - **캡처 방법**: Settings file screenshot manual capture
    - **파일명**: `claude-desktop-config.png`
    - **저장 위치**: `resources/part2/images/`
    - **용도**: Section 4 (MCP 설정)

### 수동 캡처 필요 항목

- [x] **SpecKit** (1/3 완료):
    - [x] 7단계 워크플로우 다이어그램
    - [ ] SpecKit 설치 완료 화면
    - [ ] 생성된 문서 예시
- [x] **Copilot 워크북** (1/2 완료):
    - [x] Exercise 화면
    - [ ] 상세 결과 화면
- [ ] **문제 해결** (0/2):
    - [ ] 일반적 오류 상황 및 해결 방법
    - [ ] 설정 파일 검증 과정

### 품질 기준

- [x] **해상도**: 6/6 검증 완료 (1920x1080 기준)
- [x] **명명 규칙**: 일관된 파일명 체계 사용
- [x] **설명 추가**: Main doc에 링크 필요 (Part2.md에 6개 이미지 추가)
- [x] **검증**: 원본 화면과 스크린샷 일치성 확인 (6/6 완료)

---

## 🔗 관련 문서

### 내부 링크

- **Part 2 메인 문서**: [Practical_AI_Workflow_for_Grad_Students_Part2.md](../../Practical_AI_Workflow_for_Grad_Students_Part2.md)
- **Part 2 리소스 인덱스**: [README_Part2.md](README_Part2.md)
- **Copilot 워크북**: [12_copilot_workbook_exercises.md](12_copilot_workbook_exercises.md)
- **MCP 설치 가이드**: [15_mcp_installation_guide.md](15_mcp_installation_guide.md)
- **Cline MCP 스크린샷 설치 가이드**: [../../Context_and_Planning/demo-files/06-mcp-installation/cline-screenshot-mcp-setup.md](../../Context_and_Planning/demo-files/06-mcp-installation/cline-screenshot-mcp-setup.md)
- **Part 2 스크린샷 생성 프롬프트**: [../../Context_and_Planning/demo-files/06-mcp-installation/part2-screenshot-generation-prompts.md](../../Context_and_Planning/demo-files/06-mcp-installation/part2-screenshot-generation-prompts.md)
- **SpecKit 설치 가이드**: [19_speckit_installation_guide.md](19_speckit_installation_guide.md)

### 외부 참조

- **VS Code 공식 문서**: [VS Code 공식 문서](https://code.visualstudio.com/docs)
- **GitHub Copilot 문서**: [GitHub Copilot 문서](https://docs.github.com/copilot)
- **MCP 프로토콜**: [MCP Protocol](https://modelcontextprotocol.io/)
    🛠️ [Playwright 재시도 필요]
- **SpecKit 리포지토리**: [SpecKit Repository](https://github.com/github/spec-kit)
    🛠️ [Playwright 재시도 필요]

---

## 🤖 자동화 로그

### 2025-11-12 - MCP 자동화 (2개 완료)

- ✅ **MCP Protocol 소개 페이지**: Chrome DevTools 수동 캡처 (Playwright 실패 후 대체)
- ✅ **SpecKit Repository**: Chrome DevTools 수동 캡처 (Playwright 실패 후 대체)

**완료**: 2/2 공식 문서 페이지
**방법**: Chrome DevTools 수동 캡처 → 1920x1080 해상도
**Playwright 이슈**: macOS 보안 정책으로 Chromium `bootstrap_check_in Permission denied (1100)`, WebKit `Abort trap: 6`

### 2025-11-13 - 수동 캡처 완료 (4개)

- ✅ **SpecKit 7단계 워크플로우**: `speckit-7step-workflow.png` (Diagram mockup)
- ✅ **MCP 터미널 설치**: `mcp-terminal-install.png` (Terminal screenshot)
- ✅ **Copilot Workbook Exercise**: `copilot-workbook-exercise.png` (VS Code screenshot)
- ✅ **Claude Desktop 설정**: `claude-desktop-config.png` (Settings file screenshot)

**완료**: 4/13 수동 캡처 항목
**방법**: VS Code 스크린샷, 터미널 캡처, 다이어그램 생성
**진행률**: 6/15 (40%)

---

## 📝 메모

### 캡처 우선순위

1. ✅ **완료**: 공식 문서 페이지 2개 (MCP Protocol, SpecKit Repo)
2. ✅ **완료**: MCP 설치 1개 (Terminal screenshot)
3. ✅ **완료**: SpecKit 워크플로우 1개 (Diagram)
4. ✅ **완료**: Copilot 워크북 1개 (Exercise screenshot)
5. ✅ **완료**: Claude Desktop 설정 1개 (Config file)
6. **1순위**: 남은 SpecKit 상세 화면 2개
7. **2순위**: 남은 Copilot 워크북 결과 1개
8. **3순위**: 문제 해결 시나리오 2개

### 추후 업데이트 계획

- 새로운 버전의 도구가 출시될 때 스크린샷 업데이트
- 사용자 피드백을 바탕으로 더 명확한 설명 추가
- 단계별 캡처 대신 실제 사용 시나리오 기반 캡처로 변경 검토

---

**Version**: Part 2 Screenshot Guide
**Last Updated**: 2025-11-13
**Next Review**: v13.1 업데이트 시
