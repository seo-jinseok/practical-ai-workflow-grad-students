# 연구자용 MCP 서버 모음

## 목적
- 연구자 전용 Model Context Protocol (MCP) 서버 소개
- 각 서버별 기능과 연구 활용 방법
- AI 도구 통합을 통한 연구 효율성 향상

## 연구용 MCP 서버 목록

### 1. Task Master Server
- **기능**: AI 기반 작업 관리 및 프로젝트 추적
- **연구 활용**: 논문 작성, 연구 계획 관리, 마일스톤 추적
- **연동 도구**: `16_task_master_mcp_tutorial.md` 참조

### 2. Literature Search Server
- **기능**: 학술 문헌 검색 및 요약 자동화
- **연구 활용**: 문헌 리뷰, 키워드 기반 논문 검색
- **활용법**: 연구 주제 관련 논문 자동 수집 및 분류

### 3. Data Analysis Server
- **기능**: 연구 데이터 분석 및 시각화 지원
- **연구 활용**: 통계 분석, 그래프 생성, 결과 해석
- **특징**: Python/R 코드 자동 생성 및 실행

### 4. Writing Assistant Server
- **기능**: 학술 논문 작성 및 수정 지원
- **연구 활용**: 논문 초안 작성, 참고문헌 관리, 논리 구조 개선
- **AI 모델**: 최신 GPT-4, Claude, Gemini 통합

### 5. Collaboration Server
- **기능**: 연구팀 협업 및 파일 공유
- **연구 활용**: 다기관 연구, 국제 협력, 버전 관리
- **특징**: 실시간 문서 협업 및 피드백 시스템

## 설치 및 설정

### 기본 설정 단계
1. **MCP 설치**: `part2/15_mcp_installation_guide.md` 참조
2. **서버 추가**: 필요한 서버들을 MCP 설정에 추가
3. **API 키 설정**: 각 서버별 필요한 인증 정보 입력
4. **연동 테스트**: VS Code에서 각 서버 기능 테스트

### 연구 프로젝트별 권장 조합

#### 문헌 리뷰 프로젝트
- Literature Search Server + Writing Assistant Server
- Task Master Server (작업 관리)

#### 실험 연구 프로젝트
- Data Analysis Server + Task Master Server
- Collaboration Server (팀 협업)

#### 논문 작성 프로젝트
- Writing Assistant Server + Task Master Server
- Literature Search Server (인용 관리)

## 활용 팁

### 효과적인 사용법
- **서버별 전문성 활용**: 각 서버의 장점을 극대화
- **연속적 워크플로우**: 여러 서버를 연결하여 통합 활용
- **정기적 업데이트**: 서버 기능 및 모델 업데이트 확인

### 문제 해결
- **연동 오류**: `23_part2_troubleshooting.md` 참조
- **성능 최적화**: 서버 설정 조정 및 리소스 관리
- **보안 고려**: 연구 데이터 보호 및 접근 권한 관리

## 관련 리소스
- **MCP 설치**: `part2/15_mcp_installation_guide.md`
- **Task Master**: `16_task_master_mcp_tutorial.md`
- **학문별 조합**: `18_mcp_discipline_combinations.md`
- **SpecKit 연동**: `20_speckit_research_workflow.md`

---
**마지막 업데이트**: 2025-11-11  
**버전**: Part 2
