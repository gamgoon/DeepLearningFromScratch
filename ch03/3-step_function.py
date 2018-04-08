# 계단 함수 구현하기

import numpy as np
import matplotlib.pylab as plt

# 인수가 0보다 크면 1을 리턴하고, 나머지는 0을 리턴.
# 하지만, 인수로 실수만 받을 수 있다. 넘파이 배열은 넣을 수 없다.
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


# numpy 배열을 인자로 받을 수 있는.
def step_function2(x):
    y = x > 0
    return y.astype(np.int)


# 위 보다 더 간결한 방식
def step_function3(x):
    return np.array(x > 0, dtype=np.int)


x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x > 0
print(y)    # [False True True]

y = y.astype(np.int)    # 넘파이 배열의 자료형을 변환
print(y)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function3(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
