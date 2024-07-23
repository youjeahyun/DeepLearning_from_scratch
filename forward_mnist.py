import sys, os
sys.path.append(os.pardir)  # 상위 디렉토리를 시스템 경로에 추가하여 모듈을 검색할 수 있도록 설정

from dataset.mnist import load_mnist  # dataset 패키지의 mnist 모듈에서 load_mnist 함수를 가져옴

# MNIST 데이터셋을 로드
# flatten=True: 28x28 이미지 데이터를 784개의 원소로 된 1차원 배열로 변환
# normalize=False: 픽셀 값을 정규화하지 않고, 0에서 255 사이의 정수 값으로 유지
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 학습 및 테스트 데이터셋의 형상(크기) 출력
print(x_train.shape)  # (60000, 784): 60,000개의 학습 이미지, 각 이미지는 784개의 원소로 구성된 배열
print(t_train.shape)  # (60000,): 60,000개의 학습 라벨
print(x_test.shape)   # (10000, 784): 10,000개의 테스트 이미지, 각 이미지는 784개의 원소로 구성된 배열
print(t_test.shape)   # (10000,): 10,000개의 테스트 라벨
