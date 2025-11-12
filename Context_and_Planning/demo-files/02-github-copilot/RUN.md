# 데이터 분석 실행 가이드

이 문서는 `data-analysis.py` 스크립트를 실행하기 위한 단계별 가이드를 제공합니다.

## 1. 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate
```

## 2. 의존성 설치

```bash
# requirements.txt에서 패키지 설치
pip install -r requirements.txt
```

## 3. 스크립트 실행

```bash
# 데이터 분석 실행
python data-analysis.py
```

## 실행 결과

스크립트 실행 시 다음 작업이 수행됩니다:

1. **데이터 로드 또는 생성**: `survey_data.csv` 파일이 있으면 로드하고, 없으면 샘플 데이터를 생성합니다.
2. **기초 통계 분석**: 데이터의 기술 통계를 출력합니다.
3. **상관관계 분석**: 자기조절학습 전략과 참여도 간의 상관관계를 분석하고 히트맵을 생성합니다.
4. **회귀분석**: 다중 회귀분석을 수행하여 각 전략이 참여도에 미치는 영향을 분석합니다.

## 출력 파일

- `survey_data.csv`: 생성된 샘플 데이터 파일
- `correlation_heatmap.png`: 상관관계 히트맵 이미지

## 주의사항

- 스크립트는 헤드리스 환경에서도 실행되도록 설계되어 있습니다.
- 그래프는 `correlation_heatmap.png` 파일로 저장됩니다.
- 가상환경을 활성화한 상태에서 실행하세요.