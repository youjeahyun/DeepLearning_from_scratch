#딥러닝을 구현하다 보면 배열이나 행렬 계산이 등장함, 배열클래스인 넘파이를 이용하면 편리한 메서드가 많이있어서 강력한 파이썬의 외부 라이브러리이다.

import numpy as np

#넘파이 배열 생성
x = np.array([1.0, 2.0, 3.0])
print('*넘파이 배열 생성')
print(x) #[1. 2. 3.]
print(type(x)) #<class 'numpy.ndarray'>
print('*넘파이 배열 생성 끝')
print('')

#넘파이 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print('*넘파이 산술 연산')
print(x + y) #덧
print(x - y) #뺄
print(x * y) #곱
print(x / y) #나눔
print('*넘파이 산술 연산 끝')
print('')
# 배열 x 와 y의 원소가 같아야 연산이 행해진다.
# 단 넘파이 배열은 원소별 계산 뿐 아니라 넘파이 배열과 수치하나(스칼라값) 의 조합으로 된 산술 연산은 수행이 가능하다.(브로드캐스트)

#넘파이 N차원 배열
print('*넘파이 n차원 배열')
A = np.array([[1,2], [3,4]])
print(A)
print(A.shape) #2,2 2행 2열 의미 (배열의 형상)
print(A.dtype) # 배열의 원소데이터 타입

B = np.array([[3,0], [0,6]])
print(A+B)
print(A*B)

print('*넘파이 n차원 배열 끝')
print('')
# 넘파이 배열은 n차원 배열을 작성 할 수 있다. 수학에서 1차원 배열은 벡터 2차원배열은 행렬이라고 부르는데, 일반화 한것을 텐서라고 한다.

#브로드캐스트
#넘파이에서 형상이 다른 배열끼리 계산할 수 있는데 스칼라값을 계산하면 단일값이 행렬에 맞게 확대 된 후 연산이 이뤄지는것을 브로드 캐스트라 함
print('*브로드 캐스트')
A = np.array([[1,2], [3,4]])
B = np.array([10,20])
print(A * B) # [[1,2], [3,4]] * [[10,20], [10,20]] 의 계산식을 얻게됨.
print('*브로드 캐스트 끝')
print('')

#원소 접근
print('*원소 접근')
X = np.array([[51,55],[14,19],[0,4]])
print(X)
print(X[0]) #0행
print(X[:, 0]) #0열
print(X[0][1]) #0,1 의 원소

num=1
for row in X:
    print('for으로' + str(num) + '행의 원소를')
    print(row)
    num = num+1

X = X.flatten() #X를 1차원 배열로 변환 (평탄화)
print('1차원 평탄화')
print(X)
print('*원소 접근 끝')
print(X[[0,2,4]]) # 인덱스가 0 2 4 인 원소얻기

print( X > 15)
print(X[X>15]) # X배열에서 15보다 큰 원소만 추출
print('')