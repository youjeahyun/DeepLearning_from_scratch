import numpy as np
from scipy.special import expit  # sigmoid 함수

def init_network():
    # 신경망의 가중치와 바이어스를 초기화하는 함수
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])  # 1층 가중치
    network['b1'] = np.array([[0.1, 0.2, 0.3]])                    # 1층 바이어스
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) # 2층 가중치
    network['b2'] = np.array([[0.1, 0.2]])                        # 2층 바이어스
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])             # 3층 가중치
    network['b3'] = np.array([[0.1, 0.2]])                        # 3층 바이어스

    return network

def forward(network, x):
    # 입력 데이터를 이용해 순전파를 수행하는 함수
    W1, W2, W3 = network['W1'], network['W2'], network['W3'] # 가중치 로드
    b1, b2, b3 = network['b1'], network['b2'], network['b3'] # 바이어스 로드

    # 1층의 연산 (가중치 합계 + 바이어스 -> 활성화 함수)
    a1 = np.dot(x, W1) + b1  # 행렬 곱셈 및 바이어스 더하기
    z1 = expit(a1)           # 활성화 함수 (시그모이드 함수)

    # 2층의 연산 (가중치 합계 + 바이어스 -> 활성화 함수)
    a2 = np.dot(z1, W2) + b2 # 행렬 곱셈 및 바이어스 더하기
    z2 = expit(a2)           # 활성화 함수 (시그모이드 함수)

    # 3층의 연산 (가중치 합계 + 바이어스)
    a3 = np.dot(z2, W3) + b3 # 행렬 곱셈 및 바이어스 더하기

    return a3

# 네트워크 초기화
network = init_network()

# 입력 데이터
x = np.array([1.0, 0.5])

# 순전파 계산
y = forward(network, x)

# 결과 출력
print(y)
