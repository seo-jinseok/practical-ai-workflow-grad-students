# 전공별 활용 예시 모음

**목적**: 다양한 전공에서 AI 도구와 연구 워크플로우를 효과적으로 활용하는 실전 예시  
**소요 시간**: 관심 전공 부분만 3-5분 읽기  
**대상**: 모든 전공의 대학원생 및 연구자  

---

## 🎓 인문사회계열

### 교육학/교육공학

#### 연구 주제 예시: 온라인 학습 참여도 개선
```markdown
**연구 상황**:
- 문제: 코로나19 이후 온라인 수업 참여도 40% 감소
- 방법: 게임화 요소 적용과 참여도 측정
- 대상: 대학생 200명 (교육학과 120명, 타학과 80명)

**AI 도구 활용 방법**:
1. **문헌 조사**: "온라인 학습 참여도" + "게임화" 키워드로 50편 문헌 수집
2. **측정 도구 개발**: AI에게 5점 리커트 척도 문항 15개 생성 요청
3. **통계 분석**: Python으로 t-test, ANOVA, 효과크기 계산
4. **논문 작성**: 교육학적 이론과 prático 결과를 연결한 논의

**유용한 AI 질문**:
"교육학 연구에서 온라인 학습 참여도를 측정하는 
ivalid하고 reliable한 척도를 만들어주세요. 
행동적, 인지적, 정서적 참여를 모두 포함해서요."

**특수 고려사항**:
- IRB 승인 필수 (인간 대상 연구)
- 학제적 관점: 교육학 + 심리학 + 기술학 이론 결합
- 한국적 맥락: 한국의 교육 문화와 온라인 학습 환경 반영
```

#### 연구 주제 예시: AI 기반 개인화 학습 효과
```markdown
**연구 상황**:
- 문제: 학습자별 개별적 학습 요구 충족 어려움
- 방법: AI 추천 시스템 적용 전후 비교 실험
- 대상: 고등학생 300명, 수학 과목

**AI 도구 활용 방법**:
1. **이론적 배경**: AI in Education, Personalized Learning theories
2. **연구 설계**: 준실험 설계 (실험군 vs 대조군)
3. **데이터 분석**: 추천 정확도, 학습 성과, 만족도 비교
4. **시각화**: 학습 진도와 성취도 변화를 그래프로 표현

**Python 코드 예시**:
```python
# AI 추천 시스템 효과 분석
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# 학습 성과 비교
ai_group = [85, 78, 92, 88, 79, 86, 90, 84, 87, 89]
control_group = [72, 68, 75, 70, 73, 71, 74, 69, 76, 72]

# t-test
t_stat, p_value = stats.ttest_ind(ai_group, control_group)
effect_size = (np.mean(ai_group) - np.mean(control_group)) / np.sqrt((np.var(ai_group) + np.var(control_group)) / 2)

print(f"AI 그룹 평균: {np.mean(ai_group):.2f}")
print(f"통제 그룹 평균: {np.mean(control_group):.2f}")
print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")
print(f"효과크기 (Cohen's d): {effect_size:.3f}")
```
```

---

### 심리학/상담심리학

#### 연구 주제 예시: 대학생 정신건강과 소셜미디어 사용
```markdown
**연구 상황**:
- 문제: 대학생 우울, 불안 증가와 소셜미디어 연관성
- 방법: 설문조사 (기분, 불안, 소셜미디어 사용 시간)
- 대상: 대학생 500명

**AI 도구 활용 방법**:
1. **심리 척도 선택**: PHQ-9 (우울), GAD-7 (불안) 척도 활용
2. **데이터 수집**: Google Forms로 온라인 설문
3. **통계 분석**: 상관관계, 회귀분석으로 소셜미디어 사용과 정신건강의 관계
4. **결과 해석**: 심리학적 이론으로 결과 설명

**유용한 AI 질문**:
"대학생의 소셜미디어 사용과 정신건강 관계 연구에서 
어떤 심리 척도를 사용하고, 어떤 통계 분석을 해야 할까요? 
유의수준, 효과크기, 중개효과 분석도 포함해서 알려주세요."

**심리학 연구 특화 팁**:
- 윤리적 고려: 심리적 위험 최소화, 탈락 권한 보장
- 척도 신뢰도: Cronbach's α 0.7 이상 확보
- 표본 크기: 효과크기 0.5, power 0.8, α 0.05 → 최소 128명
- 결과 해석: 통계적 유의성 ≠ 실제적 유의성
```

#### 연구 주제 예시: MBSR 기반 스트레스 관리 프로그램 효과
```markdown
**연구 상황**:
- 문제: 대학생 스트레스 증가와 대응 전략 부족
- 방법: MBSR (Mindfulness-Based Stress Reduction) 8주 프로그램
- 대상: 스트레스 높은 대학생 80명 (실험 40명, 통제 40명)

**AI 도구 활용 방법**:
1. **프로그램 설계**: 8주 MBSR 세션 구성과 활동 계획
2. **측정 도구**: 스트레스(PSS), 마음챙김(FFMQ), 대처전략(COPE)
3. **사전-사후 측정**: 3회 측정 (사전, 중간, 사후)
4. **질적 연구**: 포커스 그룹 인터뷰로 경험적 내용 수집

**디자인 고려사항**:
- 무작위 배치: 실험군/통제군 무작위 할당
- 매니퓰레이션 체크: 프로그램 참여도 확인
- 대안설명 통제: 통제군에게 equivalent한 주의 제공
- 이탈률 관리: 예상 이탈률 20% 고려한 표본 크기 산정
```

---

### 경제학/경영학

#### 연구 주제 예시: 전자상거래 고객 만족도 결정요인
```markdown
**연구 상황**:
- 문제: 온라인 쇼핑몰의 낮은 고객 유지율
- 방법: 구조방정식 모델링으로 만족도 영향요인 분석
- 대상: 온라인 쇼핑 이용자 1,200명

**AI 도구 활용 방법**:
1. **이론적 모델**: Davis의 기술수용모델(TAM), Oliver의 기대-확신모델
2. **측정 항목**: 사용용이성, 유용성, 신뢰도, 만족도, 재구매의도
3. **통계 분석**: SPSS/AMOS로 확인적 요인분석, 구조방정식 모델링
4. **비즈니스 시사점**: 실직적 실행 가능한 개선 방안 제시

**AI에게 요청할 질문**:
"E-commerce 고객 만족도 연구에서 
기술수용모델(TAM)을 적용할 때 
구체적으로 어떤 측정 항목을 사용해야 할까요? 
한국 소비자 특성을 반영한 항목으로 제안해주세요."

**경제학/경영학 연구 특징**:
- 실무 적용성: 이론적 기여 + 실무적 시사점
- 대용량 데이터: 설문지보다 실제 거래 데이터 활용 가능
- 인과관계 vs 상관관계: 실험적 설계나 자연실험 활용
- 경제적 가치: Cost-benefit analysis 포함
```

---

### 문학/언어학

#### 연구 주제 예시: AI 번역의 문학 작품 해석에 미치는 영향
```markdown
**연구 상황**:
- 문제: AI 번역 도구 발전이 전통적 번역교육에 미치는 영향
- 방법: 비교연구 (AI 도구 사용 vs 비사용 그룹)
- 대상: 번역학과 학생 60명

**AI 도구 활용 방법**:
1. **텍스트 분석**: 원본과 AI 번역의 의미 전달 차이 분석
2. **번역 품질 평가**: 정확성, 자연스러움, 창의성 평가 기준
3. **학습 효과 측정**: 번역 실력 향상 정도를_before-after 비교
4. **질적 분석**: 학생들의 인식과 경험에 대한 심층 인터뷰

**유용한 AI 질문**:
"文学 번역 연구에서 AI와 인간 번역의 
품질 차이를 평가할 수 있는 객관적 기준을 
개발해 주세요. 의미 전달, 문체, 감정 표현 등을 포함해서요."

**인문학 연구 특화 팁**:
- 정량적 측정 어려움: 질적 방법론과 혼합 연구 활용
- 주관적 평가: 전문가 평가와 독자 평가의 차이 고려
- 문화적 맥락: 한국어-영어 번역에서 문화적 차이 중요
- 텍스트 다양성: 소설, 시, 수필 등 장르별 특성 고려
```

---

## 🔬 자연과학계열

### 물리학/화공학

#### 연구 주제 예시: 나노 소재의 전기적 성질 연구
```markdown
**연구 상황**:
- 문제: graphene 기반 나노 소재의 전기전도도 향상
- 방법: 합성 조건 변화에 따른 전기적 성질 측정
- 대상: 합성된 graphene 샘플 150개

**AI 도구 활용 방법**:
1. **실험 설계**: 2^k 요인 실험으로 최적 합성 조건 탐색
2. **데이터 분석**: Python으로 회귀분석, 상관관계 분석
3. **시각화**: 3D surface plot으로 합성 조건과 전기전도도 관계 표현
4. **결과 예측**: machine learning 모델로 새로운 합성 조건 예측

**Python 코드 예시**:
```python
# 나노 소재 전기전도도 분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 합성 조건 데이터
data = pd.read_csv('graphene_synthesis_data.csv')
X = data[['temperature', 'pressure', 'time', 'catalyst_ratio']]
y = data['electrical_conductivity']

# Random Forest로 전기전도도 예측
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)

# 특성 중요도 분석
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print("특성 중요도:")
print(feature_importance)

# 최적 조건 예측
optimal_conditions = [850, 50, 120, 0.15]  # 최적값 예시
predicted_conductivity = rf.predict([optimal_conditions])[0]
print(f"예상 전기전도도: {predicted_conductivity:.2f} S/cm")
```
```

---

### 생물학/의학

#### 연구 주제 예시: 감염병 실시간 진단 AI 시스템 개발
```markdown
**연구 상황**:
- 문제: 감염병 조기 진단의 중요성과 기존 검사법의 한계
- 방법: machine learning 기반 이미지 분석 AI 개발
- 대상: 흉부 X-ray 이미지 10,000장, 혈액 검사 데이터 5,000건

**AI 도구 활용 방법**:
1. **데이터 전처리**: 이미지 정규화, 노이즈 제거, 데이터 증강
2. **모델 개발**: CNN (Convolutional Neural Network) 활용
3. **성능 평가**: accuracy, precision, recall, F1-score 계산
4. **임상 검증**: 병원과의 협력으로 실제 환자 데이터로 검증

**특수 고려사항**:
- IRB 승인 필수 (의학 연구)
- 개인정보 보호: 의료정보 익명화
- 규제 준수: 의료기기 인증 관련法规
- 임상시험: phase별 검증 과정 필요

**AI가 돕는 부분**:
```python
# 의료 이미지 분류 CNN 모델 (TensorFlow/Keras)
import tensorflow as tf
from tensorflow.keras import layers, models

# CNN 모델 구성
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')  # binary classification
])

# 모델 컴파일 및 훈련
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', 'precision', 'recall'])

# 훈련
history = model.fit(X_train, y_train,
                    epochs=20,
                    validation_data=(X_val, y_val),
                    callbacks=[tf.keras.callbacks.EarlyStopping(patience=5)])
```
```

---

### 컴퓨터공학/AI

#### 연구 주제 예시: 실시간 얼굴 인식을 위한 경량 딥러닝 모델
```markdown
**연구 상황**:
- 문제: 모바일 기기에서의 실시간 얼굴 인식 성능과功耗 균형
- 방법: 모델 압축 기법 적용 및 성능 비교
- 대상: 다양한 크기의 neural network 모델 5개

**AI 도구 활용 방법**:
1. **baseline 모델**: ResNet-50, MobileNet, EfficientNet 등 비교
2. **압축 기법**: pruning, quantization, knowledge distillation
3. **성능 평가**: 정확도, 추론 속도, 메모리 사용량, 배터리 소모
4. **edge deployment**: 실제 모바일 기기에서의 성능 측정

**연구 설계**:
```python
# 모델 압축 및 성능 비교
import torch
import torch.nn as nn
import time
import psutil

class ModelEvaluator:
    def __init__(self, model):
        self.model = model
        self.model.eval()
    
    def measure_inference_time(self, input_tensor, num_runs=100):
        times = []
        for _ in range(num_runs):
            start_time = time.time()
            with torch.no_grad():
                output = self.model(input_tensor)
            end_time = time.time()
            times.append(end_time - start_time)
        return np.mean(times), np.std(times)
    
    def measure_memory_usage(self):
        process = psutil.Process()
        memory_info = process.memory_info()
        return memory_info.rss / 1024 / 1024  # MB
    
    def measure_model_size(self):
        torch.save(self.model.state_dict(), "temp_model.pth")
        size_mb = os.path.getsize("temp_model.pth") / 1024 / 1024
        os.remove("temp_model.pth")
        return size_mb

# 모델 성능 평가 예시
evaluator = ModelEvaluator(model)
avg_time, std_time = evaluator.measure_inference_time(test_input)
memory_mb = evaluator.measure_memory_usage()
size_mb = evaluator.measure_model_size()

print(f"추론 시간: {avg_time:.3f} ± {std_time:.3f} 초")
print(f"메모리 사용량: {memory_mb:.1f} MB")
print(f"모델 크기: {size_mb:.1f} MB")
```

---

## 🔧 공학계열

### 기계공학/재료공학

#### 연구 주제 예시: 3D 프린팅 최적 파라미터 도출
```markdown
**연구 상황**:
- 문제: 3D 프린팅 품질과 인쇄 시간, 비용의 최적화
- 방법: 반응표면법(RSM)으로 최적 조건 탐색
- 대상: 3D 프린팅 파라미터 (온도, 속도, 레이어 높이)

**AI 도구 활용 방법**:
1. **실험 설계**:central composite design (CCD) 또는 Box-Behnken design
2. **반응변수**: 인장강도, 표면 거칠기, 인쇄 시간, 재료 사용량
3. **최적화**: 다목적 최적화 (Pareto front 도출)
4. **검증 실험**: 최적 조건에서 재현성 확인

**특수 도구 활용**:
```python
# 반응표면법 (Response Surface Method)
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
import matplotlib.pyplot as plt

# 실험 데이터 생성 (예시)
np.random.seed(42)
n_samples = 100

# 입력 변수: 온도(180-220°C), 속도(50-150mm/s), 레이어높이(0.1-0.3mm)
temperature = np.random.uniform(180, 220, n_samples)
speed = np.random.uniform(50, 150, n_samples)
layer_height = np.random.uniform(0.1, 0.3, n_samples)

# 출력 변수: 인장강도, 표면거칠기, 인쇄시간
tensile_strength = 45 + 0.2*temperature + 0.05*speed - 50*layer_height + np.random.normal(0, 2, n_samples)
surface_roughness = 3 - 0.01*temperature - 0.02*speed + 10*layer_height + np.random.normal(0, 0.2, n_samples)
print_time = 10 - 0.03*temperature - 0.05*speed + 20*layer_height + np.random.normal(0, 1, n_samples)

# 데이터 프레임 생성
data = pd.DataFrame({
    'temperature': temperature,
    'speed': speed,
    'layer_height': layer_height,
    'tensile_strength': tensile_strength,
    'surface_roughness': surface_roughness,
    'print_time': print_time
})

# 다목적 회귀 모델
X = data[['temperature', 'speed', 'layer_height']]
y = data[['tensile_strength', 'surface_roughness', 'print_time']]

# Random Forest Multi-output 모델
rf_multi = MultiOutputRegressor(RandomForestRegressor(n_estimators=100))
rf_multi.fit(X, y)

# 최적화 ( Genetic Algorithm 사용)
from deap import base, creator, tools, algorithms
import random

# 최적화 목적 함수: 인장강도 최대화, 표면거칠기 최소화, 인쇄시간 최소화
def evaluate(individual):
    temperature, speed, layer_height = individual
    X_test = np.array([[temperature, speed, layer_height]])
    predictions = rf_multi.predict(X_test)[0]
    strength, roughness, print_time = predictions
    
    # 다목적 최적화 (가중치 합)
    score = strength - 2*roughness - 0.5*print_time
    return score,
```

---

### 전자공학/정보통신공학

#### 연구 주제 예시: 5G 네트워크 최적화 알고리즘 개발
```markdown
**연구 상황**:
- 문제: 5G 네트워크에서 지연 시간과 처리량 간의 균형
- 방법: 강화학습 기반 자원 할당 알고리즘 개발
- 대상: 시뮬레이션 환경 (Python + ns-3)

**AI 도구 활용 방법**:
1. **시뮬레이션 환경**: ns-3로 5G 네트워크 시뮬레이션 구현
2. **강화학습 모델**: DQN (Deep Q-Network) 또는 Actor-Critic 사용
3. **보상 함수**: 지연시간, 처리량, 에너지 효율성 고려
4. **성능 평가**: 기존 알고리즘과 비교 (A2C, round-robin 등)

**실험 설계**:
```python
# 5G 네트워크 시뮬레이션 + 강화학습
import numpy as np
import gym
from stable_baselines3 import DQN, A2C, PPO
from stable_baselines3.common.env_util import make_vec_env
import matplotlib.pyplot as plt

class NetworkEnvironment(gym.Env):
    def __init__(self):
        super(NetworkEnvironment, self).__init__()
        
        # 상태 공간: [이동통신사 수, 트래픽 부하, 채널 품질]
        self.action_space = gym.spaces.Discrete(3)  # 0: 저부하, 1: 중부하, 2: 고부하
        self.observation_space = gym.spaces.Box(
            low=0, high=100, shape=(3,), dtype=np.float32
        )
        
        # 네트워크 파라미터
        self.max_latency = 10  # ms
        self.min_throughput = 50  # Mbps
        
    def reset(self):
        self.current_load = np.random.uniform(20, 80)
        self.current_quality = np.random.uniform(30, 90)
        self.current_users = np.random.randint(10, 100)
        
        return np.array([self.current_load, self.current_quality, self.current_users])
    
    def step(self, action):
        # action에 따른 자원 할당
        if action == 0:  # 저부하 할당
            latency = max(1, self.current_load * 0.05 + np.random.normal(0, 1))
            throughput = min(100, self.current_quality * 1.2 + np.random.normal(0, 5))
        elif action == 1:  # 중부하 할당
            latency = max(1, self.current_load * 0.1 + np.random.normal(0, 2))
            throughput = min(100, self.current_quality * 1.0 + np.random.normal(0, 8))
        else:  # 고부하 할당
            latency = max(1, self.current_load * 0.2 + np.random.normal(0, 3))
            throughput = min(100, self.current_quality * 0.8 + np.random.normal(0, 10))
        
        # 보상 함수: 지연시간 페널티, 처리량 보상, 품질 페널티
        latency_penalty = max(0, latency - self.max_latency) * 10
        throughput_reward = max(0, throughput - self.min_throughput) * 0.5
        quality_penalty = max(0, 100 - self.current_quality) * 0.1
        
        reward = -latency_penalty + throughput_reward - quality_penalty
        
        # done condition
        done = latency > 50 or throughput < 10
        
        info = {
            'latency': latency,
            'throughput': throughput,
            'action': action
        }
        
        return np.array([self.current_load, self.current_quality, self.current_users]), reward, done, info

# 환경 생성 및 훈련
env = make_vec_env(lambda: NetworkEnvironment(), n_envs=1)

# DQN 모델 훈련
model = DQN('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)

# 성능 평가
obs = env.reset()
cumulative_reward = 0
latencies, throughputs = [], []

for _ in range(100):
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    cumulative_reward += reward
    latencies.append(info[0]['latency'])
    throughputs.append(info[0]['throughput'])
    if done:
        obs = env.reset()

print(f"평균 누적 보상: {cumulative_reward/100:.2f}")
print(f"평균 지연시간: {np.mean(latencies):.2f} ms")
print(f"평균 처리량: {np.mean(throughputs):.2f} Mbps")
```
```

---

## 🎨 예체능계열

### 디자인/예술학

#### 연구 주제 예시: VR 기반 예술 교육의 학습 효과
```markdown
**연구 상황**:
- 문제: 전통적 예술 교육의 한계와 VR 기술의 적용 가능성
- 방법: 혼합 연구법 (정량 + 정성)
- 대상: 예술학과 학생 80명

**AI 도구 활용 방법**:
1. **VR 콘텐츠 평가**: 전문가 평정을 통한 콘텐츠 품질 평가
2. **학습 성과 측정**: before-after 능력 평가,創作成품 분석
3. **정성적 연구**: 심층 인터뷰로 학습 경험과感想 수집
4. **시각적 자료**: VR 사용 전후 작품 비교, brain mapping 결과

**연구 설계**:
```python
# 예술작품 품질 평가 시스템
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def analyze_artwork_quality(image_path):
    """예술작품의 색상 조화, 구도, 복잡도 분석"""
    
    # 이미지 로드 및 전처리
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape
    
    # 색상 분석 (주요 색상 추출)
    pixels = img_rgb.reshape(-1, 3)
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # 색상 다양성 지수
    color_diversity = len(np.unique(labels)) / (h * w)
    
    # 구도 분석 (rule of thirds)
    thirds_x = [w//3, 2*w//3]
    thirds_y = [h//3, 2*h//3]
    
    # 주요 요소의 위치 분석 (간소화: 가장 많이 나타나는 색상 위주로)
    dominant_color = colors[np.argmax(np.bincount(labels))]
    
    # 복잡도 분석 (에지 검출)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    edge_density = np.sum(edges > 0) / (h * w)
    
    return {
        'color_diversity': color_diversity,
        'dominant_color': dominant_color,
        'edge_density': edge_density,
        'composition_balance': 'balanced'  # 간소화된 평가
    }

#.before-after 비교 분석
before_analysis = analyze_artwork_quality('artwork_before.jpg')
after_analysis = analyze_artwork_quality('artwork_after.jpg')

print("학습 전후 예술작품 분석:")
print(f"색상 다양성: {before_analysis['color_diversity']:.3f} → {after_analysis['color_diversity']:.3f}")
print(f"복잡도: {before_analysis['edge_density']:.3f} → {after_analysis['edge_density']:.3f}")
```
```

---

### 체육학/운동과학

#### 연구 주제 예시: 웨어러블 기기를 활용한 운동 효과 분석
```markdown
**연구 상황**:
- 문제: 개인 맞춤형 운동 프로그램의 효과성 입증
- 방법: 웨어러블 디바이스 데이터 기반 개인화 운동
- 대상: 성인 200명, 12주 운동 프로그램

**AI 도구 활용 방법**:
1. **데이터 수집**: 심박수, 걸음수, 수면 패턴, 활동량 데이터
2. **개인화 알고리즘**:机器学习으로 개인별 최적 운동 강도 도출
3. **생체지표 분석**: 운동 전후 체력 측정, 혈액 검사 결과
4. **행동 변화**: 웨어러블 데이터로 실제 생활 패턴 변화 추적

**실제 활용**:
```python
# 웨어러블 데이터 분석 및 개인화 운동 추천
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class PersonalFitnessAI:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.user_data = None
    
    def load_user_data(self, csv_file):
        """사용자 웨어러블 데이터 로드"""
        self.user_data = pd.read_csv(csv_file)
        return self.user_data
    
    def analyze_sleep_pattern(self, user_id):
        """수면 패턴 분석"""
        user_sleep = self.user_data[self.user_data['user_id'] == user_id]
        
        if len(user_sleep) == 0:
            return "사용자 데이터를 찾을 수 없습니다."
        
        avg_sleep_duration = user_sleep['sleep_hours'].mean()
        sleep_consistency = user_sleep['sleep_hours'].std()
        sleep_efficiency = user_sleep['sleep_efficiency'].mean()
        
        # 수면 품질 평가
        if avg_sleep_duration >= 7 and sleep_consistency <= 1:
            sleep_quality = "우수"
        elif avg_sleep_duration >= 6:
            sleep_quality = "보통"
        else:
            sleep_quality = "개선 필요"
        
        return {
            'avg_sleep_hours': avg_sleep_duration,
            'sleep_consistency': sleep_consistency,
            'sleep_efficiency': sleep_efficiency,
            'quality_grade': sleep_quality
        }
    
    def recommend_exercise_intensity(self, user_id):
        """개인 맞춤형 운동 강도 추천"""
        user_data = self.user_data[self.user_data['user_id'] == user_id]
        
        if len(user_data) == 0:
            return "사용자 데이터를 찾을 수 없습니다."
        
        # 특성 엔지니어링
        features = user_data[['resting_heart_rate', 'avg_daily_steps', 'sleep_hours', 'age']].mean()
        
        # Target Heart Rate Zone 계산
        age = features['age']
        max_hr = 220 - age
        resting_hr = features['resting_heart_rate']
        
        # 5개 구간 권장 ( recuperation, base, fat_burn, cardio, max )
        zones = {
            'recuperation': (0.5 * (max_hr - resting_hr) + resting_hr, 0.6 * (max_hr - resting_hr) + resting_hr),
            'base': (0.6 * (max_hr - resting_hr) + resting_hr, 0.7 * (max_hr - resting_hr) + resting_hr),
            'fat_burn': (0.7 * (max_hr - resting_hr) + resting_hr, 0.8 * (max_hr - resting_hr) + resting_hr),
            'cardio': (0.8 * (max_hr - resting_hr) + resting_hr, 0.9 * (max_hr - resting_hr) + resting_hr),
            'max': (0.9 * (max_hr - resting_hr) + resting_hr, max_hr)
        }
        
        # 현재 피트니스 레벨 평가
        avg_steps = features['avg_daily_steps']
        sleep_quality = features['sleep_hours']
        
        if avg_steps >= 10000 and sleep_quality >= 7:
            recommended_zone = 'cardio'
        elif avg_steps >= 8000:
            recommended_zone = 'fat_burn'
        else:
            recommended_zone = 'base'
        
        return {
            'max_heart_rate': max_hr,
            'resting_heart_rate': resting_hr,
            'target_zones': zones,
            'recommended_zone': recommended_zone,
            'reasoning': f"현재 평균 {avg_steps:.0f}걸음, 수면 {sleep_quality:.1f}시간 기준으로 {recommended_zone} 구간을 추천합니다."
        }
    
    def generate_weekly_plan(self, user_id, goal='weight_loss'):
        """주간 운동 계획 생성"""
        recommendation = self.recommend_exercise_intensity(user_id)
        zone = recommendation['recommended_zone']
        
        # 목표별 주간 계획
        weekly_plans = {
            'weight_loss': {
                'recuperation': '가벼운 걷기 또는 요가 30분',
                'base': '중강도 유산소 45분',
                'fat_burn': '저강도 유산소 30분',
                'cardio': '고강도 인터벌 20분',
                'max': '스프린트 10분'
            },
            'endurance': {
                'recuperation': '가벼운 조깅 20분',
                'base': '중강도 달리기 40분',
                'fat_burn': '장거리 달리기 60분',
                'cardio': '계단오르기 30분',
                'max': '단거리 스프린트 15분'
            },
            'strength': {
                'recuperation': '스트레칭 20분',
                'base': '하체 근력운동 45분',
                'fat_burn': '상체 근력운동 45분',
                'cardio': '전신 근력운동 30분',
                'max': '고강도 인터벌 15분'
            }
        }
        
        plan = weekly_plans.get(goal, weekly_plans['weight_loss'])
        return {
            'goal': goal,
            'weekly_plan': plan,
            'current_zone_focus': plan[zone]
        }

# 사용 예시
fitness_ai = PersonalFitnessAI()

# 데이터 로드 (예시)
# fitness_ai.load_user_data('wearable_data.csv')

# 개인 분석
user_id = 'user_001'
sleep_analysis = fitness_ai.analyze_sleep_pattern(user_id)
exercise_recommendation = fitness_ai.recommend_exercise_intensity(user_id)
weekly_plan = fitness_ai.generate_weekly_plan(user_id, 'weight_loss')

print("수면 분석 결과:")
print(f"평균 수면 시간: {sleep_analysis['avg_sleep_hours']:.1f}시간")
print(f"수면 품질: {sleep_analysis['quality_grade']}")

print("\n운동 추천:")
print(f"권장 구간: {exercise_recommendation['recommended_zone']}")
print(f"근거: {exercise_recommendation['reasoning']}")

print("\n주간 운동 계획:")
for day, activity in weekly_plan['weekly_plan'].items():
    print(f"{day.capitalize()}: {activity}")
```
```

---

## 🌐 인접 분야 융합 사례

### AI + Healthcare (의료 AI)
```markdown
**연구 주제**: AI 기반 개인 맞춤형 약물 용량 최적화
**방법론**: machine learning + 임상 pharmacology
**특수 고려사항**:
- FDA 승인 process
- 임상시험 Phase I, II, III
- 환자 안전과 윤리적 고려사항
- 의료진 대상 Usability study
```

### AI + Environmental Science (환경 AI)
```markdown
**연구 주제**: 기후변화에 따른 생태계 영향 예측 AI
**방법론**: deep learning + climate modeling
**특수 고려사항**:
- 대규모 환경 데이터 처리
- 장기 추적 연구 필요
- 여러 종종과 지역에 대한 generalization
- 정책 입안자 대상 결과 해석
```

### AI + Social Sciences (사회과학 AI)
```markdown
**연구 주제**: 소셜미디어 감정 분석을 통한 정신건강 예측
**방법론**: NLP + 심리학 theory + longitudinal study
**특수 고려사항**:
- 개인정보 보호 (Privacy by design)
- 문화적 차이와 감정 표현의 다양성
- AI 편향(bias)과 공정성(fairness) 문제
- 전통적社会科学 방법론과의 통합
```

---

## 📊 연구 도구별 추천 사례

### SPSS/AMOS 사용자
**특징**: 전통적 통계 분석, 구조방정식 모델링 선호
**AI 활용**:
- 요인분석, 회귀분석 결과 해석 도움
- 구조방정식 모델의 theory-driven 개선
- 다중그룹 비교, 중개효과 분석 해석

### R/Python 사용자
**특징**: 프로그래밍 기반 분석, 기계학습 모델 선호
**AI 활용**:
- 복잡한 알고리즘 구현 assistance
- 시각화 및dash board 개발 지원
-Reproducible research workflow 구축

### Excel/Google Sheets 사용자
**특징**: 기본적인 데이터 분석, 표보고 선호
**AI 활용**:
- 데이터 클리닝 및 전처리 가이드
- 간단한 통계 함수 활용법
- 표 및 차트作成 가이드라인

---

## 🚀 향후 트렌드 및 제언

### 2025년 주목할 만한 융합 분야
1. **AI + Neuroscience**: 뇌-컴퓨터 인터페이스
2. **AI + Agriculture**: 스마트팜 및 지속가능 농업
3. **AI + Urban Planning**: 스마트시티 데이터 분석
4. **AI + Education**: adaptive learning systems
5. **AI + Finance**: algorithmic trading & risk management

### 전공별 AI 활용 팁
```markdown
**모든 전공 공통 팁**:
1. Theory-driven approach: AI 도구로 기존 이론 검증
2. Domain expertise: AI 기술보다 전공 지식이更重要
3. Ethical considerations: 연구윤리와 AI 사용의 투명성
4. Interdisciplinary collaboration: AI 전문가와 융합연구
5. Continuous learning: AI 기술의 rapid development 추종
```

---

**마지막 권고사항**:
AI 도구는 연구의 능력을 확장시키는 도구일 뿐, 연구의 본질은 사람의 창의성과 비판적 사고에 있습니다. 각 전공의 고유한 특성하고 논리적 사고를 유지하면서 AI 도구를 효과적으로 활용하시기 바랍니다.

---

*마지막 업데이트: 2025-11-10*  
*버전: v13.0 Part 1*
