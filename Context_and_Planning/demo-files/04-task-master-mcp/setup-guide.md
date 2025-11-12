# task-master-ai MCP 설정 가이드

이 문서는 task-master-ai MCP 시연을 위한 설정 가이드입니다.

## 사전 준비 (강의 2주일 전)

### 1. Claude Desktop 설치

#### macOS (권장 방법):

**방법 1: Homebrew (추천)**
```bash
# Homebrew 설치 확인 및 업데이트
brew --version
brew update

# Claude 설치
brew install --cask claude

# 설치 확인
ls -la /Applications/ | grep Claude
```

**방법 2: 공식 다운로드 (Homebrew 실패 시)**
```bash
# 공식 사이트에서 다운로드
open https://claude.ai/download

# 또는 curl로 직접 다운로드 (Intel Mac)
curl -L -o Claude.dmg "https://claude.ai/download/mac"

# 또는 Apple Silicon Mac
curl -L -o Claude.dmg "https://claude.ai/download/mac-arm64"
```

#### Windows:
- Claude 공식 웹사이트에서 Windows 버전 다운로드
- 설치 파일 실행
- 설치 완료 후 시작 메뉴에서 "Claude" 검색하여 실행 확인

#### 설치 확인 체크리스트:
- [ ] 응용 프로그램/시작 메뉴에 Claude 아이콘 표시
- [ ] 앱 실행 시 로그인 화면 나타남
- [ ] 버전 정보 확인 (Help → About에서 버전 확인 가능)
- [ ] 인터넷 연결 시 정상 작동

#### 설치 실패 시 해결 방법:
1. **Homebrew 관련 오류**:
   ```bash
   # Homebrew 업데이트 후 재시도
   brew update && brew upgrade
   brew doctor  # 문제 진단
   brew install --cask claude
   ```

2. **아키텍처 확인**:
   ```bash
   uname -m  # Intel: x86_64, Apple Silicon: arm64
   ```

3. **공식 다운로드 사용**:
   - Homebrew 실패 시 반드시 공식 사이트 다운로드 사용
   - 다운로드한 파일의 체크섬 확인 권장

4. **권한 문제**:
   ```bash
   # 권한 오류 시
   sudo spctl --master-disable  # Gatekeeper 비활성화 (임시)
   # 설치 완료 후 다시 활성화: sudo spctl --master-enable
   ```

### 2. task-master-ai MCP 설치

**설치 방법** (MCP 서버 설정):

1. Claude Desktop 설정 파일 열기:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. 설정 파일에 task-master-ai 추가:
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

3. Claude Desktop 재시작

4. 확인:
   - Claude Desktop 실행
   - 새 대화 시작
   - "task-master-ai를 사용할 수 있나요?" 질문
   - AI가 MCP 도구를 인식하면 성공

### 3. 테스트 프로젝트 준비

**테스트 프롬프트**:
```markdown
새 프로젝트를 시작합니다.

프로젝트명: 테스트 프로젝트
기간: 1주일

간단한 작업 3개를 제안해줘.
```

**예상 응답**:
- AI가 task-master-ai MCP를 사용하여 작업 제안
- 작업 목록, 우선순위, 예상 시간 제시

## 🎬 시연 시나리오 (5분)

### 준비 상태 확인 (시연 10분 전)

```markdown
# 체크리스트
- [ ] Claude Desktop 실행됨
- [ ] task-master-ai MCP 활성화 확인
- [ ] 새 대화 창 준비 (깨끗한 상태)
- [ ] 프롬프트 파일 열어둠 (복사 준비)
- [ ] 화면 공유 설정
- [ ] 글씨 크기 확대 (18pt 이상)
- [ ] 알림 끄기
- [ ] 백업 자료 준비 (클릭 한 번에 열림)
```

### 시연 진행 (5분)

**1단계: 프로젝트 초기화 (1분)**

1. Claude Desktop 화면 공유
2. 프롬프트 1 복사 & 붙여넣기
3. AI 응답 대기 (10-20초)
4. 응답 확인 및 설명

**강사 멘트**:
"AI에게 프로젝트 정보를 제공했습니다.
보시다시피 AI가 현재 상황을 분석하고,
다음 우선순위 작업 3개를 제안했습니다.
각 작업의 예상 소요 시간과 마감일까지 제시합니다."

**2단계: 작업 세부 분해 (2분)**

1. 프롬프트 2 입력
2. AI 응답 확인
3. 주간 단위 작업 계획 설명

**강사 멘트**:
"이제 '문헌 고찰 완료'라는 큰 작업을 세부 작업으로 분해해달라고 요청했습니다.
AI가 주간 단위로 작업을 나누고, 각 작업마다 체크리스트를 만들었습니다.
이것이 Part 2에서 배운 작업 분해의 실제 적용입니다."

**3단계: 진행 상황 업데이트 (1.5분)**

1. 프롬프트 3 입력
2. AI 응답 확인
3. 일정 분석 및 해결 방안 설명

**강사 멘트**:
"진행 상황을 솔직히 보고했습니다. 예상보다 느리다고요.
AI가 일정 지연 위험을 분석하고, 만회 방안을 제시합니다.
또한 어려운 논문을 이해하는 구체적인 방법까지 제안합니다.
이것이 AI를 프로젝트 매니저로 활용하는 방법입니다."

**4단계: 통합 워크플로우 (0.5분)**

1. 프롬프트 4 입력
2. AI가 Context Engineering 기법을 적용한 프롬프트 생성
3. 통합 설명

**강사 멘트**:
"마지막으로 AI에게 '논문 요약 프롬프트를 만들어달라'고 했더니,
Part 1에서 배운 Markdown 구조화, 명확한 요청 등을 적용하여
프롬프트를 만들어줍니다.
이렇게 Context Engineering + Planning + 지속적 대화가
하나의 워크플로우로 통합됩니다."

## 🔄 백업 계획

### 시나리오 1: MCP 연결 실패

**증상**: AI가 "task-master-ai를 찾을 수 없습니다" 응답

**대응**:
1. 침착하게 Claude Desktop 재시작 (1회)
2. 여전히 실패 시:
   - "기술적 문제가 발생했네요. 미리 준비한 응답으로 보여드리겠습니다"
   - `demo-files/04-task-master-mcp/responses.md` 파일의 백업 응답 사용
   - 또는 스크린샷으로 설명

### 시나리오 2: AI 응답 지연

**증상**: 30초 이상 응답 없음

**대응**:
1. "AI가 생각하는 동안 질문 받겠습니다" (청중 참여)
2. 1분 이상 지연 시:
   - "네트워크가 느린 것 같네요"
   - 백업 응답 사용

### 시나리오 3: 예상과 다른 응답

**증상**: AI가 엉뚱한 답변

**대응**:
1. "흥미로운 응답이네요. 다시 명확히 요청해보겠습니다"
2. 프롬프트 재작성하여 재시도
3. 여전히 실패 시 백업 응답 사용

### 시나리오 4: 시간 부족

**대응**:
- 프롬프트 1, 3만 시연 (핵심만)
- 프롬프트 2, 4는 "이런 것도 가능합니다"로 간단히 언급
- 백업 자료로 보완 설명

## 📸 백업 자료 준비

### 스크린샷 목록

1. `01-project-init-prompt.png`: 프롬프트 1 입력 화면
2. `02-project-init-response.png`: AI 응답 화면
3. `03-task-breakdown-prompt.png`: 프롬프트 2 입력
4. `04-task-breakdown-response.png`: 세부 작업 응답
5. `05-progress-update-prompt.png`: 프롬프트 3 입력
6. `06-progress-update-response.png`: 진행 분석 응답
7. `07-integration-prompt.png`: 프롬프트 4 입력
8. `08-integration-response.png`: 통합 프롬프트 생성

### 녹화 영상

**파일명**: `demo4-taskmaster-mcp.mp4`
**길이**: 4분
**내용**:
- 프롬프트 1-4 순차 시연
- 각 응답 설명
- 핵심 포인트 강조

**나레이션 스크립트**:
```
[0:00-0:15] "task-master-ai MCP는 AI를 프로젝트 매니저로 활용하는 도구입니다."
[0:15-1:00] "프로젝트 정보를 제공하면 AI가 다음 작업을 제안합니다."
[1:00-2:00] "큰 작업을 관리 가능한 단위로 자동 분해합니다."
[2:00-3:00] "진행 상황을 보고하면 일정을 분석하고 조언합니다."
[3:00-4:00] "이렇게 Context Engineering과 Planning이 통합됩니다."
```

## 🎯 시연 성공 체크리스트

### 시연 직전 (5분 전)
- [ ] Claude Desktop 실행 및 MCP 확인
- [ ] 새 대화 창 준비
- [ ] 프롬프트 파일 열기
- [ ] 백업 자료 준비 (한 번에 열림)
- [ ] 타이머 설정 (5분)
- [ ] 화면 공유 시작
- [ ] 글씨 크기 확인

### 시연 중
- [ ] 천천히, 명확하게 설명
- [ ] 각 응답의 핵심 포인트 강조
- [ ] Part 1, 2와의 연결 언급
- [ ] 도구 중립성 강조

### 시연 후
- [ ] "이 도구가 유일한 선택은 아닙니다" 언급
- [ ] 대안 도구 소개 (ChatGPT Custom GPTs, Claude Projects)
- [ ] 질문 받기
- [ ] 설치 가이드 공유 안내

## 💡 대안 도구 언급

**시연 후 반드시 언급**:

"task-master-ai MCP는 하나의 예시입니다.
비슷한 기능을 하는 다른 도구들도 있습니다:

- **ChatGPT Custom GPTs**: 프로젝트 관리 GPT 만들기
- **Claude Projects**: Claude의 프로젝트 기능 활용
- **Notion AI**: Notion에서 AI 작업 관리
- **다른 MCP 도구 조합**: 여러 MCP를 조합하여 자신만의 워크플로우

중요한 것은 도구가 아니라 체계적인 접근 방식입니다.
Context Engineering + Planning + 지속적 대화,
이 원칙만 지키면 어떤 도구로도 가능합니다."