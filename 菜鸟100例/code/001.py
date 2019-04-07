# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


'''
range()
    python内置函数，创建一个整数列表
    函数语法
        range(start, stop[, step])

        参数说明
        1、start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
        2、stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        3、step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

逻辑运算符
    and     x and y
    or      x or y
    not     not x

'''
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (x != z) and (z != y):
                print(x, y, z)

