import numpy as np

def relu(x):
    return np.maximum(0, x) #입력값이 0보다 크면 출력 아니면 0

A = np.array([1,2,3,4])
#print(A)
#print(np.ndim(A)) #배열의 차원을 출력
#print(A.shape) #배열의 형태 확인 (튜플형태)
#print(A.shape[0]) #배열의 첫 번째 차원의 크기

B = np.array([[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B)) #배열의 차원을 출력
print(B.shape) #배열의 형태 확인
