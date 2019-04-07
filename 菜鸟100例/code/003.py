# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

num = 168
for i in range(1, 85):
    if num % i == 0:
        j = num / i
        if j > i and(j - i) % 2 == 0 and (j + i) % 2 == 0:
            n = (j - i) / 2
            x = n * n - 100
            print(x)