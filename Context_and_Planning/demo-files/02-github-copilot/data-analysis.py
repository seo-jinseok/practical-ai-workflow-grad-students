# 설문 데이터 분석: 학습자 참여도와 자기조절학습 전략의 관계
# 이 파일은 GitHub Copilot 시연 중 선택적으로 사용 (이공계 학생 대상)

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 헤드리스 환경을 위한 백엔드 설정
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 데이터 로드
# Copilot이 여기서부터 제안을 시작합니다

# 시연 시나리오:
# 1. 위 주석까지 작성
# 2. Copilot이 아래 코드를 제안
# 3. Tab으로 수락하며 빠르게 완성

# === 아래는 Copilot이 제안할 내용 (백업용) ===

def generate_sample_data(filepath):
    """
    샘플 설문 데이터를 생성합니다.

    Parameters:
    -----------
    filepath : str
        저장할 CSV 파일 경로
    """
    np.random.seed(42)  # 재현성을 위한 시드 설정

    n_samples = 200

    # 자기조절학습 전략 변수들 생성 (1-5 척도)
    data = {
        'time_management': np.random.normal(3.5, 0.8, n_samples).clip(1, 5),
        'environment_structuring': np.random.normal(3.2, 0.9, n_samples).clip(1, 5),
        'goal_setting': np.random.normal(3.7, 0.7, n_samples).clip(1, 5),
        'self_evaluation': np.random.normal(3.4, 0.8, n_samples).clip(1, 5),
        'learning_engagement': np.random.normal(3.3, 0.9, n_samples).clip(1, 5)
    }

    df = pd.DataFrame(data)

    # 참여도와 전략 간의 현실적인 상관관계 추가
    # 시간 관리와 참여도가 가장 강한 상관관계
    df['learning_engagement'] = (
        df['time_management'] * 0.4 +
        df['goal_setting'] * 0.3 +
        df['self_evaluation'] * 0.2 +
        df['environment_structuring'] * 0.1 +
        np.random.normal(0, 0.3, n_samples)
    ).clip(1, 5)

    # 정수로 반올림
    df = df.round(2)

    # CSV로 저장
    df.to_csv(filepath, index=False)
    print(f"샘플 데이터가 생성되어 {filepath}에 저장되었습니다.")
    print(f"데이터 크기: {df.shape}")

    return df

def load_data(filepath):
    """
    설문 데이터를 로드하고 기본 전처리를 수행합니다.

    Parameters:
    -----------
    filepath : str
        CSV 파일 경로

    Returns:
    --------
    pd.DataFrame
        전처리된 데이터프레임
    """
    df = pd.read_csv(filepath)

    # 결측치 확인
    print("결측치 현황:")
    print(df.isnull().sum())

    # 기본 통계
    print("\n기술 통계:")
    print(df.describe())

    return df

def analyze_correlation(df, strategy_cols, engagement_col):
    """
    자기조절학습 전략과 참여도 간의 상관관계를 분석합니다.

    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터프레임
    strategy_cols : list
        전략 변수 컬럼명 리스트
    engagement_col : str
        참여도 변수 컬럼명

    Returns:
    --------
    pd.DataFrame
        상관계수 행렬
    """
    # 상관분석
    correlation_matrix = df[strategy_cols + [engagement_col]].corr()

    # 시각화
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('자기조절학습 전략과 참여도의 상관관계')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')

    # 환경 변수나 대화형 모드에서만 show
    if os.environ.get('DISPLAY') or os.environ.get('SHOW_PLOTS', 'false').lower() == 'true':
        plt.show()
    else:
        print("플롯이 저장되었습니다: correlation_heatmap.png")

    return correlation_matrix

def regression_analysis(df, independent_vars, dependent_var):
    """
    다중 회귀분석을 수행합니다.

    Parameters:
    -----------
    df : pd.DataFrame
        분석할 데이터프레임
    independent_vars : list
        독립변수 컬럼명 리스트
    dependent_var : str
        종속변수 컬럼명

    Returns:
    --------
    dict
        회귀분석 결과
    """
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error

    X = df[independent_vars]
    y = df[dependent_var]

    # 회귀 모델 학습
    model = LinearRegression()
    model.fit(X, y)

    # 예측
    y_pred = model.predict(X)

    # 결과
    results = {
        'coefficients': dict(zip(independent_vars, model.coef_)),
        'intercept': model.intercept_,
        'r_squared': r2_score(y, y_pred),
        'rmse': np.sqrt(mean_squared_error(y, y_pred))
    }

    print("\n회귀분석 결과:")
    print(f"R² = {results['r_squared']:.3f}")
    print(f"RMSE = {results['rmse']:.3f}")
    print("\n회귀계수:")
    for var, coef in results['coefficients'].items():
        print(f"  {var}: {coef:.3f}")

    return results

# 메인 실행
if __name__ == "__main__":
    # 데이터 파일 경로
    data_file = 'survey_data.csv'

    # 데이터 로드 (파일이 없으면 샘플 데이터 생성)
    try:
        df = load_data(data_file)
        print(f"기존 데이터 파일 '{data_file}'을(를) 로드했습니다.")
    except FileNotFoundError:
        print(f"데이터 파일 '{data_file}'이(가) 존재하지 않습니다.")
        print("샘플 데이터를 생성합니다...")
        df = generate_sample_data(data_file)

    # 변수 정의
    strategy_cols = [
        'time_management',
        'environment_structuring',
        'goal_setting',
        'self_evaluation'
    ]
    engagement_col = 'learning_engagement'

    # 상관분석
    corr_matrix = analyze_correlation(df, strategy_cols, engagement_col)

    # 회귀분석
    results = regression_analysis(df, strategy_cols, engagement_col)

    print("\n분석 완료!")

# === 시연 포인트 ===
# 1. Copilot이 주석을 이해하고 적절한 함수 생성
# 2. 함수명, 파라미터, docstring 자동 생성
# 3. 데이터 분석 로직 제안
# 4. 시각화 코드까지 포함

# 강사 멘트:
# "보시다시피 Copilot이 데이터 분석 코드를 자동으로 생성합니다."
# "함수 구조, docstring, 심지어 시각화까지 제안합니다."
# "물론 이것도 초안입니다. 본인이 검토하고 수정해야 합니다."
# "하지만 반복적인 코드 작성 시간을 크게 줄여줍니다."
# "연구 방법론 구현도 AI가 도와줍니다."