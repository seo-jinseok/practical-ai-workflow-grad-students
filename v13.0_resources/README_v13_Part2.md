# Part 2 고급 도구 리소스 가이드

**Version**: v13.0 Part 2  
**Date**: 2025-11-10  
**Target**: 대학원생 (코딩 지식 불필요, Part 1 완료)  
**Related**: [메인 Part 2 문서](../Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md)

---

## 📋 Part 2 리소스 파일 전체 인덱스

### 🎯 목적
이 디렉터리는 **Part 2: 고급 도구 편**에 필요한 모든 리소스 파일을 체계적으로 정리한 것입니다. Part 1의 기초를 바탕으로 고급 도구들을 실제 연구에 적용하는 데 필요한 구체적인 가이드와 템플릿을 제공합니다.

### 📁 파일 구조

```
v13.0_resources/
├── Part 1 관련 파일들 (01-11)
├── 📚 Part 2 전용 파일들
│   ├── 12_copilot_workbook_exercises.md    (GitHub Copilot 워크북 4개 Exercise)
│   ├── 15_mcp_installation_guide.md        (MCP 설치 및 설정 가이드)
│   ├── 19_speckit_installation_guide.md    (SpecKit 설치 가이드)
│   └── README_v13_Part2.md                 (이 파일 - Part 2 리소스 인덱스)
```

### 🗂️ Part 2 리소스 파일 상세 설명

#### 📖 12_copilot_workbook_exercises.md
**GitHub Copilot 심화 워크북 - 4개 Exercise**  
**예상 소요 시간**: 2-3시간  
**대상**: 모든 전공의 연구자  
**내용**:
- **Exercise 1**: 문헌 조사 자동화 (30-45분)
- **Exercise 2**: 연구 계획서 작성 (30-45분)  
- **Exercise 3**: 데이터 분석 스크립트 (30-45분)
- **Exercise 4**: 논문 작성 지원 (30-45분)

**사용법**: 메인 Part 2 문서 Section 2와 함께 사용

---

#### 🔧 15_mcp_installation_guide.md
**MCP (Model Context Protocol) 설치 및 실용 가이드**  
**예상 소요 시간**: 1-2시간  
**대상**: 도구 통합에 관심 있는 연구자  
**내용**:
- Claude Desktop 설치 (macOS, Windows)
- task-master-mcp 4개 실습 (총 20분)
- 연구자용 MCP 서버 4종 (arxiv, zotero, notion, jupyter)
- 전공별 MCP 조합 추천
- 트러블슈팅 및 대안 도구

**사용법**: 메인 Part 2 문서 Section 4와 함께 사용

---

#### ⚙️ 19_speckit_installation_guide.md
**GitHub SpecKit 워크플로우 가이드**  
**예상 소요 시간**: 1시간  
**대상**: 체계적 연구 계획을 원하는 고급 사용자  
**내용**:
- SpecKit 설치 및 환경 구축
- 7단계 워크플로우 (Research 버전)
- 실습: 간단한 연구 프로젝트에 적용
- SpecKit vs 전통적 방법 비교 분석

**사용법**: 메인 Part 2 문서 Section 5와 함께 사용

---

## 🎓 학습 순서 가이드

### 🛤️ 순차 학습 (추천: 초보자)

```
1주차: 기초 도구 숙달
   → 12_copilot_workbook_exercises.md (Exercise 1-2)
   → Part 2 메인 문서 Section 2 완료

2주차: 고급 활용
   → 12_copilot_workbook_exercises.md (Exercise 3-4)
   → 15_mcp_installation_guide.md (task-master-mcp까지)

3주차: 도구 통합
   → 15_mcp_installation_guide.md (연구자용 서버)
   → 19_speckit_installation_guide.md (선택적)

4주차: 실전 적용
   → 실제 연구 프로젝트에 모든 도구 적용
   → Part 2 메인 문서 Section 6-7 완료
```

### 🎯 선택 학습 (중급자 이상)

**관심사별 빠른 접근**:

- **문서 작성 자동화 관심**: `12_copilot_workbook_exercises.md` 먼저
- **도구 통합 관심**: `15_mcp_installation_guide.md` 먼저  
- **체계적 계획 관심**: `19_speckit_installation_guide.md` 먼저

---

## 🔗 메인 문서와의 연동

### 📍 각 리소스 파일의 연결 위치

| 리소스 파일 | 메인 문서 연결 위치 | 목적 |
|-------------|-------------------|------|
| `12_copilot_workbook_exercises.md` | Section 2 끝부분 | 워크북 실습深化 |
| `15_mcp_installation_guide.md` | Section 4 끝부분 | MCP 실용 가이드 |
| `19_speckit_installation_guide.md` | Section 5 끝부분 | SpecKit 상세 가이드 |
| `README_v13_Part2.md` | 문서 전체, Section 7 | Part 2 전체 인덱스 |

### 🔄 상호 참조 구조

```
메인 Part 2 문서
    ↓ (링크)
리소스 파일들 (상세 가이드)
    ↓ (참조)
메인 Part 2 문서 (적용 및 통합)
```

---

## 🎯 각 파일의 예상 결과물

### 12_copilot_workbook_exercises.md 완료 후
- [ ] `literature-search.md`: 검색 키워드 + 논문 요약 템플릿
- [ ] `research-proposal.md`: 연구 계획서 초안
- [ ] `data-analysis.py`: 데이터 분석 스크립트 (또는 Excel 대안)
- [ ] `paper-draft.md`: 논문 초안 (Methods + Results)

### 15_mcp_installation_guide.md 완료 후
- [ ] Claude Desktop + MCP 환경 구축
- [ ] task-master-mcp로 연구 프로젝트 관리 시작
- [ ] 연구자용 MCP 서버 1-2개 설치 및 테스트
- [ ] 개인 연구에 최적화된 MCP 조합 파악

### 19_speckit_installation_guide.md 완료 후
- [ ] SpecKit 설치 및 기본 사용법 습득
- [ ] 7단계 워크플로우 1회 완주
- [ ] 간단한 연구 프로젝트에 SpecKit 적용
- [ ] 전통적 방법 대비 SpecKit의 장점 체감

---

## ❓ 자주 묻는 질문 (FAQ)

### Q1: Part 1을 완료하지 않았는데 Part 2를 시작해도 되나요?
**A**: 기본적인 Markdown과 AI 사용 경험을 권장합니다. Part 1의 핵심 개념을 복습한 후 Part 2를 시작하세요.

### Q2: 3개 파일을 모두 해야 하나요?
**A**: 아닙니다. 개인의 연구 필요와 관심사에 따라 선택하세요. 최소 `12_copilot_workbook_exercises.md`을 권장합니다.

### Q3: 코딩 경험이 없어도 SpecKit을 사용할 수 있나요?
**A**: 가능하지만 Torture 테스트가 될 수 있습니다. 먼저 `12_copilot_workbook_exercises.md`와 `15_mcp_installation_guide.md`를 완료한 후 SpecKit을 시도하세요.

### Q4: 파일 다운로드나 별도 설치가 필요한가요?
**A**: 모든 파일은 Markdown 형식으로 제공되며, VS Code나 일반 텍스트 에디터로 열 수 있습니다. Copilot, MCP, SpecKit은 각 가이드에 따라 별도 설치가 필요합니다.

### Q5: Part 2를 완료한 후 다음 단계는?
**A**: Part 3 (통합 워크플로우 편)에서 Part 1-2의 모든 도구를 실제 연구에 완전 통합하는 방법을 배우게 됩니다.

---

## 📞 추가 지원 및 피드백

### 🆘 문제 해결
- **설치 문제**: 각 파일의 트러블슈팅 섹션 참조
- **사용법 문제**: 메인 Part 2 문서의 해당 섹션 참조
- **AI 도구 문제**: Part 1의 기본 개념 복습

### 💬 피드백 및 개선 제안
- 각 파일의 마지막 섹션에 피드백 양식 제공
- 연구 분야별 활용 사례 공유 환영
- 개선사항이나 새로운 도구 발견 시 공유

### 🌐 관련 링크
- **Part 1 리소스**: `README_v13_Part1.md`
- **메인 Part 2 문서**: `../Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md`
- **최신 업데이트**: [GitHub 저장소](링크)

---

## 🏁 시작하기

 Part 2 고급 도구 학습을 시작하려면:

1. **목표 설정**: 어떤 도구에 가장 관심이 있는지 파악
2. **준비물 확인**: 필요한 소프트웨어 및 계정 준비
3. **학습 경로 선택**: 순차 학습 vs 선택 학습
4. **시작**: 관심 있는 리소스 파일부터 시작

**각 파일은 독립적으로도 사용할 수 있도록 설계되었지만, 메인 Part 2 문서와 함께使用时 효과를 극대화할 수 있습니다.**

---

**Version**: v13.0 Part 2 Resources  
**Last Updated**: 2025-11-10  
**Next**: [메인 Part 2 문서](../Practical_AI_Workflow_for_Grad_Students v13.0_Part2.md)  
**Previous**: [Part 1 Resources](README_v13_Part1.md)
