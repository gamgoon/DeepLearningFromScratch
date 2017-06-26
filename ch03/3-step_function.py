import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

def step_function3(x):
    return np.array(x > 0, dtype=np.int)
#
# x = np.array([-1.0, 1.0, 2.0])
# print(x)
#
# y = x > 0
# print(y)
#
# y = y.astype(np.int)
# print(y)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function3(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
