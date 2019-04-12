# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def reduceNumber(n):
    print(n, "=", end=" ")
    while n != 1:
        for i in range(2, n+1):
            # 判断i是否是n的一个因数
            if n % i == 0:
                # 如果是，就n = n // i
                n = n // i
                if n == 1:
                    print(i, end=" ")
                else:
                    print(i, "*", end=" ")
                break
num = int(input("请输入数字："))
reduceNumber(num)


