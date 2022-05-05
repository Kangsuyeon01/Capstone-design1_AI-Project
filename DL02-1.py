def AND(x1,x2):
    w1, w2, theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def NAND(x1,x2):
    w1, w2, theta = -0.5,-0.5,-0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1,x2):
    w1, w2, theta = 0.5,0.5,0.2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

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