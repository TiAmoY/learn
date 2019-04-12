# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
'''
分析
    月份      兔子数量
    1           1对
    2           1对
    3           2对(一对生的一对原来的)
    4           3对(一对4月生的，一对3月生的，一对原本就有的)
    5           5对
    ...         ...
    在大于2月时，每个月兔子的数量是前两个月之和
    相当于斐波那契数列
'''

def rabbit(month):
    if month == 1 or month == 2:
        return 1
    rabbits = [1, 1]
    for num in range(2, month):
        print(num)
        rabbits.append(rabbits[-1]+rabbits[-2])
    return rabbits[rabbits.__len__()-1]

print(rabbit(10), "对兔子")

