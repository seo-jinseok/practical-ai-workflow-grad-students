# SpecKit 실습 프로젝트 가이드

## 목적
- SpecKit 실습을 위한 단계별 프로젝트 가이드
- 실제 연구 프로젝트를 통한 SpecKit 워크플로우 체험
- 5분 시연용 프로젝트 설계

## 프로젝트 개요
**주제**: 온라인 학습 참여도 조사 연구  
**기간**: 4주 실습 프로젝트  
**방법론**: 설문 조사 및 간단한 정량 분석  
**산출물**: 연구 계획서 및 기본 분석 결과  

## 시연 시나리오

### 연구 주제
- **주문제목**: "대학생의 온라인 학습 참여도에 대한 조사 연구"
- **연구목적**: COVID-19 이후 온라인 학습 환경 변화 파악
- **연구대상**: 대학생 1-4학년 (n=200 목표)

### SpecKit 7단계 워크플로우 적용

#### 1. Constitution 설정
- **연구 원칙**: 윤리적 연구, 투명성, 재현성
- **가이드라인**: 학생 대상 설문 시 고려사항
- **품질 기준**: 데이터 신뢰성 및 윤리 준수

#### 2. Spec 문서 작성
- **연구목표**: 온라인 학습 참여도 요인 분석
- **방법론**: 설문 조사 (Cronbach's α 신뢰도)
- **일정**: 4주 실행 계획 ( literature review → 설문 설계 → 수집 → 분석)

#### 3. Plan/Tasks 자동 생성
- **작업분해**: 구체적인 연구 단계별 과제
- **마일스톤**: 주간별 완료 목표
- **의존성**: 선행 작업 및 자원 요구사항

## 실습 단계별 가이드

### Week 1: 프로젝트 설정
- **Day 1-2**: Constitution 및 Spec 문서 작성
- **Day 3-4**: 문헌 고찰 (최소 10편)
- **Day 5**: 주간 점검 및 계획 조정

### Week 2: 설문 설계
- **Day 1-2**: 설문 문항 개발
- **Day 3-4**: 파일럿 테스트
- **Day 5**: 최종 설문 완성

### Week 3: 데이터 수집
- **Day 1-3**: 설문 배포 및 응답 수집
- **Day 4-5**: 데이터 정제 및 검증

### Week 4: 분석 및 보고
- **Day 1-3**: 기초 통계 분석
- **Day 4-5**: 결과 정리 및 최종 보고서

## SpecKit 명령어 실습

### 설치 및 초기화
```bash
# Python 3.11+ 확인
python --version

# SpecKit CLI 설치
uv tool install specify-cli

# 프로젝트 초기화
specify init online-learning-study
cd online-learning-study
```

### 문서 작성
```bash
# Constitution 작성
specify constitution

# Spec 문서 생성
specify spec

# Plan 및 Tasks 자동 생성
specify plan
specify tasks

# 진행 상황 업데이트
specify update
```

## 데모 파일 활용

### 예시 파일 참조
- **시나리오**: `../Context_and_Planning/demo-files/07-speckit-practice/demo-scenario.md`
- **Constitution**: `../Context_and_Planning/demo-files/07-speckit-practice/constitution-example.md`
- **Spec 예시**: `../Context_and_Planning/demo-files/07-speckit-practice/spec-example.md`
- **Plan 예시**: `../Context_and_Planning/demo-files/07-speckit-practice/plan-example.md`
- **Tasks 예시**: `../Context_and_Planning/demo-files/07-speckit-practice/tasks-example.md`

### 터미널 명령어
- **설치**: `../Context_and_Planning/demo-files/07-speckit-practice/terminal-commands.md`
- **체크리스트**: `../Context_and_Planning/demo-files/07-speckit-practice/setup-checklist.md`

## 대안 도구

### 간단한 프로젝트용
- **Markdown + AI**: `13_spec_driven_planning_guide.md` 참조
- **Notion 템플릿**: 연구 계획서 양식
- **Google Docs**: 협업 기반 문서 작성
- **Trello/Asana**: 작업 관리 도구

### 언제 대안을 사용할까?
- **개인 연구**: 간단한 1-2주 프로젝트
- **초보자**: 터미널 친숙도 낮을 때
- **팀 협업 미필요**: 단순한 연구 목표
- **시간 절약**: 빠른 프로젝트 수행 시

## 성과 평가

### 체크리스트
- [ ] Constitution 원칙 3개 이상 정의
- [ ] Spec 문서 핵심 섹션 완성
- [ ] Plan에서 주간별 마일스톤 설정
- [ ] Tasks에서 15개 이상 구체적 과제 분해
- [ ] 4주 내 연구 계획서 완성

### AI 도구 활용 평가
- [ ] Copilot을 통한 문서 작성
- [ ] Task Master와 연동한 진행 추적
- [ ] Literature Search Server 활용
- [ ] AI-assisted 분석 및 시각화

## 문제 해결

### 일반적 오류
- **Python 버전**: 3.11+ 필요 확인
- **터미널 권한**: 관리자 권한 필요 시
- **依赖 패키지**: uv 또는 pip로 설치

### 대안 제시
- **설치 실패**: 데모 파일로 개념 설명
- **명령어 오류**: 스크린샷으로 시연 대체
- **시간 부족**: 핵심 개념만 시연

## 관련 리소스
- **SpecKit 설치**: `part2/19_speckit_installation_guide.md`
- **연구 워크플로우**: `20_speckit_research_workflow.md`
- **데모 파일**: `../Context_and_Planning/demo-files/07-speckit-practice/`
- **터미널 가이드**: `../Context_and_Planning/demo-files/07-speckit-practice/terminal-commands.md`

---
**마지막 업데이트**: 2025-11-11  
**버전**: v13.0  
**데모 파일 출처**: `../Context_and_Planning/demo-files/07-speckit-practice/`
