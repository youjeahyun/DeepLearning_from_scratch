import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit  # sigmoid 함수

# 입력층에서 1층으로 신호전달
X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([[0.1,0.2,0.3]])

A1 = np.dot(X,W1) +B1
#print(A1)
Z1 = expit(A1)
#print(Z1) #[[0.57444252 0.66818777 0.75026011]]

# 1층에서 2층으로의 신호전달
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1,W2) + B2
#print(A2) #[[0.51615984 1.21402696]]
Z2 = expit(A2)

#2층에서 출력층으로 신호전달
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2,W3) + B3
print(A3)