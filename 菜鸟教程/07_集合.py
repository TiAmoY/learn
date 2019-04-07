'''
集合
    1、集合（set）是一个无序的不重复元素序列。
    2、可以使用大括号{ }或者 set( ) 函数创建，注意，创建一个空集合必须用set()
'''



print("=========---创建集合---=========")
# 创建格式
parame = {1, 2, 3, 4}
print(parame)
print(type(parame))

print("=========---集合的基本操作---=========")
# 添加元素
s = {1, 2, 3, 4, 5}
print(s)
s.add(6)
print(s)
s.update((567, 345))
print(s) # update添加元素参数可以是列表、元组、字典等

# 移除元素
s.remove(567)
print('移除567：', s)
# s.remove(567) 移除不存在的元素会报错

s.discard(567)  # 移除不存在的元素不会报错
print(s)

# 随机删除集合中的元素
# 在交互模式，pop是删除集合的第一个元素(排序后的集合的第一个元素)
s.pop()
print(s)

# 计算集合元素个数
print("集合元素个数：",len(s))

# 请空集合
s.clear()
print("请空集合：",s)

# 判断元素在集合中是否存在
s = {1,2,3,4,5}
print(1 in s)
print(7 in s)
print(1 not in s)

print("=========---集合的内置方法---=========")
# 集合的内置方法完整列表
s.add()
s.clear()
s.copy()
