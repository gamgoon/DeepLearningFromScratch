def and_gate(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def nand_gate(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def or_gate(x1, x2):
    w1, w2, theta = 1.5, 1.5, 1.
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print(and_gate(0, 0))   # 0
print(and_gate(1, 0))   # 0
print(and_gate(0, 1))   # 0
print(and_gate(1, 1))   # 1

print(nand_gate(0, 0))  # 1
print(nand_gate(1, 0))  # 1
print(nand_gate(0, 1))  # 1
print(nand_gate(1, 1))  # 0

print(or_gate(0, 0))    # 0
print(or_gate(1, 0))    # 1
print(or_gate(0, 1))    # 1
print(or_gate(1, 1))    # 1
