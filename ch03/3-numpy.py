import numpy as np


A = np.array([[1,2], [3,4]])
print(A.shape)  # (2, 2)

B = np.array([[5,6], [7,8]])
print(B.shape)  # (2, 2)

C = np.dot(A, B)
print(C)

A = np.array([[1,2,3], [4,5,6]])
print(A.shape)  # (2, 3)

B = np.array([[5,6], [7,8], [9, 10]])
print(B.shape)  # (3, 2)

C = np.dot(A, B)
print(C)

C = np.array([[1,2], [3,4]])
C.shape # (2, 2)

# print(np.dot(A, C)) # 오류

A = np.array([[1,2], [3,4], [4,5]])
print(A)
print(A.shape)

B = np.array([7,8])
print(B)
print(B.shape)

print(np.dot(A, B))