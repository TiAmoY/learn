'''
元组
    元组与列表类似，不同之处在于元组的元素不能修改
    元组使用小括号，列表使用方括号
'''

# 创建元组
# 在括号中添加元素，并用逗号隔开
tup1 = ('Google','Runoob',1998,2000)
print(tup1)
print(type(tup1))
print("1==================")
# 创建空元组
tup2 = ();
# 元组中只包含一个元素的时候，需要在元素后面添加逗号，否则括号会被当做运算符使用
tup3 = (1,)
print(tup3)
print(type(tup3))
print(tup3[0])
print("2==================")

# 访问元组
# 元组可以通过下标索引来访问元组中的值
tup4 = (1,2,3,4,5,6,7)
print(tup4[0])
print(tup4[1:3])
print("3==================")

# 修改元组
# 元组中的值时不允许修改的，但我们可以对元组进行连接组合
tup5 = (1,2,3)
tup6 = ('a','v','s')
tup7 = tup5 + tup6
print(tup7)
# 以下修改元组元素是非法的
# tup5[2] = 4
# print(tup5)
print("4==================")

# 删除元组
# 元组中的元素是不允许删除的，但是我们可以使用del语句删除整个元组
tup8 = ('a','v','s')
print(tup8)
del(tup8)
# print(tup8)
print("5==================")

# 元组运算符
# 和列表相同

# 元组索引截取
# 与列表相同


# 元素内置函数
tup = (1,2,3,4,5,6)
list = [1,2,3,3]
print(len(tup))
print(max(tup))
print(min(tup))
print(tuple(list))
