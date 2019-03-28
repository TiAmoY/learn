    # print("你好，世界")
'''
    标准数据类型
        Number（数字），String（字符串），List（列表），Tuple（元组），Set（集合），Dictionary（字典）
        不可变数据：Number、String、Tuple
        可变数据：List、Set、Dictionary
'''

#Number（数字）
#int、float、bool、complex
    # a,b,c,d = 20,5.5,True,4+3j
    # print(type(a),type(b),type(c),type(d))
    # print("================================")
    # a = 111
    # print(isinstance(a,int))
    # print("================================")
'''
isinstance()和type()的区别
    1、type()不会认为子类是一种父类类型
    2、isinstance()会认为子类是一种父类类型
'''
    # class A:
    #     pass
    # class B(A):
    #     pass
    # print(isinstance(A(),A))
    # print(isinstance(B(),A))
    # print(type(B()) == A)
    # print("================================")

'''
String(字符串)
    字符串用单引号或双引号括起来，同时使用\转义特殊字符
    1、字符串截取的语法格式
        变量[头下标:尾下标]
    2、+ 字符串的连接符
       * 复制当前字符串，紧跟的数字为复制的次数
'''
# str = 'wangh'
#
# print(str)      #输出字符串
# print(str[1:3]) #输出下标1-3
# print(str[0])   #输出下标为0的字符
# print(str[1:])  #输出下标为1之后的所有字符
# print(str * 2)  #输出字符串两次
# print(str + 'test') #连接字符串

'''
List()列表
    是python中使用最频繁的数据类型
    列表是写在[]之间，用逗号分隔开的元素列表
    1、+ 是列表连接运算符
    2、* 是重复操作
    列表中的元素可以改变
'''
# list = ['abc',678,123,234,56]
# print(list)
# print(list[0])
# print(list[0:2])
# list[0] = 12
# print(list)

'''
Tuple(元组)
    1、元组与列表相似，不同之处在于元组的元素不能修改，元组写在()里，元素之间用逗号隔开
    2、可以把字符串看成一种特殊的元组
    3、元组的元素不可变，但是可以包含可变的对象，比如list列表
'''

'''
Set(集合)
    1、集合是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或者是成员
    2、基本功能是进行成员关系测试和删除重复元素
    3、可以用{ }或者set()函数来创建集合  注：创建空集合必须用set()
'''
# student = {'tom','jim','mary','tom','jack','rose'}
# print(student)
#
# #成员测试
# if 'rose' in student:
#     print("rose在集合中")
# else:
#     print("rose不在集合中")
#
# #set可以进行集合运算
# a = set('zxcvbn')
# b = set('asdfgzxc')
#
# print(a - b)    #差集
# print(a | b)    #并集
# print(a & b)    #交集
# print(a ^ b)    #a和b中不同时存在的元素

'''
Dictionary(字典)
    1、列表是有序的对象集合，字典是无序的对象集合，字典中的元素通过键来存取
    2、字典是一种映射类型，用{ }标识，是一个无序的 键(key):值(value)的集合
    3、键必须使用不可改变类型
    4、在同一个字典，键必须是唯一的
'''
# dict = { }
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟教程"
tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}
#
# print(dict['one'])
# print(dict[2])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())

print({x : x**2 for x in (2,4,6)})

print(dict([('Runoob',1),('Google',2)]))
print(tinydict.clear())