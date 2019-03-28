'''
迭代器与生成器
    迭代器
        1、迭代是python最强大的功能之一，是访问集合元素的一种方式
        2、迭代器是一个可以记住遍历的位置的对象
        3、迭代器对象从集合的第一个元素开始访问，直到所有的元素都被访问完结束。迭代器只能往前不会后退
        4、迭代器有两个基本的方法：iter() 和 next()。
        5、字符串，列表或元组对象都可用于创建迭代器
'''

# 迭代器
list = [1,2,3,4]
str = 'asdfgh'
itList = iter(list)
itStr = iter(str)
# print(itList)
# for i in itList:
#     print(i,end = "\t")


import  sys     #引入sys模块
while True:
    try:
        print(next(itStr),end = "\t")
    except StopIteration:
        sys.exit()


'''
创建一个迭代器
    1、把一个类作为迭代器使用需要在类中实现两个方法__iter__()和__init__()
    2、python的构造函数为__init__()
'''


