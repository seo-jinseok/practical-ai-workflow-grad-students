# GitHub Projects 설정 가이드

이 문서는 GitHub Projects 시연을 위한 설정 가이드입니다.

## 사전 준비 (강의 1주일 전)

### 1. GitHub 계정 및 저장소 준비

```bash
# 1. GitHub 계정 생성 (없는 경우)
# https://github.com/signup

# 2. 테스트 저장소 생성
# 저장소명: thesis-project-demo
# 설명: 석사 논문 프로젝트 관리 데모
# Public 또는 Private

# 3. 로컬에 클론
git clone https://github.com/[username]/thesis-project-demo.git
cd thesis-project-demo

# 4. SPEC.md 파일 추가

# 방법 1: Raw URL에서 직접 복사 (온라인에서 바로 사용)
curl -L https://raw.githubusercontent.com/your-username/your-repo/main/demo-files/03-github-projects/SPEC.md -o SPEC.md
git add SPEC.md
git commit -m "Add project specification"
git push

# 방법 2: 로컬에서 복사 (이 저장소를 이미 클론한 경우)
# 현재 디렉토리에서 이 파일과 같은 위치에 있는 경우
cp ../demo-files/03-github-projects/SPEC.md .
git add SPEC.md
git commit -m "Add project specification"
git push
```

### 2. GitHub Projects 설정

**웹 인터페이스에서**:
1. 저장소 페이지 → Projects 탭 클릭
2. "New project" 버튼 클릭
3. Template 선택: "Board" (Kanban 스타일)
4. 프로젝트명: "석사 논문 작성"
5. "Create project" 클릭

### 3. 작업(Issues) 생성

**수동으로 Issues 생성** (시연용):

```markdown
# Issue 1: 문헌 고찰 계획 수립
- Labels: Phase 1, High Priority
- Milestone: M1 (4월 말)
- Assignee: 본인
- Description: 문헌 검색 전략 수립, 키워드 선정, 데이터베이스 선정

# Issue 2: 문헌 검색 및 수집
- Labels: Phase 1, High Priority
- Milestone: M1
- Description: 관련 논문 50편 수집

# Issue 3: 문헌 읽기 및 요약
- Labels: Phase 1, High Priority
- Milestone: M1
- Description: 각 논문 요약, 주제별 분류

# Issue 4: 문헌 고찰 초안 작성
- Labels: Phase 1, High Priority
- Milestone: M1
- Description: 문헌 고찰 섹션 초안 (15-20페이지)

# Issue 5: 연구 설계 구체화
- Labels: Phase 1, High Priority
- Milestone: M1
- Description: 연구 방법, 대상, 도구 구체화

# ... (총 20-30개 Issues)
```

### 4. 프로젝트 보드 구성

**컬럼 설정**:
1. 📝 To Do (예정)
2. 🔄 In Progress (진행중)
3. 👀 Review (검토중)
4. ✅ Done (완료)

**Issues를 보드에 추가**:
- 모든 Issues를 "To Do" 컬럼에 배치
- 우선순위 순으로 정렬
- 의존성 관계 표시 (Issue 설명에 명시)

## 🎬 시연 시나리오

### 1단계: Spec 문서 보여주기 (1.5분)

**화면**: GitHub 저장소의 SPEC.md 파일

**강사 멘트**:
"이것이 우리가 Part 2에서 배운 Spec 문서입니다.
목표, 범위, 일정, 산출물이 명확히 정의되어 있습니다.
이제 이 Spec을 실제 프로젝트 관리로 연결해보겠습니다."

### 2단계: Projects 보드 보여주기 (2분)

**화면**: GitHub Projects 보드 (Kanban 뷰)

**강사 멘트**:
"Spec 문서를 바탕으로 작업들을 Issues로 만들었습니다.
보시다시피 To Do, In Progress, Review, Done 컬럼으로 구성되어 있습니다.
각 작업에는 라벨, 마일스톤, 담당자가 할당되어 있습니다."

**시연 액션**:
1. Issue 하나를 클릭하여 상세 내용 보여주기
2. 체크리스트 확인
3. 예상 소요 시간 확인
4. 의존성 관계 설명

### 3단계: 작업 이동 시연 (1분)

**강사 멘트**:
"실제로 작업을 시작하면 이렇게 이동합니다."

**시연 액션**:
1. Issue 1개를 "To Do"에서 "In Progress"로 드래그
2. 체크리스트 일부 체크
3. 코멘트 추가 (진행 상황 기록)
4. "이렇게 시각적으로 진행 상황을 관리합니다"

### 4단계: 전체 뷰 보여주기 (0.5분)

**화면**: Roadmap 뷰 또는 Table 뷰

**강사 멘트**:
"다양한 뷰로 전환할 수 있습니다.
Roadmap 뷰는 타임라인을 보여주고,
Table 뷰는 스프레드시트처럼 관리할 수 있습니다.
여러분의 선호에 맞게 선택하세요."

## 🎯 강조 포인트

### 시연 중 반드시 언급

1. **Spec의 중요성**
   - "Spec 문서가 모든 것의 중심입니다"
   - "명확한 Spec이 있어야 작업 분해가 가능합니다"

2. **시각적 관리**
   - "한눈에 전체 프로젝트 상황을 파악할 수 있습니다"
   - "어떤 작업이 막혀있는지 즉시 알 수 있습니다"

3. **협업 용이성**
   - "지도교수님과 공유하면 진행 상황을 투명하게 보여줄 수 있습니다"
   - "동료 연구자와 공동 연구 시 특히 유용합니다"

4. **도구 중립성**
   - "GitHub Projects가 유일한 선택은 아닙니다"
   - "Notion, Trello, Linear 등 다양한 대안이 있습니다"
   - "중요한 것은 Spec-driven 접근 방식입니다"

## 🔄 백업 계획

### 시연 실패 시나리오

**인터넷 끊김**:
- screenshots/ 폴더의 스크린샷으로 설명
- "미리 준비한 화면으로 보여드리겠습니다"

**GitHub 접속 오류**:
- 로컬 스크린샷 사용
- "실제로는 이렇게 보입니다"

**시간 부족**:
- 2단계와 3단계만 집중
- 4단계 생략 가능

## 📸 스크린샷 준비 목록

### 필수 스크린샷
1. `01-spec-document.png`: SPEC.md 파일 전체
2. `02-projects-board-overview.png`: 전체 보드 뷰
3. `03-issue-detail.png`: Issue 상세 화면
4. `04-issue-moving.png`: Issue 이동 중
5. `05-roadmap-view.png`: Roadmap 뷰
6. `06-table-view.png`: Table 뷰

### 선택적 스크린샷
7. `07-milestone-view.png`: 마일스톤 진행 상황
8. `08-labels-view.png`: 라벨 관리
9. `09-insights.png`: 프로젝트 인사이트

## 🎥 녹화 영상 스크립트

**영상 길이**: 3분

**내용**:
1. Spec 문서 보여주기 (30초)
2. Projects 보드 전체 뷰 (30초)
3. Issue 상세 및 이동 (1분)
4. 다양한 뷰 전환 (30초)
5. 마무리 멘트 (30초)

**나레이션**:
"Spec 문서를 바탕으로 GitHub Projects에서 작업을 관리합니다.
각 작업은 Issue로 만들어지고, 보드에서 시각적으로 관리됩니다.
작업을 드래그하여 진행 상황을 업데이트할 수 있습니다.
이렇게 전체 프로젝트를 한눈에 파악하고 관리할 수 있습니다."