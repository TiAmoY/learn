# 暂停一秒输出。
# 一秒输出一行乘法表
# time模块的sleep()函数

import time

for x in range(1, 10):
    for y in range(1, x+1):
        print(y, "*", x, "=", (x*y), end="\t")
    print()
    time.sleep(1) # 暂停一秒