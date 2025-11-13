# v13.0 릴리스 체크리스트
## 최종 배포 전 확인 사항

**목적**: v13.0 교재 및 리소스의 최종 품질 확인  
**대상**: 강의 담당자, 콘텐츠 제작자  
**사용 시점**: 강의 1주일 전  
**완료 목표**: 모든 항목 체크 완료  

---

## 📄 문서 완성도 확인

### 메인 문서 (3개)
- [ ] **Part 1** (`v13.0_Part1.md`): 2,224 lines, 7 sections 완성
  - [ ] Section 1-7 모두 작성 완료
  - [ ] [SCREENSHOT: ...] 플레이스홀더 문서화
  - [ ] 실습 체크리스트 동작 확인
  
- [ ] **Part 2** (`v13.0_Part2.md`): 1,845 lines, 7 sections 완성
  - [ ] Section 1-7 모두 작성 완료
  - [ ] Copilot Workbook 4개 Exercise 완성
  - [ ] MCP/ SpecKit 실습 가이드 완성
  
- [ ] **Part 3** (`v13.0_Part3.md`): 2,635+ lines, 11 sections 완성
  - [ ] Section 1-11 모두 작성 완료
  - [ ] 5개 전공 시나리오 완성 (Sections 2-6)
  - [ ] 2025 도구 생태계 가이드 완성

- [ ] **모든 섹션 번호 순차적**
  - [ ] Part 1: 1-7 순차 확인
  - [ ] Part 2: 1-7 순차 확인  
  - [ ] Part 3: 1-11 순차 확인
  
- [ ] **모든 목차 정확**
  - [ ] 목차와 실제 섹션 제목 일치
  - [ ] 페이지 내비게이션 링크 작동
  
- [ ] **모든 헤더/푸터 일관성**
  - [ ] 버전 번호: v13.0 Part [N] 일관
  - [ ] 날짜: 2025-11-10 일관
  - [ ] 교차 링크: Part 간 참조 정확

### 리소스 파일 (43+ 개)
- [ ] **Part 1 리소스 (01-11)**: 11개 파일 완성
  - [ ] 01: GitHub Copilot Student Guide
  - [ ] 02: VS Code Setup Checklist  
  - [ ] 03: Folder Structure Templates
  - [ ] 04: Context Template 2025
  - [ ] 05: Markdown Quick Reference
  - [ ] 06: AI Models Comparison
  - [ ] 07: Copilot Chat Examples
  - [ ] 08: MCP Introduction Slides
  - [ ] 09: Troubleshooting Guide
  - [ ] 10: Discipline Examples
  - [ ] 11: Screenshot Descriptions (26개 문서화)

- [ ] **공유 리소스 (13-23, 38-43)**: 21개 파일 완성
  - [ ] 13: Spec-driven Planning Guide
  - [ ] 14: Research Spec Template 2025
  - [ ] 16: Task Master MCP Tutorial
  - [ ] 17: Researcher MCP Servers
  - [ ] 18: MCP Discipline Combinations
  - [ ] 20: SpecKit Research Workflow
  - [ ] 21: SpecKit Practice Project
  - [ ] 22: Integrated Workflow Example
  - [ ] 23: Part2 Troubleshooting
  - [ ] 38: Workflow Automation Templates
  - [ ] 39: AI Assistant Prompt Library
  - [ ] 40: Research Methodology Comparison
  - [ ] 41: Project Timeline Templates
  - [ ] 42: Collaboration Workflows
  - [ ] 43: AI Tools Roadmap 2025

- [ ] **Part 2 리소스 (part2/)**: 3개 파일 완성
  - [ ] 12: Copilot Workbook Exercises
  - [ ] 15: MCP Installation Guide
  - [ ] 19: SpecKit Installation Guide

- [ ] **Part 3 리소스 (part3/)**: 14개 파일 완성
  - [ ] 25: 2025 Research Tools Ecosystem
  - [ ] 26: Education Complete Scenario
  - [ ] 27-29: Other Discipline Scenarios
  - [ ] 30: Literature Review 2025 Workflow
  - [ ] 31: Weekly/Monthly Routines
  - [ ] 32: Progress Tracking Methods
  - [ ] 33: Problem Solving Protocol
  - [ ] 34: Quality Checklist
  - [ ] 35: Folder Structure Examples
  - [ ] 36: Success Stories
  - [ ] 37: Part3 Troubleshooting

- [ ] **모든 파일 번호 일관성**
  - [ ] Leading zeros 일관 (01, 02, 03...)
  - [ ] 파일명 규칙 일치
  
- [ ] **모든 파일 푸터 일관성**
  - [ ] "업데이트: 2025-11-10 기준"
  - [ ] "다음 확인: 2025-12월"

### README 파일 (4개)
- [ ] **Master README**: 완성, 43+ 파일 인덱싱
  - [ ] 전체 파일 구조 정확
  - [ ] 6개 퀵스타트 경로 검증
  - [ ] 학습 경로 가이드 완성
  
- [ ] **README_Part1.md**: 완성
  - [ ] Part 1 관련 파일 11개 모두列出
  - [ ] 학습 순서 가이드 완성
  
- [ ] **README_Part2.md**: 완성
  - [ ] Part 2 관련 파일 모두列出
  - [ ] 실습 준비 체크리스트 완성
  
- [ ] **README_Part3.md**: 완성
  - [ ] Part 3 관련 파일 모두列出
  - [ ] 시나리오별 학습 가이드 완성
  
- [ ] **모든 README 상호 링크 정확**
  - [ ] Master → Part READMEs 링크
  - [ ] Part → 메인 문서 링크
  - [ ] 리소스 파일 간 상호 링크

### 데모 파일 (8개 폴더)
- [ ] **01-04 기존 데모**: 검증 완료
  - [ ] 01-vscode-markdown: 정상 작동
  - [ ] 02-github-copilot: Student 혜택 확인
  - [ ] 03-github-projects: 워크플로우 검증
  - [ ] 04-task-master-mcp: MCP 서버 연결 확인
  
- [ ] **05 Copilot 워크북**: 완성
  - [ ] 4개 Exercise 모두 완성
  - [ ] starter/answer 파일 쌍 완성
  - [ ] 프롬프트/응답 예시 검증
  
- [ ] **06 MCP 설치**: 완성
  - [ ] 설치 스크립트 작동 확인
  - [ ] 설정 템플릿 검증
  - [ ] 문제 해결 가이드 완성
  
- [ ] **07 SpecKit 실습**: 완성
  - [ ] 7단계 워크플로우 검증
  - [ ] terminal-commands 작동 확인
  - [ ] 예시 프로젝트 완성
  
- [ ] **08 통합 워크플로우**: 완성
  - [ ] 전체 연구 프로세스 검증
  - [ ] 주간 타임라인 완성
  - [ ] AI 프롬프트 예시 검증
  
- [ ] **모든 데모 README 완성**
  - [ ] 각 데모별 목적/시간/대상 명시
  - [ ] 단계별 실습 가이드 완성
  
- [ ] **rehearsal-guide.md 업데이트**
  - [ ] 8개 데모 전체 리허설 계획
  - [ ] 시간 배분 (각 5분 × 8개 = 40분)
  - [ ] 백업 시나리오 포함
  
- [ ] **demo-cheatsheet.md 업데이트**
  - [ ] 데모별 핵심 단축키
  - [ ] 문제 해결 빠른 참조
  
- [ ] **backup-plan.md 업데이트**
  - [ ] 기술 실패 시 대안 계획
  - [ ] 스크린샷 백업 접근 방법
  - [ ] 비디오 백업 준비 (선택적)
  
- [ ] **v13.0-master-demo-script.md 완성**
  - [ ] 전체 데모 통합 스크립트
  - [ ] 40분 데모 완성 가이드
  - [ ] 전환 시점 및 타이밍 명시

---

## ✅ 품질 기준 확인

### 헌장 준수 (Constitution v1.1.2)
- [ ] **학습자 중심 설계**: 실용적, 즉시 적용 가능
  - [ ] 구체적 예시와 시나리오 포함
  - [ ] 실제 연구 상황에 적용 가능
  - [ ] 단계별 명확한 지침

- [ ] **문서 우선 기획**: 모든 내용 Markdown
  - [ ] Word/기타 형식 없음
  - [ ] 마크다운 문법 일관
  - [ ] VS Code에서 편집 가능

- [ ] **점진적 기술 습득**: Part 1 → 2 → 3 구조
  - [ ] Part 1: 기초 + 실습 환경
  - [ ] Part 2: 고급 도구 + 실습
  - [ ] Part 3: 통합 + 실제 적용

- [ ] **실시간 도구 시연**: 8개 데모 준비
  - [ ] 각 데모별 시연 시간 3-5분
  - [ ] 백업 파일 및 스크린샷 준비
  - [ ] 예상 문제점 및 해결법 준비

- [ ] **이중언어 명확성**: 한국어 격식체 + 영문 용어
  - [ ] "Term (한국어 설명)" 패턴 일관
  - [ ] "~합니다, ~하세요" 격식체 유지
  - [ ] 기술 용어 적절한 번역

- [ ] **무료 도구**: 모든 도구 학생 무료 또는 무료 티어
  - [ ] GitHub Copilot: Student Pro 무료
  - [ ] GitHub Education Pack: 무료
  - [ ] MCP: 오픈소스
  - [ ] SpecKit: 무료
  - [ ] 2025 도구: 무료 티어 확인

- [ ] **접근성**: 코딩 지식 불필요
  - [ ] 모든 코드에 한국어 설명
  - [ ] 비코더 대안 제공
  - [ ] 단계별 상세 설명

- [ ] **다학제**: 5개 전공 균형
  - [ ] 인문학: 충분한 예시
  - [ ] 사회과학: 충분한 예시
  - [ ] 자연과학: 충분한 예시
  - [ ] 공학: 충분한 예시
  - [ ] 예체능: 충분한 예시

### 내용 일관성
- [ ] **용어 통일**
  - [ ] Context Engineering: 일관된 사용
  - [ ] Spec-driven Planning: 일관된 사용
  - [ ] MCP: Model Context Protocol으로 최초 사용 시 풀어쓰기
  - [ ] SpecKit: 일관된 사용
  
- [ ] **이모지 계층 일관성**
  - [ ] 🎯 (목표/목적)
  - [ ] 📝 (작성/문서)
  - [ ] 🔍 (검색/조사)
  - [ ] 💡 (팁/아이디어)
  - [ ] ⚠️ (주의/경고)
  - [ ] ✅ (완료/성공)
  - [ ] 🚀 (다음 단계/진행)
  - [ ] 📊 (분석/데이터)
  - [ ] 🏆 (성과/달성)

- [ ] **이중언어 형식 일관성**
  - [ ] 첫 사용: "English Term (한국어 설명: 상세 설명)"
  - [ ] 이후 사용: "English Term" 또는 "한국어"
  - [ ] 예시: "Agent mode (에이전트 모드: AI가 자동으로 여러 단계 작업 수행)"

- [ ] **격식체 일관성**
  - [ ] "~합니다" 사용
  - [ ] "~하세요" 사용
  - [ ] "여러분" 주소 형식
  - [ ] "~입니다" 종결 어미

- [ ] **섹션 번호 일관성**
  - [ ] Part 1: 1-7 순차
  - [ ] Part 2: 1-7 순차
  - [ ] Part 3: 1-11 순차
  - [ ] 리소스: 01-43 leading zeros

### 링크 검증
- [ ] **모든 내부 링크 작동**
  - [ ] Part 간 참조 정확
  - [ ] Part → 리소스 참조 정확
  - [ ] 리소스 → 데모 참조 정확
  - [ ] README → 파일 참조 정확

- [ ] **모든 외부 링크 작동**
  - [ ] GitHub Copilot: https://github.com/features/copilot
  - [ ] GitHub Education: https://education.github.com/
  - [ ] VS Code: https://code.visualstudio.com/
  - [ ] Claude Desktop: https://claude.ai/download
  - [ ] MCP: https://modelcontextprotocol.io/
  - [ ] SpecKit: https://github.com/github/spec-kit

- [ ] **모든 앵커 링크 정확**
  - [ ] 섹션 제목과 일치
  - [ ] 소문자 + 하이픈 형식
  - [ ] 스페이스 → 하이픈 변환

- [ ] **상대 경로 정확**
  - [ ] 절대 경로 (/Users/...) 없음
  - [ ] ./ ../ 적절한 사용
  - [ ] 폴더 구조와 일치

### 스크린샷 문서화
- [ ] **Part 1**: 26개 스크린샷 문서화 (11번 파일)
  - [ ] GitHub Education (4개) 문서화
  - [ ] VS Code setup (4개) 문서화
  - [ ] Copilot features (5개) 문서화
  - [ ] 2025 new features (5개) 문서화
  - [ ] MCP (2개) 문서화
  - [ ] Troubleshooting (3개) 문서화
  - [ ] Practice examples (3개) 문서화

- [ ] **Part 2**: 스크린샷 문서화 완료 (또는 계획)
  - [ ] Copilot workbook exercises 문서화 필요
  - [ ] MCP installation 문서화 필요
  - [ ] SpecKit workflow 문서화 필요

- [ ] **Part 3**: 스크린샷 문서화 완료 (또는 계획)
  - [ ] 2025 tools (Elicit, Perplexity 등) 문서화 필요
  - [ ] Integrated workflow 문서화 필요
  - [ ] Folder structures 문서화 필요

- [ ] **Demo 파일**: 스크린샷 체크리스트 완료
  - [ ] 8개 데모 폴더 체크리스트 확인
  - [ ] backup-plan.md 스크린샷 리스트 확인

- [ ] **모든 [SCREENSHOT: ...] 플레이스홀더 문서화**
  - [ ] Part 1: 26개 모두 문서화
  - [ ] Part 2: 플레이스홀더 → 문서로 변환 필요
  - [ ] Part 3: 플레이스홀더 → 문서로 변환 필요

### 전공별 균형
- [ ] **인문학**: 충분한 예시 (목표: 5+ 예시)
  - [ ] 문학, 역사학, 철학, 언어학 포함
  - [ ] Part 1-3 적절한 분배
  
- [ ] **사회과학**: 충분한 예시 (목표: 5+ 예시)
  - [ ] 교육학, 사회학, 심리학, 정치학, 경제학 포함
  - [ ] Part 2 Exercise 1-4 모두 사회과학 예시 포함
  
- [ ] **자연과학**: 충분한 예시 (목표: 5+ 예시)
  - [ ] 생명과학, 화학, 물리학, 지구과학 포함
  - [ ] Part 3 시나리오 포함
  
- [ ] **공학**: 충분한 예시 (목표: 5+ 예시)
  - [ ] 컴퓨터공학, 전기전자, 기계공학, 재료공학 포함
  - [ ] 코드 예시 및 시스템 개발 시나리오 포함
  
- [ ] **예체능**: 충분한 예시 (목표: 5+ 예시)
  - [ ] 음악학, 미술학, 체육학, 디자인 포함
  - [ ] Part 2 Exercise 및 Part 3 시나리오 포함
  
- [ ] **Part 3 시나리오**: 모든 전공 커버 (26-29번)
  - [ ] 26: 교육학 시나리오 완성
  - [ ] 27: 생명과학 시나리오 완성
  - [ ] 28: 컴퓨터공학 시나리오 완성
  - [ ] 29: 사회학 시나리오 완성
  - [ ] 음악학 시나리오 (Part 3 Section 6) 완성

### 코딩 지식 불필요
- [ ] **모든 코드 블록에 한국어 설명**
  - [ ] "이 코드는 ~을 합니다" 수준 이상
  - [ ] "이 코드는 다음을 수행합니다: 1) ..., 2) ..., 3) ..." 권장
  
- [ ] **설명 품질**: Level 2 이상 (구체적)
  - [ ] Level 3: "이 코드는 다음을 수행합니다: 1) X를 실행, 2) Y를 계산, 3) 결과를 Z에 저장"
  - [ ] Level 2: "이 코드는 데이터를 분석합니다" (최소 기준)
  - [ ] Level 1: "코드를 실행합니다" (피해야 할 수준)
  
- [ ] **대안 제공**: Excel/SPSS + AI 방법
  - [ ] 각 코드 예시에 비코더 대안 명시
  - [ ] "이 작업은 Excel에서 [기능명]으로도 가능하며, AI에게 '...'라고 물어보면 됩니다"
  
- [ ] **터미널 명령어 설명**
  - [ ] 각 명령어 목적 설명
  - [ ] 예상 결과 설명
  - [ ] 오류 발생 시 대안
  
- [ ] **JSON 설명** (비코더용)
  - [ ] "JSON이란 데이터를 저장하는 형식입니다"
  - [ ] 중괄호 {}, 대괄호 [], 쉼표 주의사항
  - [ ] 복사-붙여넣기 권장
  
- [ ] **"코딩 지식 불필요" 안심 문구**
  - [ ] 관련 섹션에 "코딩을 모르셔도 괜찮습니다" 포함
  - [ ] "이 예시는 참고용이며, 실제로는 AI가 도와줍니다" 포함
  - [ ] 초보자 친화적 어조 유지

### 최신 정보 (2025-11)
- [ ] **모든 "2025-10" → "2025-11" 업데이트**
  - [ ] 헌장: v1.1.2 (2025-11-10)
  - [ ] Part 1-3: 2025-11-10
  - [ ] 리소스: 2025-11-10 기준
  - [ ] README: 2025-11-11 (인덱스)
  - [ ] 데모 파일: 2025-11-10

- [ ] **헌장 날짜 업데이트**
  - [ ] ".specify/memory/constitution.md" v1.1.2
  - [ ] "2025년 10월" → "2025년 11월" 
  - [ ] "Last Amended: 2025-11-10"

- [ ] **도구 버전 최신**
  - [ ] GitHub Copilot: 2025년 11월 기준
  - [ ] SpecKit: v0.0.79+ (최신 확인)
  - [ ] MCP: 2025년 11월 기준
  
- [ ] **2025 도구 정보 최신**
  - [ ] Elicit, Perplexity, NotebookLM, Consensus, Scite, ResearchRabbit, Connected Papers, Semantic Scholar
  - [ ] 무료 티어 및 학생 할인 정보
  
- [ ] **AI 모델 정보 최신**
  - [ ] GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro, Grok Code Fast 1
  - [ ] 각 모델별 특화 작업

### 버전 메타데이터
- [ ] **모든 파일 버전 번호**: v13.0
  - [ ] 메인 문서: v13.0 Part [N]
  - [ ] 리소스: v13.0
  - [ ] README: v13.0 [Index/Part X Resources]

- [ ] **모든 파일 날짜**: 2025-11-10 (콘텐츠) 또는 2025-11-11 (인덱스)
  - [ ] 콘텐츠 파일: 2025-11-10
  - [ ] 인덱스/README: 2025-11-11
  
- [ ] **모든 헤더 메타데이터 완성**
  - [ ] 버전, 날짜, 대상, 목적, 소요시간 명시
  - [ ] 전제조건 (Part 2-3) 명시
  
- [ ] **모든 푸터 메타데이터 완성**
  - [ ] 버전, 날짜, 이전/다음 링크
  - [ ] 소요시간, 관련 리소스
  
- [ ] **교차 참조 일관성**
  - [ ] "Part 1 Section 3" 형식 일관
  - [ ] "resources/part2/12_..." 정확한 경로
  
- [ ] **파일명 규칙 일관**
  - [ ] v13.0_ 패턴 유지
  - [ ] Leading zeros (01, 02, 03...)
  - [ ] 언더스코어 (_) 일관 사용

---

## 🎓 강의 준비 확인

### 도구 설치 (강의 1주일 전)
- [ ] **VS Code 최신 버전**
  - [ ] v1.95+ 설치 확인
  - [ ] Windows: "Add to PATH" 체크
  - [ ] Extensions: GitHub Copilot 설치
  
- [ ] **GitHub Copilot 확장 설치 및 활성화**
  - [ ] Extensions Marketplace에서 설치
  - [ ] GitHub 계정 연결
  - [ ] Copilot Pro 활성화 (Student 혜택)
  
- [ ] **Claude Desktop 설치**
  - [ ] https://claude.ai/download
  - [ ] 시스템 요구사항 확인
  - [ ] 로그인 및 기본 설정
  
- [ ] **MCP 서버 설정** (task-master-mcp 최소)
  - [ ] Node.js 설치 확인
  - [ ] task-master-mcp 설치 및 테스트
  - [ ] 기본 설정 파일 생성
  
- [ ] **SpecKit 설치** (선택적)
  - [ ] GitHub SpecKit 저장소 클론
  - [ ] 설치 스크립트 실행
  - [ ] 7단계 워크플로우 테스트
  
- [ ] **모든 도구 작동 테스트**
  - [ ] 각 도구별 기본 기능 테스트
  - [ ] 데모 파일 실행 테스트
  - [ ] 예상 문제점 및 해결법 준비

### 데모 파일 준비 (강의 3일 전)
- [ ] **모든 데모 파일 테스트 실행**
  - [ ] 8개 데모 폴더 각각 실행
  - [ ] 예상 시간 내 완료 확인
  - [ ] 문제 발생 시 대안 준비
  
- [ ] **백업 파일 준비** (completed 버전)
  - [ ] 각 데모별 completed 파일 확인
  - [ ] 기술 실패 시 즉시 사용 가능
  - [ ] 스크린샷 백업 접근 방법 확인
  
- [ ] **스크린샷 캡처** (우선순위 높은 것부터)
  - [ ] Critical (Part 1 필수): GitHub Education, VS Code+Copilot, AI 모델 선택, Agent mode
  - [ ] Important (Part 2): MCP 설치, SpecKit 워크플로우, Copilot Workbook
  - [ ] Nice-to-have (Part 3): 2025 도구, 통합 워크플로우
  
- [ ] **데모 리허설** (각 5분 × 8개 = 40분)
  - [ ] 전체 데모 40분 내 완료
  - [ ] 각 데모별 전환 시간 포함
  - [ ] 예상 질문 및 답변 준비
  
- [ ] **타이밍 확인 및 조정**
  - [ ] 각 데모별 소요시간 측정
  - [ ] 질의응답 시간 고려
  - [ ] 전체 강의 시간 (120분) 내 완료

### 자료 배포 (강의 1일 전)
- [ ] **GitHub repository 업데이트**
  - [ ] 모든 파일 최종 커밋
  - [ ] 메인 README.md 업데이트
  - [ ] 릴리스 브랜치 생성 (선택적)
  
- [ ] **학생 접근 권한 확인**
  - [ ] repository 공개/비공개 설정 확인
  - [ ] 학생 계정 Invitation 전송
  - [ ] 접근 권한 테스트
  
- [ ] **다운로드 링크 테스트**
  - [ ] Master README 링크 작동 확인
  - [ ] 각 Part 문서 접근 확인
  - [ ] 리소스 파일 다운로드 확인
  
- [ ] **인쇄 자료 준비** (필요시)
  - [ ] Part 1-3 핵심 부분 인쇄
  - [ ] 체크리스트 및 참고자료
  - [ ] 데모 치트시트 인쇄

---

## 🔍 최종 점검 (강의 당일 아침)

### 환경 설정 (30분 전)
  - [ ] **노트북 완충**
  - [ ] 배터리 100% 또는 충전기 연결
  - [ ] 비상 배터리 팩 준비 (선택적)
  
- [ ] **인터넷 연결**
  - [ ] Wi-Fi 연결 안정성 확인
  - [ ] 모바일 핫스팟 백업 준비
  - [ ] 데모용 오프라인 버전 준비
  
- [ ] **프로젝터 연결 테스트**
  - [ ] HDMI/VGA 연결 확인
  - [ ] 화면 공유 설정 확인
  - [ ] 해상도 1920x1080 최적화
  
- [ ] **화면 해상도 확인**
  - [ ] 데모 화면 명확성 확인
  - [ ] 텍스트 크기 가독성 확인
  - [ ] 스크린샷 품질 확인
  
- [ ] **알림 끄기**
  - [ ] Do Not Disturb 모드 설정
  - [ ] 모바일 진동/벨 끄기
  - [ ] 이메일/메신저 알림 끄기
  
- [ ] **모든 도구 실행 테스트**
  - [ ] VS Code 실행 및 Copilot 활성화
  - [ ] GitHub 계정 로그인 확인
  - [ ] 데모 파일 접근 확인

### 파일 준비 (10분 전)
- [ ] **모든 데모 파일 탭에 열기**
  - [ ] 데모 폴더별 VS Code에서 열기
  - [ ] 데모 READMEs 브라우저에서 열기
  - [ ] 백업 파일 위치 확인
  
- [ ] **백업 파일 접근 가능**
  - [ ] completed versions 폴더 접근
  - [ ] 스크린샷 백업 접근
  - [ ] 대체 데모 시나리오 준비
  
- [ ] **치트 시트 준비** (demo-cheatsheet.md)
  - [ ] 데모별 핵심 단축키
  - [ ] 문제 해결 빠른 참조
  - [ ] AI 프롬프트 예시 모음
  
- [ ] **타이머 설정**
  - [ ] 전체 강의 120분 타이머
  - [ ] 데모별 5분 타이머
  - [ ] 휴식 시간 고려
  
- [ ] **물 준비**
  - [ ] 물병 및 컵 준비
  - [ ] 목 마를 때를 위한 준비

### 백업 계획 확인
- [ ] **스크린샷 백업 접근 가능**
  - [ ]backup-plan.md 참조
  - [ ] 주요 화면별 스크린샷 준비
  - [ ] 시연용 비디오 준비 (선택적)
  
- [ ] **비디오 백업 준비** (선택적)
  - [ ] 각 데모 30-60초 핵심 장면
  - [ ] 기술 실패 시 즉시 재생
  - [ ] 음성 설명 녹음 (선택적)
  
- [ ] **슬라이드 백업** (기술 실패 시)
  - [ ] 핵심 개념 요약 슬라이드
  - [ ] 도구 설치 가이드 슬라이드
  - [ ] 데모 스크린샷 슬라이드
  
- [ ] **긴급 연락처**
  - [ ] IT 지원실 연락처
  - [ ] 강의실 관리자 연락처
  - [ ] 기술 지원 동료 연락처

---

## 📝 배포 후 작업

### 즉시 (강의 종료 후 1시간)
- [ ] **학생 피드백 수집**
  - [ ] 간단한 설문 작성 요청
  - [ ] 개선사항 메모
  - [ ] 어려웠던 부분 기록
  
- [ ] **발견된 오류 기록**
  - [ ] 데모 실패 사례 기록
  - [ ] 링크 오류 발견시 메모
  - [ ] 내용 수정 필요 부분 체크
  
- [ ] **개선 사항 메모**
  - [ ] 학생 질문 유형 분석
  - [ ] 추가 설명이 필요한 부분
  - [ ] 실습 시간 조정 필요 부분
  
- [ ] **다음 강의 조정 사항 정리**
  - [ ] 시간 배분 조정 필요 부분
  - [ ] 데모 순서 변경 필요 부분
  - [ ] 추가 준비물 필요 부분

### 1주일 내
- [ ] **QA 리포트 업데이트**
  - [ ] v13.0_QA_REPORT.md에 발견사항 추가
  - [ ] 중요도별 이슈 분류
  - [ ] 해결 방안 제안
  
- [ ] **발견된 오류 수정**
  - [ ] 링크 오류 수정
  - [ ] 타이포그래피 수정
  - [ ] 데모 파일 개선
  
- [ ] **학생 질문 FAQ 추가**
  - [ ]resources/09_troubleshooting_guide.md 업데이트
  - [ ]resources/23_part2_troubleshooting.md 업데이트
  - [ ]resources/37_part3_troubleshooting.md 업데이트
  
- [ ] **v13.1 계획 수립** (필요시)
  - [ ] 발견된 Issues 해결 계획
  - [ ] 학생 피드백 반영 계획
  - [ ] 스크린샷 완성 계획

### 1개월 내
- [ ] **도구 업데이트 확인** (2025-12월)
  - [ ] GitHub Copilot 새로운 기능 확인
  - [ ] SpecKit 버전 업데이트 확인
  - [ ] MCP 서버 새로운 기능 확인
  
- [ ] **외부 링크 재검증**
  - [ ] 도구 다운로드 페이지 확인
  - [ ] 문서 링크 유효성 재확인
  - [ ] 변경된 URL 업데이트
  
- [ ] **스크린샷 업데이트** (UI 변경 시)
  - [ ] 도구 UI 변경사항 반영
  - [ ] 새로운 기능 스크린샷 추가
  - [ ] 구식 스크린샷 교체
  
- [ ] **성공 사례 수집**
  - [ ]resources/36_success_stories.md 업데이트
  - [ ] 학생 연구 성과 사례 수집
  - [ ] 워크플로우 개선 사례 공유

---

## ✅ 최종 체크

### 사전 체크리스트 완료
- [ ] **모든 문서 완성도 확인 완료**
- [ ] **모든 품질 기준 준수 확인 완료**
- [ ] **모든 강의 준비 확인 완료**
- [ ] **모든 최종 점검 완료**

### 승인 기준
- [ ] **Important Issues 모두 해결** (QA 리포트 기준)
- [ ] **Critical Issues 없음** 확인
- [ ] **데모 파일 전체 테스트 완료**
- [ ] **백업 계획 준비 완료**

### 릴리스 승인
- [ ] **강의 담당자 최종 승인**
- [ ] **QA 팀 최종 승인**
- [ ] **기술 팀 최종 승인**
- [ ] **학생 테스트 완료** (선택적)

---

## 📞 비상연락망

### 기술 지원
- **GitHub Copilot**: https://support.github.com/contact/copilot
- **VS Code**: https://code.visualstudio.com/docs/support/contact
- **Claude Desktop**: https://help.anthropic.com
- **MCP**: https://modelcontextprotocol.io/

### 강의 진행
- **뒤로가기 방법**: 각 데모 폴더의 README.md 참조
- **빠른 설명**: demo-cheatsheet.md 참조
- **문제 해결**: 관련 troubleshooting guide 참조

### 긴급시
- **슬라이드 모드**: 핵심 내용만 간단히 설명
- **대화형 모드**: 학생들과 함께 실습 진행
- **Q&A 중심**: 이론 설명 후 실습 시간 확대

---

**버전**: v13.0 Release Checklist  
**작성일**: 2025-11-11  
**최종 업데이트**: 2025-11-11  
**다음 검토**: 강의 1주일 전

**관련 문서**:
- v13.0_QA_REPORT.md (품질 보증 리포트)
- Context_and_Planning/demo-files/DEMO-QUICK-START.md (데모 준비)
- .specify/memory/constitution.md (헌장 준수)

---
*v13.0 릴리스 체크리스트 | 생성형 AI 특별강의*
