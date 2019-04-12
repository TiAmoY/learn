# 判断101-200之间有多少个素数，并输出所有素数。

import math

# flag用来标记是否为素数
flag = True
for num in range(101, 201):
    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        print(num)
    flag = True
