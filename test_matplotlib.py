import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
x = np.arange(0, 6, 0.1)  # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

print('-------------')
print(y1)
print('-------------')
print(y2)
print('-------------')

# 그래프 그리기
plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--',label='cos') #코사인은 점선으로 그리기
plt.xlabel('x') #x축 라벨
plt.ylabel('y') #y축 라벨
plt.title('sin & cos')
plt.legend()
plt.show()