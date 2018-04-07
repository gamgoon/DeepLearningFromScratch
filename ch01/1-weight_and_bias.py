import numpy as np

x = np.array([0, 1])    # input
w = np.array([0.5, 0.5])    # weight
b = -0.7    # bias
print(w * x)

print(np.sum(w * x))

print(np.sum(w * x) + b)    # 대략 -0.2


def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(and_gate(0, 0))
print(and_gate(1, 0))
print(and_gate(0, 1))
print(and_gate(1, 1))

print(nand_gate(0, 0))
print(nand_gate(1, 0))
print(nand_gate(0, 1))
print(nand_gate(1, 1))

print(or_gate(0, 0))
print(or_gate(1, 0))
print(or_gate(0, 1))
print(or_gate(1, 1))
