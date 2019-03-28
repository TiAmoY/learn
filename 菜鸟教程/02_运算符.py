'''
算术运算符
    +   -   *   /   %   //  **
比较（关系）运算符
    ==  !=  <   >   <=  >=
赋值运算符
    =   +=   -=   *=   /=   %=   //=  **=
逻辑运算符
    and     or     not
位运算符
    &   |   ^   ~   <<  >>
成员运算符
    in      not in
身份运算符
    is      is  not
运算符优先级
'''

# 逻辑运算符
# 只要值不为零，都是ture
# a = 10
# b = 20
# print(a and b)
# print(a or b)
# print(not b)
# print("---------------")
# a = 0
# print(a and b)
# print(a or b)
# print(not a)
# print("---------------")
# a = -1
# print(a and b)
# print(a or b)
# print(not a)


# # 位运算符
# a = 60
# b = 13
#
# # & 按位与：两个相应位都为1，则该结果为1，否则为0
# print(a & b)
#
# # | 按位或：只要有一个为1，结果就为1
# print(a | b)
#
# # 按位异或：两对应二进制位相异，结果为1
# print(a ^ b)
#
# # 按位取反
# print(~ a)
#
# # 左移动运算符:相当于乘2
# print(a << 2)
#
# #右移动运算符：相当于除2
# print(a >> 2)

# 身份运算符

a = 20
b = 10
print(a is b)
print(a is not b)