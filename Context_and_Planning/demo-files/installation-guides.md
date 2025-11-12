# 도구 설치 가이드 (학생 배포용)

이 문서는 강의 후 학생들에게 배포할 도구 설치 가이드입니다.

---

## 🚀 빠른 시작 가이드

### 초보자 추천 경로 (무료)

```markdown
1단계: AI 계정 만들기 (5분)
→ ChatGPT 무료 계정 (https://chat.openai.com)

2단계: Markdown 배우기 (10분)
→ Markdown Guide (https://www.markdownguide.org/basic-syntax/)

3단계: 첫 프롬프트 작성 (15분)
→ 강의 자료의 템플릿 사용

4단계: 실전 적용 (지속적)
→ 자신의 연구 프로젝트에 적용
```

---

## 1️⃣ VS Code 설치

### 다운로드 및 설치

**공식 웹사이트**: https://code.visualstudio.com/

**macOS**:
```bash
# Homebrew 사용 (권장)
brew install --cask visual-studio-code

# 또는 웹사이트에서 .dmg 파일 다운로드
```

**Windows**:
1. 공식 웹사이트에서 Windows 버전 다운로드
2. 설치 파일 실행
3. 기본 설정으로 설치

**Linux**:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install code

# Fedora/RHEL
sudo dnf install code
```

### 필수 확장 프로그램

**Markdown 관련**:
1. **Markdown All in One**
   - 설치: Extensions → "Markdown All in One" 검색 → Install
   - 기능: 자동 완성, 단축키, 미리보기

2. **Markdown Preview Enhanced**
   - 설치: Extensions → "Markdown Preview Enhanced" 검색
   - 기능: 강력한 미리보기, PDF 내보내기

**선택적 확장**:
3. **Korean Language Pack**
   - 한국어 인터페이스 원하는 경우

4. **Prettier**
   - 코드 자동 정리

### 기본 설정

**글씨 크기 조정**:
1. Settings (Cmd/Ctrl + ,)
2. "Font Size" 검색
3. 14-16으로 설정

**자동 저장**:
1. Settings
2. "Auto Save" 검색
3. "afterDelay"로 설정

### 단축키 (필수)

| 기능 | macOS | Windows/Linux |
|------|-------|---------------|
| 명령 팔레트 | Cmd + Shift + P | Ctrl + Shift + P |
| 파일 열기 | Cmd + O | Ctrl + O |
| 저장 | Cmd + S | Ctrl + S |
| Markdown Preview | Cmd + K V | Ctrl + K V |
| 찾기 | Cmd + F | Ctrl + F |

---

## 2️⃣ GitHub Copilot 설치

### 계정 및 구독

**학생 무료 혜택**:
1. GitHub Student Developer Pack 신청
   - URL: https://education.github.com/pack
   - 필요: 학생증 또는 재학증명서
   - 승인: 보통 1-3일
   - 혜택: Copilot 무료 + 기타 개발 도구

**일반 구독** (학생 혜택 없는 경우):
- 가격: $10/월 (약 13,000원)
- 무료 체험: 30일
- URL: https://github.com/features/copilot

### VS Code에 설치

1. **확장 프로그램 설치**:
   - Extensions → "GitHub Copilot" 검색
   - Install 클릭
   - Reload 클릭

2. **로그인**:
   - 우측 하단 Copilot 아이콘 클릭
   - "Sign in to GitHub" 클릭
   - GitHub 계정으로 로그인
   - 권한 승인

3. **활성화 확인**:
   - 새 파일 열기
   - 주석 작성 시작
   - Copilot 제안이 나타나면 성공

### 사용 방법

**기본 사용**:
- 코드/문서 작성 시작
- Copilot이 회색 텍스트로 제안
- Tab: 제안 수락
- Esc: 제안 거부
- Alt + ]: 다음 제안
- Alt + [: 이전 제안

**주석 활용**:
```markdown
<!-- 여기에 원하는 내용 설명 -->
# 제목
```
→ Copilot이 주석을 읽고 적절한 내용 제안

---

## 3️⃣ GitHub Projects 설정

### GitHub 계정

**계정 생성** (없는 경우):
1. https://github.com/signup
2. 이메일, 비밀번호 설정
3. 이메일 인증
4. 무료 플랜 선택

### 저장소 생성

```bash
# 웹 인터페이스에서
1. 우측 상단 "+" → "New repository"
2. 저장소명: my-thesis-project
3. Description: 석사 논문 프로젝트 관리
4. Public 또는 Private 선택
5. "Create repository" 클릭
```

### Projects 설정

**프로젝트 생성**:
1. 저장소 페이지 → "Projects" 탭
2. "New project" 클릭
3. Template 선택:
   - **Board**: Kanban 스타일 (추천)
   - **Table**: 스프레드시트 스타일
   - **Roadmap**: 타임라인 스타일
4. 프로젝트명 입력
5. "Create" 클릭

**Issues 생성**:
1. 저장소 → "Issues" 탭
2. "New issue" 클릭
3. 제목 및 설명 작성
4. Labels, Milestone 설정
5. "Submit new issue" 클릭

**Issues를 Project에 추가**:
1. Issue 페이지에서 우측 "Projects" 클릭
2. 프로젝트 선택
3. 자동으로 보드에 추가됨

### 기본 사용법

**작업 이동**:
- 드래그 앤 드롭으로 컬럼 간 이동
- To Do → In Progress → Done

**진행 상황 추적**:
- 각 Issue의 체크리스트 업데이트
- 코멘트로 진행 내용 기록
- 라벨로 우선순위 표시

---

## 4️⃣ task-master-ai MCP 설치

### 사전 요구사항

- Node.js 18 이상
- Claude Desktop 또는 호환 AI 클라이언트

### Node.js 설치

**macOS**:
```bash
# Homebrew 사용
brew install node

# 버전 확인
node --version  # v18 이상이어야 함
```

**Windows**:
1. https://nodejs.org/ 에서 LTS 버전 다운로드
2. 설치 파일 실행
3. 기본 설정으로 설치
4. 명령 프롬프트에서 `node --version` 확인

### Claude Desktop 설치

**다운로드**:
- macOS: https://claude.ai/download
- Windows: 동일 URL에서 Windows 버전

**설치**:
1. 다운로드한 파일 실행
2. 기본 설정으로 설치
3. Claude 계정으로 로그인

### task-master-ai MCP 설정

**설정 파일 위치**:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**설정 파일 편집**:
```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"]
    }
  }
}
```

**적용**:
1. 설정 파일 저장
2. Claude Desktop 완전 종료
3. Claude Desktop 재시작
4. 새 대화에서 "task-master-ai 사용 가능?" 확인

### 사용 방법

**기본 사용**:
```markdown
새 프로젝트를 시작합니다.

프로젝트명: [프로젝트명]
기간: [기간]

작업을 제안해주세요.
```

**진행 업데이트**:
```markdown
완료한 작업:
- [작업 1]
- [작업 2]

다음 할 일을 알려줘.
```

---

## 🆓 무료 대안 도구

### AI 도구 (무료)

1. **ChatGPT Free**
   - URL: https://chat.openai.com
   - 기능: GPT-3.5 무제한
   - 제한: GPT-4 사용 불가

2. **Claude Free**
   - URL: https://claude.ai
   - 기능: Claude 3 Haiku
   - 제한: 일일 메시지 제한

3. **Google Gemini**
   - URL: https://gemini.google.com
   - 기능: Gemini Pro 무료
   - 장점: Google 서비스 통합

### 프로젝트 관리 (무료)

1. **Notion**
   - URL: https://www.notion.so
   - 기능: 문서 + 데이터베이스 + 프로젝트 관리
   - 학생: 무료 플랜 업그레이드

2. **Trello**
   - URL: https://trello.com
   - 기능: Kanban 보드
   - 무료: 10개 보드

3. **Obsidian**
   - URL: https://obsidian.md
   - 기능: Markdown 노트 + 그래프 뷰
   - 완전 무료 (개인 사용)

---

## 🆘 문제 해결 (Troubleshooting)

### VS Code 관련

**Q: Markdown Preview가 안 보여요**
A:
1. Cmd/Ctrl + K V 단축키 확인
2. 확장 프로그램 설치 확인
3. VS Code 재시작

**Q: 한글이 깨져요**
A:
1. Settings → "Encoding" 검색
2. "UTF-8"로 설정

### Copilot 관련

**Q: Copilot 제안이 안 나와요**
A:
1. 우측 하단 Copilot 아이콘 확인 (활성화 상태?)
2. GitHub 로그인 확인
3. 구독 상태 확인
4. VS Code 재시작

**Q: 제안이 엉뚱해요**
A:
1. 주석으로 더 명확한 컨텍스트 제공
2. 여러 제안 중 선택 (Alt + ])
3. 마음에 안 들면 무시하고 직접 작성

### GitHub Projects 관련

**Q: Projects 탭이 안 보여요**
A:
1. 저장소 Settings → Features → Projects 활성화
2. 페이지 새로고침

**Q: Issue를 Project에 추가할 수 없어요**
A:
1. Issue 우측 "Projects" 섹션 확인
2. 프로젝트 선택
3. 권한 확인 (본인 저장소인가?)

### task-master-ai MCP 관련

**Q: MCP를 찾을 수 없다고 나와요**
A:
1. Node.js 버전 확인 (v18 이상)
2. 설정 파일 경로 확인
3. JSON 문법 오류 확인
4. Claude Desktop 완전 재시작

**Q: 설정 파일을 찾을 수 없어요**
A:
- macOS: Finder → Cmd + Shift + G → 경로 입력
- Windows: 파일 탐색기 주소창에 경로 입력
- 폴더가 없으면 생성

---

## 📚 추가 학습 리소스

### 공식 문서

1. **VS Code**
   - 공식 문서: https://code.visualstudio.com/docs
   - Markdown 가이드: https://code.visualstudio.com/docs/languages/markdown

2. **GitHub Copilot**
   - 공식 문서: https://docs.github.com/en/copilot
   - 시작 가이드: https://docs.github.com/en/copilot/getting-started-with-github-copilot

3. **GitHub Projects**
   - 공식 문서: https://docs.github.com/en/issues/planning-and-tracking-with-projects

4. **MCP**
   - 공식 문서: https://github.com/modelcontextprotocol

### 튜토리얼 영상

1. **VS Code 기초** (YouTube)
   - "VS Code 완벽 가이드" (한글)
   - 길이: 30분

2. **GitHub Copilot 활용** (YouTube)
   - "GitHub Copilot으로 생산성 2배" (한글)
   - 길이: 20분

3. **GitHub Projects** (YouTube)
   - "GitHub Projects로 프로젝트 관리" (한글)
   - 길이: 15분

---

## 💰 비용 정보

### 무료로 시작 가능

| 도구 | 무료 버전 | 유료 버전 | 학생 혜택 |
|------|----------|----------|----------|
| VS Code | ✅ 완전 무료 | - | - |
| ChatGPT | ✅ GPT-3.5 | $20/월 (GPT-4) | ❌ |
| Claude | ✅ 제한적 | $20/월 | ❌ |
| Gemini | ✅ 무료 | - | - |
| Copilot | ❌ | $10/월 | ✅ 무료 |
| GitHub | ✅ 무료 | $4/월 (Pro) | ✅ Pro 무료 |
| Notion | ✅ 개인 무료 | $8/월 | ✅ Plus 무료 |

### 추천 조합

**완전 무료 조합**:
- VS Code (무료)
- ChatGPT Free (무료)
- GitHub (무료)
- Notion (무료)

**학생 최적 조합**:
- VS Code (무료)
- GitHub Copilot (학생 무료)
- GitHub Projects (학생 무료)
- Claude (무료 또는 $20/월)

**프리미엄 조합** (월 $30):
- VS Code (무료)
- ChatGPT Plus ($20/월)
- GitHub Copilot ($10/월)
- Notion Plus (학생 무료)

---

## 🎓 학습 경로

### Week 1: 기초 다지기

```markdown
Day 1-2: 환경 설정
- [ ] VS Code 설치
- [ ] AI 계정 생성
- [ ] Markdown 기본 문법 학습

Day 3-4: 첫 프롬프트
- [ ] 강의 템플릿 사용
- [ ] 자신의 연구 주제로 프롬프트 작성
- [ ] AI 응답 받아보기

Day 5-7: 실전 적용
- [ ] 실제 연구 작업에 적용
- [ ] 결과 기록
- [ ] 개선점 파악
```

### Week 2-4: 심화 학습

```markdown
Week 2: Spec 문서 작성
- [ ] 프로젝트 Spec 작성
- [ ] AI와 대화하며 정교화
- [ ] 작업 분해 연습

Week 3: 도구 활용
- [ ] GitHub Projects 설정 (또는 대안)
- [ ] 작업 추적 시작
- [ ] 주간 루틴 확립

Week 4: 통합 워크플로우
- [ ] 전체 워크플로우 적용
- [ ] 자신만의 템플릿 개발
- [ ] 동료와 공유
```

---

## 📞 도움 받기

### 공식 지원

1. **VS Code**
   - 커뮤니티: https://github.com/microsoft/vscode/discussions
   - Stack Overflow: [vscode] 태그

2. **GitHub Copilot**
   - 지원: https://support.github.com/
   - 커뮤니티: GitHub Community Forum

3. **GitHub**
   - 문서: https://docs.github.com
   - 지원: https://support.github.com

### 커뮤니티

1. **한국 커뮤니티**
   - 네이버 카페: "AI 활용 연구자 모임"
   - 카카오톡: "대학원생 AI 스터디"
   - 디스코드: "한국 AI 연구자"

2. **부산 지역**
   - 카카오톡: "부산 AI 연구자"
   - 오프라인 모임: 월 1회

3. **국제 커뮤니티**
   - Reddit: r/ChatGPT, r/ClaudeAI
   - Discord: OpenAI Community

### 강사 연락처

- 이메일: [이메일]
- GitHub: [저장소 URL]
- 오픈 채팅: [링크]

**질문 환영**:
- 설치 관련 질문
- 사용 중 어려움
- 추가 예제 요청

---

## ✅ 설치 완료 체크리스트

```markdown
# 설치 완료 확인

## 필수 도구
- [ ] VS Code 설치 및 실행 확인
- [ ] Markdown 파일 작성 및 Preview 확인
- [ ] AI 계정 (ChatGPT 또는 Claude) 생성
- [ ] 첫 프롬프트 작성 및 응답 받기

## 선택적 도구
- [ ] GitHub Copilot 설치 (학생 무료 또는 유료)
- [ ] GitHub 계정 및 저장소 생성
- [ ] GitHub Projects 설정
- [ ] task-master-ai MCP 설정 (고급)

## 학습 자료
- [ ] 강의 자료 다운로드 (GitHub)
- [ ] 예제 및 템플릿 확인
- [ ] 추가 학습 리소스 북마크

## 실전 적용
- [ ] 자신의 연구 프로젝트 정의
- [ ] 첫 Spec 문서 작성
- [ ] 1주일 챌린지 시작
```

---

## 🎯 다음 단계

설치가 완료되었다면:

1. **강의 자료 복습**
   - GitHub 저장소의 예제 확인
   - 템플릿 다운로드

2. **첫 프로젝트 시작**
   - 현재 연구를 Markdown으로 정리
   - AI에게 검토 요청

3. **커뮤니티 참여**
   - 부산 AI 연구자 모임 가입
   - 경험 공유

4. **지속적 학습**
   - 매일 AI와 대화
   - 새로운 기법 시도
   - 자신만의 워크플로우 개발

**화이팅! 🚀**