# 시그모이드 함수 구현
# 기본 식 h(x) = 1 / (1 + np.exp(-x))
# exp(-x) 는 e 의 -x 승. e는 자연상수 2.7182...의 값을 갖는 실수.

import numpy as np
import matplotlib.pylab as plt


# 브로드캐스트 기능 참 신기하다 했는데, np.exp(-x) 가 넘파이 배열을 반환하니까
# 결과적으로 1 / (1 + np.exp(-x)) 도 넘파이 배열의 각 원소에 연산을 수행한 결과를 낸다.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1) # y축 범위를 지정.
# plt.show()


# 아래는 채민이의 생애 첫 타이핑!!!
# 시작합니다 감채민가족