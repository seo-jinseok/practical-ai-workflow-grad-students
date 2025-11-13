# Part 3 스크린샷 캡처 가이드

**Version**: v13.0 Part 3
**Date**: 2025-11-13
**Purpose**: Part 3 관련 스크린샷 필요한 경우의 가이드 문서
**Status**: 🚧 In Progress (8/20 완료, 40%, MCP 1 + manual 7)
**Related**: [Part 3 메인 문서](../Practical_AI_Workflow_for_Grad_Students%20v13.0_Part3.md) | [Part 3 리소스 인덱스](README_Part3.md)

---

## 🎯 목적

Part 3에서 사용될 스크린샷들의 캡처 가이드라인을 제공합니다. Part 3는 통합 워크플로우와 실전 적용에 중점을 두므로, 실제 도구 사용 시나리오와 결과물이 중심이 됩니다.

---

## 📋 스크린샷 목록

### 1. 연구 도구 생태계 (25_2025_research_tools_ecosystem.md)

#### 2025년 AI 연구 도구들

**완료된 스크린샷** (1개):
- [x] **Elicit**: 논문 검색 및 요약 화면
  - ✅ **생성 완료**: 2025-11-13
  - **파일명**: `elicit-main.png`
  - **저장 위치**: `resources/part3/images/tools-ecosystem/`
  - **파일 크기**: ~50KB
  - **해상도**: 1920x1080
  - **용도**: Section 4.1 (AI 연구 도구 생태계)

**대기 중인 스크린샷** (7개) - ⏳ **[MCP 배치 자동화 필요]**:
- [ ] **Perplexity**: 웹 검색 및 인용 기능
  - ⏳ **MCP 프롬프트 필요**: `part3-screenshot-generation-prompts.md`
  - **파일명**: `perplexity-main.png`
  - **URL**: https://perplexity.ai/
- [ ] **NotebookLM**: 노트북 기반 연구 도구
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `notebooklm-main.png`
  - **URL**: https://notebooklm.google.com/
- [ ] **Consensus**: 학술 연구 도구
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `consensus-main.png`
  - **URL**: https://consensus.app/
- [ ] **Scite**: 인용 분석 도구
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `scite-main.png`
  - **URL**: https://scite.ai/
- [ ] **ResearchRabbit**: 연구 발견 도구
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `researchrabbit-main.png`
  - **URL**: https://researchrabbit.ai/
- [ ] **Connected Papers**: 논문 연결 시각화
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `connectedpapers-main.png`
  - **URL**: https://www.connectedpapers.com/
- [ ] **Semantic Scholar**: AI 학술 검색
  - ⏳ **MCP 프롬프트 필요**
  - **파일명**: `semanticscholar-main.png`
  - **URL**: https://www.semanticscholar.org/

## 🤖 MCP 자동화 로그

### 2025-11-13 - Part 3 연구 도구 생태계

- ✅ **Elicit** (<https://elicit.org/>) - 완료
- ⏳ **Perplexity** (<https://perplexity.ai/>) - MCP 배치 실행 필요
- ⏳ **NotebookLM** (<https://notebooklm.google.com/>) - MCP 배치 실행 필요
- ⏳ **Consensus** (<https://consensus.app/>) - MCP 배치 실행 필요
- ⏳ **Scite** (<https://scite.ai/>) - MCP 배치 실행 필요
- ⏳ **ResearchRabbit** (<https://researchrabbit.ai/>) - MCP 배치 실행 필요
- ⏳ **Connected Papers** (<https://www.connectedpapers.com/>) - MCP 배치 실행 필요
- ⏳ **Semantic Scholar** (<https://www.semanticscholar.org/>) - MCP 배치 실행 필요

**완료**: 1/8 (12.5%)
**대기**: 7/8 (87.5%)

**사용 도구**: Cline MCP `webpageScreenshot` 서버 (`@srigi/mcp-webpage-screenshot`)  
**생성 방법**: `part3-screenshot-generation-prompts.md` 배치 프롬프트 실행 필요
**저장 위치**: `resources/part3/images/tools-ecosystem/`  
**해상도**: 1920x1080 PNG

**다음 단계**: 배치 프롬프트로 나머지 7개 도구 스크린샷 생성 (~7분 예상)

### 기타 Part 3 이미지 (7개 완료)

- [x] **연구 생애주기 다이어그램**
  - ✅ **생성 완료**: 2025-11-13
  - **파일명**: `research-8step-lifecycle.png`
  - **저장 위치**: `resources/part3/images/`
  - **용도**: Section 1 (연구 프로세스 개요)
- [x] **AI 도구 생태계 다이어그램**
  - ✅ **생성 완료**: 2025-11-13
  - **파일명**: `ai-tools-ecosystem.png`
  - **저장 위치**: `resources/part3/images/`
  - **용도**: Section 1.3 (도구 통합)
- [x] **전공별 폴더 구조** (5개):
  - [x] 교육학: `education-project-folders.png` - Section 2
  - [x] 생명과학: `life-science-project-folders.png` - Section 3
  - [x] 컴퓨터공학: `cs-project-folders.png` - Section 4
  - [x] 사회학: `sociology-project-folders.png` - Section 5
  - [x] 음악학: `music-project-folders.png` - Section 6
  - ✅ **생성 완료**: 2025-11-13
  - **저장 위치**: `resources/part3/images/`
  - **방법**: Mockup/diagram generation

### 2. 교육학 시나리오 (26_education_complete_scenario.md)

#### 통합 워크플로우 시연
- **중요한 스크린샷** (4-5개):
  - 초기 연구 계획서 완성 화면
  - 문헌 조사와 분석 진행 상황
  - 데이터 수집 및 분석 결과
  - 논문 초안 작성 진행 상황
  - 최종 논문 완성 화면
- **캡처 지침**:
  - 시간 순서대로 워크플로우 진행 상황 캡처
  - 각 단계의 핵심 결과물과 문서 구조 강조
  - 전/후 비교로 개선점 명시
- **저장 경로**: `resources/part3/images/education-scenario-*.png`

### 3-6. 전공별 시나리오 (27-29번: 향후 추가 예정)

#### TBD 파일들
- **27번**: 생명과학 실험 연구 시나리오
- **28번**: 컴퓨터공학 시스템 개발 시나리오  
- **29번**: 사회학 질적 연구 시나리오
- **30번**: 음악학 창작 프로젝트 시나리오 (Section 6)

**공통 요구사항**:
- 각 전공의 고유한 도구와 워크플로우 시연
- 실제 연구 결과물과 문서 예시
- 전공별 특화 AI 프롬프트 예시

### 7. 문헌 리뷰 워크플로우 (30_literature_review_2025_workflow.md)

#### 2025년식 문헌 리뷰
- **중요한 스크린샷**:
  - AI 도구들을 활용한 체계적 문헌 검색
  - 자동화된 문헌 분류 및 요약
  - 연구 갭 분석 과정
  - 문헌 고찰 초안 작성 화면
- **캡처 지침**:
  - 새로운 AI 도구들을 활용한 최신 방법론 강조
  - 2025년 도구의 장점과 기존 방법 대비 개선점 명시
- **저장 경로**: `resources/part3/images/literature-review-*.png`

### 8. 주간/월간 루틴 (31_weekly_monthly_routines.md)

#### 연구 루틴 자동화
- **중요한 스크린샷**:
  - 주간 연구 계획 및 체크리스트
  - AI 도구들과의 정기적 상호작용 화면
  - 진행 상황 추적 대시보드
  - 월간 성과 리뷰 화면
- **캡처 지침**:
  - 실제 연구자의 화면을 기반으로 한 현실적인 시나리오
  - 루틴의 지속 가능성과 효과성 강조
- **저장 경로**: `resources/part3/images/research-routines-*.png`

### 9. 진행 상황 추적 (32_progress_tracking_methods.md)

#### 프로젝트 관리 대시보드
- **중요한 스크린샷**:
  - GitHub Projects 또는 Notion 기반 프로젝트 보드
  - AI 도구들을 활용한 자동화된 진행 상황 업데이트
  - 마일스톤 및 마감일 관리 화면
  - 성과 측정 및 분석 결과
- **캡처 지침**:
  - 프로젝트 관리 도구와 AI 도구의 통합 강조
  - 데이터 시각화와 추적 지표 명확히 표시
- **저장 경로**: `resources/part3/images/progress-tracking-*.png`

### 10. 문제 해결 프로토콜 (33_problem_solving_protocol.md)

#### 5단계 문제 해결
- **중요한 스크린샷**:
  - 각 단계별 실행 과정 및 도구 사용
  - AI 도구들을 활용한 진단 및 해결 제안
  - 해결 전후 비교 화면
  - 지식 베이스 및 FAQ 구축
- **캡처 지침**:
  - 문제 해결의 체계적 접근법 시각화
  - AI 도구들의 역할과 한계 명확히 표시
- **저장 경로**: `resources/part3/images/problem-solving-*.png`

### 11. 품질 관리 체크리스트 (34_quality_checklist.md)

#### 연구 품질 관리
- **중요한 스크린샷**:
  - 체크리스트 실행 화면
  - AI 도구들을 활용한 자동화된 품질 검증
  - 피드백 및 개선 과정
  - 최종 품질 평가 결과
- **캡처 지침**:
  - 품질 관리의 객관성과 체계성 강조
  - 자동화와 수동 검토의 균형점 명시
- **저장 경로**: `resources/part3/images/quality-checklist-*.png`

### 12. 폴더 구조 예시 (35_folder_structure_examples.md)

#### 연구 조직화
- **중요한 스크린샷**:
  - 전공별 최적화된 폴더 구조
  - 버전 관리 및 문서 관리 시스템
  - AI 도구들과의 통합된 작업 환경
  - 팀 협업 시 폴더 구조 예시
- **캡처 지침**:
  - 실제 연구 프로젝트의 폴더 구조 예시
  - 파일命名 규칙과 관리 시스템 명확히 표시
- **저장 경로**: `resources/part3/images/folder-structures-*.png`

### 13. 성공 사례 (36_success_stories.md)

#### 실제 성공 사례들
- **중요한 스크린샷**:
  - 연구 성과 향상 통계 및 그래프
  - AI 도구 도입 전후 비교
  - 연구 생산성 증가 시각화
  - 연구자 인터뷰 또는 피드백 화면
- **캡처 지침**:
  - 실제 수치와 데이터를 기반으로 한 객관적 결과
  - 다양한 전공과 연구 분야 커버
- **저장 경로**: `resources/part3/images/success-stories-*.png`

---

## 🎨 캡처 지침

### 기술적 요구사항
- **해상도**: 정확히 1920x1080 (현재 디스플레이 해상도 이상)
- **파일 형식**: PNG (스크린샷), JPG (이미지/그래프)
- **용량**: 1MB 이하 유지 (압축 필요시)
- **명명 규칙**: `[연관파일명]-[주제]-[단계].png`

### 시각적 가이드
- **주요 포인트 강조**:
  - AI 도구들의 기여와 기능 하이라이트
  - 연구 성과 향상 부분을 화살표나 텍스트로 강조
  - 전/후 비교로 개선점 명시
- **단계별 설명**:
  - 각 스크린샷에 단계 번호와 설명 추가
  - 워크플로우의 진행 상황을 시각적으로 연결
- **접근성 고려**:
  - 색상 대비와 텍스트 가독성 확보
  --screen reader를 위한 alt-text 추가

### 통합 워크플로우 강조
- **도구 간 연결성**:
  - 여러 AI 도구가 함께 작동하는 화면
  - 데이터와 결과가 도구 간 흐르는 과정
- **실시간 시연**:
  - 실제 연구 과정의 실시간 진행 상황
  - 문제 해결과 의사결정 과정

---

## 📁 저장 구조

```
resources/part3/
├── images/                                  # 스크린샷 저장 디렉토리
│   ├── research-8step-lifecycle.png         # ✅ 생성 완료
│   ├── ai-tools-ecosystem.png               # ✅ 생성 완료
│   ├── education-project-folders.png        # ✅ 생성 완료
│   ├── life-science-project-folders.png     # ✅ 생성 완료
│   ├── cs-project-folders.png               # ✅ 생성 완료
│   ├── sociology-project-folders.png        # ✅ 생성 완료
│   ├── music-project-folders.png            # ✅ 생성 완료
│   ├── tools-ecosystem/
│   │   ├── elicit-main.png                  # ✅ 생성 완료
│   │   ├── perplexity-main.png              # ⏳ MCP 배치 대기
│   │   ├── notebooklm-main.png              # ⏳ MCP 배치 대기
│   │   ├── consensus-main.png               # ⏳ MCP 배치 대기
│   │   ├── scite-main.png                   # ⏳ MCP 배치 대기
│   │   ├── researchrabbit-main.png          # ⏳ MCP 배치 대기
│   │   ├── connectedpapers-main.png         # ⏳ MCP 배치 대기
│   │   └── semanticscholar-main.png         # ⏳ MCP 배치 대기
│   ├── education-scenario/
│   │   ├── step1-research-plan.png
│   │   ├── step2-literature-review.png
│   │   ├── step3-data-analysis.png
│   │   ├── step4-paper-draft.png
│   │   └── step5-final-paper.png
│   ├── research-routines/
│   │   ├── weekly-planning.png
│   │   ├── monthly-review.png
│   │   └── progress-dashboard.png
│   ├── discipline-specific/
│   │   ├── biology-workflow.png
│   │   ├── computer-science-project.png
│   │   ├── sociology-analysis.png
│   │   └── music-composition.png
│   ├── quality-management/
│   │   ├── checklist-execution.png
│   │   ├── automated-verification.png
│   │   └── quality-scoring.png
│   └── folder-structures/
│       ├── humanities-organization.png
│       ├── stem-project-structure.png
│       └── team-collaboration.png
└── 24-37_screenshot_descriptions.md         # 이 파일
```

---

## ✅ 캡처 체크리스트

### Part 3 핵심 스크린샷 (우선순위 높음)

- [x] **2025년 연구 도구 생태계** (1/8개 완료, 12.5%) 🚧:
    - [x] Elicit (완료)
    - [ ] Perplexity, NotebookLM, Consensus, Scite (4개 대기)
    - [ ] ResearchRabbit, Connected Papers, Semantic Scholar (3개 대기)
    - 🚧 MCP 배치 실행 필요 (7개)
    - 📝 `part3-screenshot-generation-prompts.md` 참조
- [x] **기타 다이어그램 및 폴더 구조** (7/7 완료) ✅:
    - [x] 연구 생애주기 다이어그램 (research-8step-lifecycle.png)
    - [x] AI 도구 생태계 다이어그램 (ai-tools-ecosystem.png)
    - [x] 5개 전공별 폴더 구조 (education, life-science, cs, sociology, music)
- [ ] **교육학 완전 시나리오** (0/5-6개):
    - [ ] 5단계 워크플로우 진행 과정
    - [ ] 각 단계의 핵심 결과물
    - [ ] 전/후 비교로 개선점 명시
- [ ] **통합 워크플로우** (0/3-4개):
    - [ ] 도구 간 연결성 및 데이터 흐름
    - [ ] AI 도구들이 함께 작동하는 화면
    - [ ] 문제 해결 및 의사결정 과정

### Part 3 보조 스크린샷 (선택적)

- [ ] **전공별 시나리오** (0/2-3개):
    - [ ] 생물과학, 컴퓨터공학, 사회학, 음악학
    - [ ] 각 전공의 고유한 워크플로우
- [ ] **연구 관리** (2-3개):
  - [ ] 주간/월간 루틴, 진행 상황 추적
  - [ ] 프로젝트 대시보드 및 성과 측정
- [ ] **품질 관리** (2-3개):
  - [ ] 체크리스트 실행, 자동화된 검증
  - [ ] 품질 평가 및 개선 과정

### 품질 기준
- [ ] **해상도**: 정확히 1920x1080
- [ ] **명명 규칙**: 일관된 파일명 체계 사용
- [ ] **설명 추가**: 각 스크린샷에 상세 설명문 추가
- [ ] **워크플로우 연결성**: 도구 간 연결 및 데이터 흐름 명확화
- [ ] **실제성**: 실제 연구 환경과 유사한 시나리오 기반

---

## 🔗 관련 문서

### 내부 링크
- **Part 3 스크린샷 생성 프롬프트**: [../../Context_and_Planning/demo-files/06-mcp-installation/part3-screenshot-generation-prompts.md](../../Context_and_Planning/demo-files/06-mcp-installation/part3-screenshot-generation-prompts.md)
- **Part 3 메인 문서**: [Practical_AI_Workflow_for_Grad_Students_Part3.md](../Practical_AI_Workflow_for_Grad_Students%20v13.0_Part3.md)
- **Part 3 리소스 인덱스**: [README_Part3.md](README_Part3.md)
- **Part 1 스크린샷 가이드**: [../11_screenshot_descriptions.md](../11_screenshot_descriptions.md)
- **Part 2 스크린샷 가이드**: [../part2/12_screenshot_descriptions.md](../part2/12_screenshot_descriptions.md)

### 주요 연구 도구들

- **Elicit**: <https://elicit.org/> - ✅ [MCP 완료]
- **Perplexity**: <https://perplexity.ai/> - ⏳ [MCP 대기]
- **NotebookLM**: <https://notebooklm.google.com/> - ⏳ [MCP 대기]
- **Consensus**: <https://consensus.app/> - ⏳ [MCP 대기]
- **Scite**: <https://scite.ai/> - ⏳ [MCP 대기]
- **ResearchRabbit**: <https://researchrabbit.ai/> - ⏳ [MCP 대기]
- **Connected Papers**: <https://www.connectedpapers.com/> - ⏳ [MCP 대기]
- **Semantic Scholar**: <https://www.semanticscholar.org/> - ⏳ [MCP 대기]

---

## 📝 메모

### 캡처 우선순위

1. 🚧 **진행 중**: 2025년 연구 도구 생태계 (1/8 완료, MCP 배치 7개 ~7분)
2. **1순위**: 교육학 완전 시나리오 (5단계 워크플로우, 수동 캡처)
3. **2순위**: 통합 워크플로우 및 도구 간 연결성 (수동 캡처)
4. **3순위**: 전공별 특화 시나리오 (수동 캡처)
5. **4순위**: 연구 관리 및 품질 관리 (수동 캡처)

### 추후 업데이트 계획
- 새로운 AI 도구들의 추가 및 업데이트
- 사용자 피드백을 바탕으로 더 실용적인 시나리오 개발
- 실제 연구 성과 데이터를 통한 효과성 검증
- 다양한 전공별 커버리지 확대

### 특히 강조할 부분
- **통합성**: 여러 AI 도구가 함께 작동하는 모습
- **실용성**: 실제 연구 환경에서 바로 사용 가능한 방법론
- **효과성**: 연구 생산성 및 품질 향상 명확히 입증
- **접근성**: 코딩 지식 없이도 활용 가능한 수준

---

**Version**: v13.0 Part 3 Screenshot Guide  
**Last Updated**: 2025-11-13  
**Next Review**: v13.1 업데이트 시
