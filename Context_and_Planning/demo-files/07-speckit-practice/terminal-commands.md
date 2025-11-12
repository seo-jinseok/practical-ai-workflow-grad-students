# SpecKit 시연용 터미널 명령어

**목적**: 시연 중 복사-붙여넣기할 명령어 모음  
**대상**: 터미널 사용 경험이 제한적인 강사/학생  
**사용법**: 각 명령어를 순서대로 복사하여 터미널에 붙여넣기  

## 사전 확인 명령어

### Python 버전 확인
```bash
python3 --version
```
**예상 결과**: `Python 3.11.x` 이상  
**실패 시**: Python 업그레이드 필요 (자료 참고)

### Git 확인
```bash
git --version
```
**예상 결과**: `git version 2.x.x`  
**실패 시**: Git 설치 필요

### uv 확인
```bash
uv --version
```
**예상 결과**: `uv x.x.x`  
**실패 시**: uv 설치 필요 (다음 섹션)

## uv 설치 (필요시)

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
**설명**: uv 패키지 매니저 설치  
**소요 시간**: 1-2분  
**설치 후**: 터미널 재시작 필요

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**설명**: Windows용 uv 설치  
**권한**: 관리자 권한 필요할 수 있음

## SpecKit 설치

### specify CLI 설치
```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```
**설명**: GitHub에서 SpecKit 다운로드 및 설치  
**소요 시간**: 1-2분  
**진행 표시**: 다운로드 및 설치 진행 상황 표시됨

### 설치 확인
```bash
specify --version
```
**예상 결과**: `Specify CLI version x.x.x`  
**실패 시**: PATH 설정 확인 필요

## 시연용 프로젝트 생성 (Step 1)

### 프로젝트 폴더 생성 및 이동
```bash
mkdir online-learning-survey
cd online-learning-survey
```
**설명**: 새 폴더 생성 후 이동

### SpecKit 프로젝트 초기화
```bash
specify init online-learning-survey --ai copilot
```
**설명**: SpecKit 프로젝트 초기화, AI는 GitHub Copilot 사용  
**예상 결과**: `.specify/` 폴더 및 템플릿 파일 생성  
**소요 시간**: 5-10초

### 생성된 파일 확인
```bash
ls -la .specify/
```
**예상 결과**:
```
.specify/
├── memory/
│   └── constitution.md
└── templates/
    ├── spec-template.md
    ├── plan-template.md
    └── tasks-template.md
```

## SpecKit 명령어 (시연 중)

### 프로젝트 상태 확인
```bash
specify check
```
**설명**: 현재 프로젝트 상태 확인  
**용도**: 각 단계 완료 후 확인

### Constitution 작성 후 검증
```bash
specify check constitution
```
**설명**: Constitution 파일 검증

### Spec 작성 후 검증
```bash
specify check spec
```
**설명**: Spec 문서 완성도 확인

### 전체 워크플로우 상태
```bash
specify status
```
**설명**: 7단계 중 현재 위치 확인

## 트러블슈팅 명령어

### PATH 문제 해결 (macOS/Linux)
```bash
export PATH="$HOME/.local/bin:$PATH"
```
**설명**: specify 명령어를 찾을 수 없을 때

### PATH 문제 해결 (Windows PowerShell)
```powershell
$env:PATH += ";$HOME\.local\bin"
```

### 설치 재시도
```bash
uv tool uninstall specify-cli
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```
**설명**: 설치 문제 발생 시 재설치

## 시연 후 정리 (선택적)

### 테스트 프로젝트 삭제
```bash
cd ..
rm -rf online-learning-survey
```
**주의**: 실제 프로젝트는 삭제하지 말 것

### 또는 보관
```bash
mv online-learning-survey demo-speckit-example
```
**설명**: 학생들이 참고할 수 있도록 보관

## 🎯 빠른 참조 카드 (시연 중)

| 단계 | 명령어 | 설명 |
|------|--------|------|
| 초기화 | `specify init [name] --ai copilot` | 프로젝트 시작 |
| 확인 | `specify check` | 상태 확인 |
| 상태 | `specify status` | 진행 단계 확인 |
| 도움말 | `specify --help` | 명령어 도움말 |

## 시연용 명령어 시퀀스 (5분)

```bash
# 1. 프로젝트 생성
mkdir online-learning-survey && cd online-learning-survey

# 2. SpecKit 초기화
specify init online-learning-survey --ai copilot

# 3. 파일 구조 확인
ls -la .specify/

# 4. 상태 확인
specify check

# 5. 워크플로우 상태
specify status
```

**설명**: 위 5개 명령어로 SpecKit의 기본 사용법을 시연할 수 있습니다.

## ⚠️ 주의사항

### 시연 중 주의사항
- **복사-붙여넣기**: 모든 명령어를 직접 타이핑하지 마세요
- **시간 관리**: 각 명령어마다 10-15초 대기
- **오류 발생**: 즉시 백업 방법 전환
- **터미널 친숙화**: "초보자도 따라할 수 있습니다" 강조

### 대안 시나리오
**SpecKit 미설치 시**:
1. 위 명령어들을 스크린샷으로 준비
2. "정상적으로 설치되면 이런 결과가 나옵니다" 설명
3. 완성된 파일들을 보여주기

**명령어 실행 실패 시**:
1. "기술적 문제입니다" 자연스럽게 전환
2. 완성된 폴더 구조 스크린샷 보여주기
3. "이 개념만 이해해도 충분합니다" 강조

## 📋 강사용 체크리스트

### 시연 전 확인
- [ ] Python 3.11+ 설치 확인
- [ ] SpecKit 설치 완료 (`specify --version` 테스트)
- [ ] 터미널에서 복사-붙여넣기 테스트
- [ ] 백업 스크린샷 준비

### 시연 중 체크
- [ ] 각 명령어 전 복사 확인
- [ ] 결과 출력 대기 (10-15초)
- [ ] 오류 발생 시 대안으로 전환
- [ ] "선택적 도구" 강조

### 시연 후
- [ ] 테스트 프로젝트 정리
- [ ] 대안 도구 언급 (Markdown + AI)
- [ ] "도구가 아닌 원칙이 중요" 강조
