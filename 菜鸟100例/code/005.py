# 输入三个整数x,y,z，请把这三个数由小到大输出。

sort = []

for i in range(0, 3):
    x = int(input("int:"))
    sort.append(x)
for i in range(0, 3):
    for j in range(i, 3):
        if sort[i] > sort[j]:
            t = sort[i]
            sort[i] = sort[j]
            sort[j] = t
print(sort)