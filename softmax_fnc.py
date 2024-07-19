import numpy as np


#소프트 맥스의 흐름
a = np.array([[0.3, 2.9, 4.0]])

exp_a = np.exp(a)
#print(exp_a)

sum_exp_a = np.sum(exp_a)
#print(sum_exp_a)

y = exp_a / sum_exp_a
#print(y)

# 위 흐름을 파이썬함수로 정의하면
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) #오버플로 대책, 최댓값을 빼줌
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


a = np.array([1010, 1000, 990])
y = softmax(a)
print(y)
print(np.sum(y)) #출력 총합은 1이 된다는 것이 소프트맥스의 중요한 성질
# 1이 되기에 소프트맥스 함수의 출력을 확률로 해석할수 있음.