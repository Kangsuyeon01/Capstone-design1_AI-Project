import numpy as np

def AND(x1,x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.7  # 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([-0.5, -0.5])  # 가중치
    b = 0.7  # 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.2  # 편향
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print("AND GATE")
print("x1 x2|","y")
print("---------")
print("0  0 |",AND(0,0))
print("1  0 |",AND(1,0))
print("0  1 |",AND(0,1))
print("1  1 |",AND(1,1))
print()
print("NAND GATE")
print("x1 x2|","y")
print("---------")
print("0  0 |",NAND(0,0))
print("1  0 |",NAND(1,0))
print("0  1 |",NAND(0,1))
print("1  1 |",NAND(1,1))
print()
print("OR GATE")
print("x1 x2|","y")
print("---------")
print("0  0 |",OR(0,0))
print("1  0 |",OR(1,0))
print("0  1 |",OR(0,1))
print("1  1 |",OR(1,1))
print()
print("XOR GATE")
print("---------")
print("0  0 |",XOR(0,0))
print("1  0 |",XOR(1,0))
print("0  1 |",XOR(0,1))
print("1  1 |",XOR(1,1))