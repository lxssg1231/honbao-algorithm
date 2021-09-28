import random


def honbao(money, num):
    L = []
    for i in range(0, num):
        if i == (num - 1):
            j = round(money,2)
            L.append(j)
            break
        else:
            j = round(random.uniform(0.01, 2 * money / (num - i)), 2)
            money -= j
            L.append(j)
    return L


money = float(input('请输入红包金额：'))
num = int(input('请输入红包数量：'))
l = honbao(money, num)
print(l)
