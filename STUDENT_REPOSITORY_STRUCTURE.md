# 학생 공개용 저장소 구조 가이드

> **목적**: 학생들이 저장소를 처음 클론했을 때 전체 구조를 이해하고 효과적으로 탐색할 수 있도록 안내합니다.  
> **대상**: 모든 학생 (공개 문서)  
> **버전**: 
> **최종 업데이트**: 2025-11-13

---

## 📖 저장소 개요

**대학원생을 위한 실용적 AI 워크플로우** 저장소에 오신 것을 환영합니다!

이 저장소는 대학원생들이 생성형 AI를 연구 파트너로 활용하여 연구 생산성을 10배 향상시키는 방법을 학습하도록 설계되었습니다.

### 🎯 저장소 목적

- **학습 자료 제공**: 3부작 강의 문서 + 43개 리소스 파일
- **실습 환경 제공**: 8개 데모 시나리오로 즉시 실습 가능
- **템플릿 제공**: 연구 계획서, 프롬프트, 워크플로우 템플릿
- **전공별 가이드**: 인문·사회·자연·공학 모두 적용 가능한 예시

### 📊 저장소 규모

- **핵심 문서**: 5개 (README, LICENSE, Part 1-3)
- **리소스 파일**: 30+ 번호가 매겨진 리소스 + 지원 자료 (템플릿, 가이드, 이미지 등)
- **데모 시나리오**: 8개 폴더 + DEMO-QUICK-START.md
- **총 파일 개수**: 약 110개 이상
- **학습 시간**: 17-25시간 (4-6주 과정)

---

## 🗂️ 디렉토리 트리

```text
Generative AI Special Lecture - Graduate School/
├── README.md                                    # 🎯 시작 가이드 (여기부터 읽으세요!)
├── LICENSE                                      # 📄 라이선스 정보
│
├── Practical_AI_Workflow_for_Grad_Students_Part1.md  # 📚 기초 편
├── Practical_AI_Workflow_for_Grad_Students_Part2.md  # 📚 고급 도구 편
├── Practical_AI_Workflow_for_Grad_Students_Part3.md  # 📚 통합 워크플로우 편
│
├── resources/                            # 📦 30+ 리소스 파일
│   ├── README.md                               # 🗂️ 리소스 마스터 인덱스
│   ├── README_Part1.md                     # Part 1 가이드
│   ├── README_Part2.md                     # Part 2 가이드
│   ├── README_Part3.md                     # Part 3 가이드
│   │
│   ├── 번호가 매겨진 리소스 (30+개)
│   │   ├── 01-11: Part 1 기초 자료
│   │   │   (Copilot 가이드, VS Code 설정, 템플릿 등)
│   │   ├── 13-23: 공유 리소스 및 Part 2 자료
│   │   │   (MCP, SpecKit, 연구 계획 등)
│   │   └── 38-43: 확장 템플릿
│   │       (워크플로우 자동화, 프롬프트 라이브러리 등)
│   │
│   └── 시각 자료 폴더
│       ├── part2/                              # Part 2 이미지 (16개)
│       ├── part3/                              # Part 3 이미지 (27개)
│       └── images/                             # 공통 이미지 (34개)
│
└── Context_and_Planning/
    └── demo-files/                             # 🎭 8개 실습 데모
        ├── DEMO-QUICK-START.md                 # 🚀 데모 시작 가이드
        │
        ├── 01-vscode-markdown/                 # VS Code와 Markdown 기본
        ├── 02-github-copilot/                  # GitHub Copilot 핵심 기능
        ├── 03-github-projects/                 # GitHub Projects 프로젝트 관리
        ├── 04-task-master-mcp/                 # Task Master MCP 서버 활용
        ├── 05-copilot-workbook/                # Copilot Workbook 실습
        ├── 06-mcp-installation/                # MCP 서버 설치 및 설정
        ├── 07-speckit-practice/                # SpecKit 워크플로우 실습
        └── 08-integrated-workflow/             # 통합 워크플로우 완전 적용
```

---

## 📚 주요 파일 설명

### 🎯 README.md (첫 번째로 읽어야 할 파일)

**[README.md](./README.md)** - 저장소 전체 개요 및 학습 경로 안내

**내용**:

- 프로젝트 소개 및 주요 특징
- 3부작 구조 설명 (Part 1-3)
- 빠른 시작 가이드 (초보자/중급자/고급자/전공별 경로)
- 필수 도구 설치 안내
- 학습 목표 및 기대 효과

**읽는 시간**: 10-15분

### 📚 Part 1-3 문서 (핵심 강의 자료)

#### Part 1: 기초 편 (2-3시간)

**[Practical_AI_Workflow_for_Grad_Students_Part1.md](./Practical_AI_Workflow_for_Grad_Students_Part1.md)**

- Context Engineering 기본
- Markdown으로 연구 문서 작성
- GitHub Copilot 2025 신기능
- 연구 효율성 10배 향상 기법

#### Part 2: 고급 도구 편 (3-4시간)

**[Practical_AI_Workflow_for_Grad_Students_Part2.md](./Practical_AI_Workflow_for_Grad_Students_Part2.md)**

- Copilot Workbook 4개 실습
- MCP 서버 설치 및 통합
- SpecKit 워크플로우 마스터
- 도구 생태계 구축

#### Part 3: 통합 워크플로우 편 (4-6시간)

**[Practical_AI_Workflow_for_Grad_Students_Part3.md](./Practical_AI_Workflow_for_Grad_Students_Part3.md)**

- 8단계 연구 라이프사이클
- 5개 전공별 완전 시나리오 (교육학, 생명과학, 컴퓨터공학, 사회학, 음악학)
- 2025년 AI 연구 도구 생태계
- 실제 프로젝트 적용

### 📦 resources/ (43개 리소스 파일)

**[resources/README.md](./resources/README.md)** - 마스터 인덱스 (필수 참조!)

**구성**:

- **01-11**: Part 1 기초 자료 (Copilot 가이드, VS Code 설정, 템플릿 등)
- **12-23**: 공유 리소스 및 Part 2 자료 (계획, MCP, SpecKit 등)
- **24-37**: Part 3 통합 워크플로우 자료 (시나리오, 도구 생태계 등)
- **38-43**: 확장 템플릿 (워크플로우 자동화, 프롬프트 라이브러리 등)

**주요 리소스 하이라이트**:

- **01번**: Copilot 2025 최신 기능 가이드
- **04번**: Markdown 연구 문서 템플릿
- **14번**: 연구 계획서 템플릿
- **16번**: Task Master MCP 가이드
- **21번**: SpecKit 연구 프로젝트 템플릿
- **25번**: 2025 AI 연구 도구 생태계
- **26-29번**: 4개 전공별 완전 시나리오
- **39번**: 프롬프트 라이브러리

**참고**: README.md에서 "13번", "21번" 같은 번호 참조는 이 마스터 인덱스를 가리킵니다.

### 🎭 Context_and_Planning/demo-files/ (8개 데모)

**[Context_and_Planning/demo-files/DEMO-QUICK-START.md](./Context_and_Planning/demo-files/DEMO-QUICK-START.md)** - 데모 시작 가이드

**8개 데모 시나리오**:

1. **01-vscode-markdown**: VS Code 설정 + Markdown 기본 실습
2. **02-github-copilot**: Copilot Chat, Inline Chat, Agent 모드
3. **03-github-projects**: GitHub Projects로 연구 프로젝트 관리
4. **04-task-master-mcp**: Task Master MCP 서버 설치 및 활용
5. **05-copilot-workbook**: 4개 Copilot Workbook 실습
6. **06-mcp-installation**: MCP 서버 설치 및 Claude 통합
7. **07-speckit-practice**: SpecKit으로 연구 계획 체계화
8. **08-integrated-workflow**: 실제 연구 프로젝트에 전체 워크플로우 통합

**실습 방법**: 각 데모 폴더에는 README.md, 프롬프트 예시, 스크린샷, 가이드가 포함되어 있습니다.

---

## 🎓 학습 경로 안내

저장소를 효과적으로 탐색하는 방법을 수준별로 안내합니다.

### 🌱 초보자 (AI 도구 처음 사용)

**학습 시간**: 4-6시간

```text
1. README.md 읽기 (10분)
   ↓
2. Part 1 기초 편 전체 학습 (2-3시간)
   - Context Engineering
   - Markdown 문서화
   - GitHub Copilot 기본
   ↓
3. resources/README.md 마스터 인덱스 확인 (10분)
   ↓
4. 자신의 전공에 맞는 예시 참조 (1시간)
   - 인문/사회: 40번 전공별 템플릿
   - 자연/공학: 04번 Markdown 템플릿
   ↓
5. 14번 연구 계획서 템플릿으로 첫 문서 작성 (1-2시간)
```

**추천 데모**: 01-vscode-markdown, 02-github-copilot

### 🔧 중급자 (AI 도구 경험 있음)

**학습 시간**: 3-4시간

```text
1. Part 1 복습 (30분 - 핵심만)
   - Context Engineering 개념
   - Copilot 모델 선택 (02번 참조)
   ↓
2. Part 2 고급 도구 편 학습 (2-3시간)
   - Copilot Workbook 4개 실습
   - MCP 서버 통합 (15번, 16번)
   - SpecKit 워크플로우 (19번, 20번)
   ↓
3. 13번 연구 계획 워크플로우로 계획 중심 연구 시작 (30분)
   ↓
4. 21번 SpecKit 템플릿으로 실습 프로젝트 수행 (1-2시간)
```

**추천 데모**: 05-copilot-workbook, 06-mcp-installation, 07-speckit-practice

### 🏆 고급자 (생산성 극대화 원함)

**학습 시간**: 2-3시간

```text
1. Part 3 통합 워크플로우 편 학습 (1-2시간)
   - 8단계 연구 라이프사이클 (24번)
   - 2025 AI 도구 생태계 (25번)
   ↓
2. 자신의 전공 시나리오 적용 (1시간)
   - 교육학: 26번
   - 생명과학: 27번
   - 컴퓨터공학: 28번
   - 사회학: 29번
   - 음악학: Part 3 참조
   ↓
3. 38-43번 확장 템플릿으로 워크플로우 최적화 (30분)
   - 38번: 워크플로우 자동화
   - 39번: 프롬프트 라이브러리
   - 41번: AI 도구 통합 패턴
   ↓
4. 실제 연구 프로젝트에 25번 도구 생태계 적용 (1-2시간)
```

**추천 데모**: 08-integrated-workflow

### 🎯 전공별 경로

#### 인문/사회과학자

```text
Part 1 (Context + Markdown + Copilot Chat)
   ↓
공유 리소스 (14번 템플릿 + 18번 MCP 조합)
   ↓
Part 3 (26번 교육학 시나리오 + 30번 문헌 리뷰)
```

**관련 리소스**: 04, 06, 14, 18, 26, 30, 34, 39, 40

#### 자연과학/공학자

```text
Part 1 (VS Code + Copilot + MCP 소개)
   ↓
Part 2 (15번 MCP 설치 + 19번 SpecKit)
   ↓
Part 3 (25번 도구 생태계 + 32번 진행 추적)
```

**관련 리소스**: 03, 15, 16, 19, 21, 25, 27, 28, 31, 32

#### 예술/디자인연구자

```text
Part 1 (Markdown + Copilot Vision)
   ↓
공유 리소스 (39번 프롬프트 + 18번 MCP 조합)
   ↓
Part 3 (36번 성공 사례 + 42번 협업 워크플로우)
```

**관련 리소스**: 04, 06, 18, 33, 35, 36, 39, 40, 42

### ⚡ 시간 압박자 (빠른 시작)

**학습 시간**: 90분

```text
30분: Part 1 핵심
   - Context Engineering (핵심 개념만)
   - Copilot 모델 선택 (02번)
   ↓
30분: 공유 리소스
   - 14번 연구 계획서 템플릿
   - 16번 Task Master MCP
   ↓
30분: Part 3 적용
   - 30번 문헌 리뷰 워크플로우
```

### 🔍 문제 해결자

**학습 시간**: 45분

```text
15분: 09번 Part 1 문제 해결 가이드
15분: 23번 Part 2 트러블슈팅
15분: 37번 Part 3 트러블슈팅
```

---

## 📊 파일 개수 요약

### 디렉토리별 파일 개수

| 디렉토리 | 파일 종류 | 개수 | 설명 |
|---------|---------|------|------|
| **루트** | 핵심 문서 | 5개 | README, LICENSE, Part 1-3 |
| **resources/** | 번호가 매겨진 리소스 | 31개 | 템플릿, 가이드, 예시 (01-43번 범위) |
| **resources/** | 지원 문서 | 4개 | README, README_Part1-3 |
| **resources/part2/** | 이미지/다이어그램 | 16개 | Part 2 시각 자료 |
| **resources/part3/** | 이미지/다이어그램 | 27개 | Part 3 시각 자료 |
| **resources/images/** | 공통 이미지 | 34개 | 공유 시각 자료 |
| **demo-files/** | 데모 시나리오 | 8개 폴더 | 실습용 데모 + 가이드 |
| **총계** | - | **110개 이상** | 전체 파일 |

### 파일 유형별 분류

- **Markdown 문서**: 약 40개 (Part 문서, 번호가 매겨진 리소스, 데모 가이드)
- **이미지/다이어그램**: 약 77개 (SVG, PNG - part2, part3, images 폴더)
- **설정/예시 파일**: JSON 설정, CSV 데이터, Python 스크립트 예시 등
- **기타**: LICENSE, .gitkeep 등

---

## 🚀 다음 단계 안내

### 1단계: 환경 준비 (15분)

```text
1. VS Code 설치
   - https://code.visualstudio.com/
   
2. GitHub Copilot 확장 설치
   - VS Code 확장 마켓플레이스에서 "GitHub Copilot" 검색
   
3. GitHub Student Developer Pack 신청
   - https://education.github.com/pack
   - Copilot Pro 무료 사용!
```

**참고 리소스**: 03번 VS Code 설정 가이드

### 2단계: README.md 읽기 (10분)

**[README.md](./README.md)**를 읽고 전체 프로젝트 구조와 학습 경로를 파악하세요.

### 3단계: 수준 선택 (자기 평가)

- **AI 도구 처음 사용**: 초보자 경로 → Part 1부터 시작
- **Copilot 경험 있음**: 중급자 경로 → Part 1 복습 + Part 2
- **생산성 극대화 원함**: 고급자 경로 → Part 3 + 전공별 시나리오

### 4단계: 학습 시작!

선택한 경로에 따라 Part 문서를 순서대로 학습하세요.

- **Part 1**: [Practical_AI_Workflow_for_Grad_Students_Part1.md](./Practical_AI_Workflow_for_Grad_Students_Part1.md)
- **Part 2**: [Practical_AI_Workflow_for_Grad_Students_Part2.md](./Practical_AI_Workflow_for_Grad_Students_Part2.md)
- **Part 3**: [Practical_AI_Workflow_for_Grad_Students_Part3.md](./Practical_AI_Workflow_for_Grad_Students_Part3.md)

### 5단계: 리소스 활용

학습 중 필요한 템플릿, 가이드, 예시는 **[resources/README.md](./resources/README.md)** 마스터 인덱스에서 찾으세요.

### 6단계: 데모 실습

이론 학습 후 **[Context_and_Planning/demo-files/](./Context_and_Planning/demo-files/)**에서 실습하세요.

---

## 💡 팁과 권장 사항

### 📌 학습 팁

1. **순서대로 학습**: Part 1 → Part 2 → Part 3 순서를 지키면 이해가 쉽습니다
2. **실습 병행**: 이론 학습 후 즉시 데모로 실습하세요
3. **템플릿 활용**: 처음부터 만들지 말고 리소스 템플릿을 수정해서 사용하세요
4. **전공별 예시**: 자신의 전공과 유사한 시나리오를 우선 학습하세요
5. **문제 해결**: 막힐 때는 09번, 23번, 37번 트러블슈팅 가이드 참조

### 🎯 효과적인 탐색

- **검색 활용**: VS Code에서 `Ctrl+P` (또는 `Cmd+P`)로 파일 이름 검색
- **키워드 검색**: `Ctrl+Shift+F` (또는 `Cmd+Shift+F`)로 전체 텍스트 검색
- **마스터 인덱스**: 리소스 찾을 때는 resources/README.md 먼저 확인
- **링크 활용**: README.md의 모든 링크는 클릭 가능합니다 (VS Code 프리뷰 모드)

### 🚀 학습 가속화

- **GitHub Student Pack**: Copilot Pro 무료 → 학습 효율 10배 향상
- **데모 먼저**: 시간 없을 때는 데모부터 실습하고 이론은 나중에
- **템플릿 복사**: 리소스 템플릿을 자신의 프로젝트에 복사해서 바로 사용
- **프롬프트 라이브러리**: 39번 프롬프트 라이브러리를 즐겨찾기에 추가

### 🤝 협업 및 공유

- **GitHub Issues**: 버그 발견 시 이슈 등록
- **피드백**: 강의 후 설문 참여 (개선에 큰 도움이 됩니다!)
- **동료 공유**: 저장소 URL을 동료 대학원생들과 공유하세요

---

## 🎓 학습 목표 재확인

이 저장소를 완료하면:

- ✅ **AI 연구 파트너 활용**: Context Engineering으로 AI 출력 품질 극대화
- ✅ **체계적 문서화**: Markdown 기반 연구 문서 체계 구축
- ✅ **생산성 10배 향상**: GitHub Copilot 2025로 연구 효율성 극대화
- ✅ **도구 통합**: MCP로 AI 도구 생태계 구축
- ✅ **연구 자동화**: SpecKit으로 계획-실행-검증 워크플로우 구현
- ✅ **전공별 적용**: 5개 전공 시나리오로 실제 프로젝트 적용
- ✅ **미래 대비**: 2025년 AI 연구 도구 생태계 완전 마스터

---

## 📞 문의 및 지원

### 질문이 있으신가요?

- **버그 리포트**: GitHub Issues 등록
- **개선 제안**: Pull Request 환영
- **학습 관련 문의**: 강의 담당자 메일 또는 수업 시간에 질문

### 추가 리소스

- **공식 문서**: 각 도구의 공식 문서 링크는 Part 문서에 포함
- **커뮤니티**: GitHub Discussions (활성화 시)
- **업데이트**: 새 버전 릴리스 시 README.md 버전 정보 참조

---

## 🎊 학습을 시작하세요

준비가 되었다면 **[README.md](./README.md)**부터 시작하세요!

*2025년 최신 AI 도구로 연구 생산성을 혁신하는 여정이 시작됩니다!*

---

## 📋 빠른 참조 (즐겨찾기)

### 자주 사용하는 파일

- **[README.md](./README.md)** - 전체 개요
- **[resources/README.md](./resources/README.md)** - 리소스 마스터 인덱스
- **[Context_and_Planning/demo-files/DEMO-QUICK-START.md](./Context_and_Planning/demo-files/DEMO-QUICK-START.md)** - 데모 가이드
- **[Part 1](./Practical_AI_Workflow_for_Grad_Students_Part1.md)** - 기초 편
- **[Part 2](./Practical_AI_Workflow_for_Grad_Students_Part2.md)** - 고급 도구 편
- **[Part 3](./Practical_AI_Workflow_for_Grad_Students_Part3.md)** - 통합 워크플로우 편

### 자주 참조하는 리소스

- **01번**: Copilot 2025 최신 기능
- **04번**: Markdown 연구 템플릿
- **14번**: 연구 계획서 템플릿
- **25번**: AI 연구 도구 생태계
- **39번**: 프롬프트 라이브러리
- **09, 23, 37번**: 트러블슈팅 가이드

---

## 🔧 저장소 유지보수 참고사항

### .gitignore 규칙에 대하여

현재 `.gitignore`는 학생용 저장소를 깔끔하게 유지하기 위해 다음 파일들을 무시합니다:

- **루트 `.py` 파일**: 현재 강사용 스크립트만 존재하여 차단 중
- **`package.json`**: 현재 Node.js 종속성이 없어 차단 중
- **`.github/` 폴더**: 현재 GitHub Actions가 없어 차단 중

**향후 확장 계획 시 검토 필요:**

만약 향후 다음과 같은 학생용 콘텐츠를 추가할 계획이 있다면 `.gitignore` 규칙을 조정해야 합니다:

1. **Python 예제 추가 시**:
   ```gitignore
   # .gitignore에 예외 규칙 추가
   /*.py
   !/student_example.py  # 특정 학생용 파일 허용
   ```

2. **Node.js 데모 추가 시**:
   - `/package.json` 규칙 제거
   - 또는 `Context_and_Planning/demo-files/` 내 package.json만 허용

3. **GitHub Actions 튜토리얼 추가 시**:
   - `/.github/` 규칙 제거
   - 또는 특정 워크플로우만 허용하도록 세분화

현재는 학생용 저장소를 간결하게 유지하기 위해 위 규칙들을 유지하고 있습니다.

---

*대학원생을 위한 실용적 AI 워크플로우 | 학생 공개용 문서*  
*최종 업데이트: 2025-11-13*
