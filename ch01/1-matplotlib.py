import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
print(x)
y1 = np.sin(x)
y2 = np.cos(x)
print(y1)
print(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos') #제목
plt.legend()
plt.show()

img = imread('test.png')
plt.imshow(img)
plt.show()