import numpy as np
import matplotlib.pylab as plt

def step_function(x):
   return np.array(x > 0, dtype=np.int64)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

print(y)
plt.plot(x,y)
plt.xlim(-6, 6.1)
plt.ylim(-0.1, 1.1)
plt.show()