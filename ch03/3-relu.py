# RELU (Rectified Linear Unit) 함수
# 입력이 0을 넘으면 그 입력을 그대로 출력
import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 5.1) # y축 범위를 지정.
plt.show()
