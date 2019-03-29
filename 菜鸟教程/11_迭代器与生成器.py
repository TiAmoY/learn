'''
迭代器与生成器
    迭代器
        1、迭代是python最强大的功能之一，是访问集合元素的一种方式
        2、迭代器是一个可以记住遍历的位置的对象
        3、迭代器对象从集合的第一个元素开始访问，直到所有的元素都被访问完结束。迭代器只能往前不会后退
        4、迭代器有两个基本的方法：iter() 和 next()。
        5、字符串，列表或元组对象都可用于创建迭代器
StopIteration异常
生成器
'''

# 迭代器
# list = [1,2,3,4]
# str = 'asdfgh'
# itList = iter(list)
# itStr = iter(str)
# print(itList)
# for i in itList:
#     print(i,end = "\t")


# import  sys     #引入sys模块
# while True:
#     try:
#         print(next(itStr),end = "\t")
#     except StopIteration:
#         sys.exit()


'''
创建一个迭代器
    1、把一个类作为迭代器使用需要在类中实现两个方法__iter__()和__init__()
    2、python的构造函数为__init__(),他会在对象初始化的时候执行
    3、__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 
       方法并通过 StopIteration 异常标识迭代的完成。
    4、__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
    
'''
print("------创建迭代器-------")
# 定义类MyNumber
class MyNumbers:
    # 实现 __iter__()方法
    def __iter__(self):
        self.a = 1
        return self
    # 实现__next__()方法
    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = MyNumbers()
myiter = iter(myClass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(type(myClass))
print(type(myiter))


'''
StopIteration异常
    用于标识迭代的完成，防止出现无限死循环的情况，在__next__()方法中，可以设置在完成指定循环次数后触发
StopIteration异常来结束迭代
'''
print("-------StopIteration异常-------")
class MyNumbers:
    # 实现 __iter__()方法
    def __iter__(self):
        self.a = 1
        return self
    # 实现__next__()方法
    def __next__(self):
        if self.a < 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myClass = MyNumbers()
myiter = iter(myClass)
for x in myiter:
    print(x,end = "\t")


'''
生成器
    使用yield的函数被称为生成器(generator)
    生成器是一个返回迭代器的函数，只能用于迭代操作，生成器就是一个迭代器。
    在调用生成器运行的过程中，每次遇到yield时，函数会暂停并保存当前所有的运行信息，返回yield的值，
并在下一次执行next()方法时从当前位置继续运行
    调用一个生成器函数，返回的是迭代器    
'''

print()
print("--------生成器--斐波那契数列---------")
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
            return
        yield a
        a,b = b,a+b
        counter += 1

f = fibonacci(10)
print(f)
for x in f:
    print(x, end = "\t")


