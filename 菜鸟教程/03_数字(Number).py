'''
数字Number
    1、数据类型是不允许改变的，如果改变数字数据类型的值，将重新分配内存空间
    2、支持三种不同的数值类型
        1）整型(int)
        2）浮点型(float)
        3）复数(complex):由实数和虚数构成，复数的的实部和虚部都是浮点型
    3、我们可以使用十六进制和八进制来代表整数
'''

# 在变量赋值时Number对象将被创建
# var1 = 10
# var2 = 20

# 可以用del语句删除数据对象的引用
# print(var1)
# del var1,var2

# # 十六进制
# number = 0xA0F
# print(number)
#
# # 八进制
# number = 0o37
# print(number)

x = 10
print(int(x))
print(float(x))
print(complex(x))