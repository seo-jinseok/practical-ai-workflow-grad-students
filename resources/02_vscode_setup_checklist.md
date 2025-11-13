# VS Code 설치 및 설정 체크리스트

**목적**: Visual Studio Code 설치와 GitHub Copilot 설정을 위한 단계별 가이드  
**소요 시간**: 약 15-20분  
**대상**: 모든 OS (Windows, macOS, Linux) 사용자  

---

## 📋 사전 준비사항 체크

### 시스템 요구사항
- [ ] **운영체제 확인**
  - [ ] Windows 10/11 (64-bit) 또는 macOS 10.15+ 또는 Linux
  - [ ] 최소 1GB 사용 가능한 디스크 공간
  - [ ] 인터넷 연결 상태 확인

### 계정 준비
- [ ] **GitHub 계정**
  - [ ] 기존 계정 보유 확인
  - [ ] 없다면 https://github.com 에서 회원가입
- [ ] **학교 이메일** (학생 혜택 신청용)
  - [ ] .ac.kr, .edu 등 교육용 이메일 확인
  - [ ] 학생증 또는 재학증명서 준비 (학교 이메일 없을 경우)

---

## 🛠️ VS Code 설치 (5분)

### Windows 사용자
![VS Code 다운로드 페이지 - Windows용 설치 파일](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

1. **다운로드**
   - [ ] https://code.visualstudio.com/ 방문
   - [ ] "Download for Windows" 클릭
   - [ ] 설치 파일 저장 (예: `VSCodeUserSetup-x64-1.95.0.exe`)

2. **설치 진행**
   - [ ] 설치 파일 실행 (관리자 권한 필요)
   - [ ] **권장 옵션 선택**:
     - [ ] ✅ "Add to PATH" (환경 변수 추가)
     - [ ] ✅ "Create a desktop icon" (바탕화면 바로가기)
     - [ ] ✅ "Register Code as an editor" (기본 에디터로 등록)
     - [ ] ✅ "Add 'Open with Code' action" (우클릭 메뉴)
   - [ ] "Next" → "Install" 클릭
   - [ ] 설치 완료까지 대기

### macOS 사용자
![VS Code 다운로드 페이지 - macOS용](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

1. **다운로드**
   - [ ] https://code.visualstudio.com/ 방문
   - [ ] "Download for macOS" 클릭
   - [ ] `.zip` 파일이 Downloads 폴더에 저장됨

2. **설치 진행**
   - [ ] 다운로드된 `.zip` 파일 더블클릭하여 압축 해제
   - [ ] `Visual Studio Code` 앱을 Applications 폴더로 드래그
   - [ ] Finder → Applications → VS Code 더블클릭하여 실행
   - [ ] 첫 실행 시 "확인 없이 열기" 클릭 (Gatekeeper 우회)

### Linux 사용자
![VS Code 설치 방법 안내](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

**Ubuntu/Debian:**
```bash
# 방법 1: Snap으로 설치 (추천)
sudo snap install --classic code

# 방법 2: Repository 추가 후 설치
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update && sudo apt install code
```

---

## 🔌 GitHub Copilot 설치 (5분)

### Copilot 확장 설치
![VS Code Extensions Marketplace - GitHub Copilot 검색](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

1. **VS Code 실행**
   - [ ] VS Code 아이콘 더블클릭하여 프로그램 시작
   - [ ]elcome 화면 또는 빈 에디터가 보이면 정상 실행

2. **Extensions 탭 열기**
   - [ ] 왼쪽 사이드바의 4개 사각형 아이콘 클릭
   - [ ] 또는 `Ctrl+Shift+X` (Windows/Linux) / `Cmd+Shift+X` (macOS) 단축키

3. **GitHub Copilot 검색 및 설치**
   - [ ] 검색창에 "GitHub Copilot" 입력
   - [ ] "GitHub Copilot" (Microsoft, GitHub 제공) 선택
   - [ ] "Install" 버튼 클릭
   - [ ] 설치 완료 후 "Reload Required" 메시지 확인
   - [ ] "Reload" 클릭하여 VS Code 재시작

### GitHub 계정 연결
![Copilot 로그인 프롬프트 - 상태바](../images/part1/vscode-setup/copilot-login-prompt.png)

1. **로그인 시작**
   - [ ] VS Code 하단 상태바의 GitHub Copilot 아이콘 확인
   - [ ] 아이콘 클릭 (또는 `Ctrl+Shift+P` → "GitHub Copilot: Sign in")
   - [ ] "Sign in to GitHub" 선택

2. **브라우저 인증**
   - [ ] 기본 브라우저가 자동 열림
   - [ ] GitHub 계정으로 로그인 (없다면 먼저 가입)
   - [ ] "Authorize GitHub Copilot for VS Code" 페이지 확인
   - [ ] "Authorize github-copilot" 버튼 클릭
   - [ ] 브라우저에서 "You can close this tab and return to VS Code" 메시지 확인

3. **VS Code로 돌아가기**
   - [ ] VS Code 창으로 포커스 이동
   - [ ] 하단 상태바에 "GitHub Copilot is active" 또는 "GitHub Copilot" 아이콘 표시 확인
   - [ ] 마우스 오버 시 "GitHub Copilot is active" 툴팁 확인

---

## 🎓 학생 혜택 신청 (10분, 선택사항)

### Student Developer Pack 신청
![GitHub Education Pack 신청 페이지](../images/part1/github-education/github-education-pack-main.png)

1. **GitHub Education 페이지 접속**
   - [ ] https://education.github.com/pack 방문
   - [ ] "Get your pack for free" 버튼 클릭

2. **계정 정보 입력**
   - [ ] **학교 이메일 주소** 입력
     - 예: student@university.ac.kr
     - 学校 이메일 없다면: "Don't have a school email?" 클릭
   - [ ] **학교 이름** (영문) 입력
     - 예: "Seoul National University"
   - [ ] **졸업 예정일** 선택
   - [ ] **사용 목적** 영어로 간단히 작성
     ```
     I will use GitHub Copilot for my graduate research in [your field] to improve research productivity and data analysis efficiency.
     ```

3. **인증 방법 선택**
   - [ ] **학교 이메일 있는 경우**: 이메일 인증
   - [ ] **학교 이메일 없는 경우**: 학생증/재학증명서 업로드
     - [ ] 최근 3개월 이내 발급된 재학증명서 또는 학생증 사진
     - [ ] JPG, PNG, PDF 형식 지원

4. **승인 대기**
   - [ ] "Submit" 버튼 클릭
   - [ ] 승인 메일 대기 (보통 1-3일, 빠르면 몇 시간)
   - [ ] 승인 완료 시 GitHub 계정에 자동 반영

---

## ⚙️ 기본 설정 (5분, 선택사항)

### 테마 및 외관 설정
![VS Code Settings - 테마 및 폰트 설정](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

1. **테마 변경**
   - [ ] `Ctrl+K` (Windows/Linux) / `Cmd+K` (macOS) → `Ctrl+T` (Windows/Linux) / `Cmd+T` (macOS)
   - [ ] 또는 File → Preferences → Theme → Color Theme
   - [ ] "Dark+" 또는 "Light+" 선택
   - [ ] 선택 즉시 적용 확인

2. **폰트 크기 조정**
   - [ ] `Ctrl+,` (Windows/Linux) / `Cmd+,` (macOS) 설정 열기
   - [ ] "Font Size" 검색
   - [ ] 기본값 14에서 16-18로 증가 (시력에 따라 조정)

3. **한글 폰트 개선** (선택사항)
   - [ ] Settings에서 "Font Family" 검색
   - [ ] 기존 값 앞에 `'Malgun Gothic', 'Noto Sans KR',` 추가
   - [ ] 예: `'Malgun Gothic', 'Noto Sans KR', Consolas, 'Courier New', monospace`

### 유용한 확장 프로그램 추가
![VS Code Extensions - 권장 확장](../images/part1/vscode-setup/extensions-marketplace-copilot.png)

- [ ] **Korean Language Pack**: 한국어 번역 지원
- [ ] **Markdown All in One**: Markdown 작성 도구
- [ ] **GitLens**: Git 정보 시각화
- [ ] **Prettier**: 코드 포맷터

---

## ✅ 설정 완료 확인

### Copilot 활성화 확인
![Copilot Pro 활성화 확인](../images/part1/vscode-setup/copilot-pro-status-active.png)

- [ ] **하단 상태바 아이콘**
  - [ ] "✓" 마크가 있는 Copilot 아이콘 확인
  - [ ] 마우스 오버 시 "GitHub Copilot is active" 표시
  - [ ] Pro 버전: "GitHub Copilot Pro" 표시

- [ ] **기능 테스트**
  - [ ] 새 파일 생성 (`Ctrl+N`)
  - [ ] 파일에 "console.log("Hello"); " 입력
  - [ ] Copilot이 자동완성 제안 표시 확인

### Copilot Student Pro 확인
![GitHub Copilot 설정 페이지](../images/part1/vscode-setup/copilot-pro-status-active.png)

1. **웹에서 확인**
   - [ ] https://github.com/settings/copilot 방문
   - [ ] "Copilot Pro" 플랜 표시 확인
   - [ ] "You've activated Copilot Pro" 메시지 확인

2. **VS Code에서 확인**
   - [ ] Copilot 아이콘 마우스 오버
   - [ ] "GitHub Copilot Pro" 툴팁 확인
   - [ ] Chat 기능 (새로운 Ctrl+I)에서 Pro 전용 모델 선택 가능 확인

---

## 🚨 문제 해결

### VS Code 실행 문제
- **문제**: VS Code가 실행되지 않음
- **해결**: 
  - [ ] 컴퓨터 재시작
  - [ ] Windows: 설치 파일 다시 실행 → "Repair" 선택
  - [ ] macOS: Applications 폴더에서 삭제 후 재설치
  - [ ] Linux: `sudo snap refresh code` 또는 재설치

### Copilot 연결 문제
- **문제**: Copilot 아이콘이 나타나지 않음
- **해결**:
  - [ ] VS Code 재시작 (`Ctrl+Q` → 재실행)
  - [ ] Extensions 탭에서 GitHub Copilot 확인 → "Disable" → "Enable" 다시 설정
  - [ ] VS Code 완전 종료 후 재실행

### 로그인 문제
- **문제**: "Sign in failed" 오류
- **해결**:
  - [ ] 브라우저에서 GitHub 로그아웃 → 다시 로그인
  - [ ] VS Code에서 "File → Preferences → Settings" → "Extensions → GitHub Copilot" → "Reset auth" 클릭
  - [ ] 30분 후 다시 시도 (API 제한)

### 학생 혜택 미적용
- **문제**: Pro 버전으로 업그레이드 안됨
- **해결**:
  - [ ] Education Pack 신청 상태 확인 (이메일 확인)
  - [ ] 3일 후에도 미승인: 학생증/재학증명서 재업로드
  - [ ] GitHub Support contato (https://github.com/contact)

---

## 📚 다음 단계

설치와 기본 설정이 완료되면:

1. **Part 1 메인 문서로 이동**: `../Practical_AI_Workflow_for_Grad_Students_Part1.md`
2. **연구 폴더 구조 생성**: `03_folder_structure_templates.md` 참고
3. **연구 컨텍스트 작성**: `04_context_template_2025.md` 템플릿 사용
4. **Markdown 실습**: `05_markdown_quick_reference.md` 참조

---

**📞 지원 및 피드백**
- VS Code 공식 문서: https://code.visualstudio.com/docs
- GitHub Copilot 도움말: https://docs.github.com/copilot
- 문제 해결: `09_troubleshooting_guide.md` 참조

---

*마지막 업데이트: 2025-11-10*  
*버전: v13.0 Part 1*
