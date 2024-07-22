import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten=True, normalize=False)

# 데이터의 형상  출력
print(x_train.shape) 
print(x_train.shape)
print(x_test.shape)
print(t_test.shape)