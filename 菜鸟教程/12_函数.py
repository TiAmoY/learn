'''
函数
    函数是组织好的，可重复使用的，用来实现单一，或相关联动功能的代码段

    一、定义一个函数
        1、函数代码块以 def 开头，后接函数标识符名称和()
        2、任何传入参数和自变量必须放在圆括号中间，圆括号中间可以用于定义参数
        3、函数的第一行语句可以选择性的使用文档字符串----用于存放函数说明
        4、函数内容以冒号起始，并且缩进
        5、return [表达式] 结束函数，选择性的返回一个值，给调用方，不带表达式的return相当于返回None

        语法：
            def 函数名(参数列表):
                函数体

        匿名函数

        变量作用域（4种）
            L(local) 局部作用域
            E(Enclosing)    闭包函数外的函数中
            G(Global)   全局作用域
            B(Built-in) 内置作用域（内置函数坐在模块的范围内）
'''

# 用函数输出hello world
print("----------函数输出hello world----------")
def hello():
    print("hello world")

hello()

# 计算长方形面积函数
print("----------计算长方形面积----------")
def area(width,height):
    return width*height
w = 4
h = 5
print(area(w,h))

'''
函数调用
    定义一个函数，给了函数一个名称，指定了函数里面包含的参数，和代码块结构
    可以通过另一个函数调用执行，也可以直接从python命令提示符执行
'''

print("--------函数调用--------")
def printme(str):
    print(str)

printme("调用了printme函数")


'''
参数传递
    类型属于对象，变量是没有类型的
    
    可更改与不可更改对象
        在python中，strings、tuples和numbers是不可更改的对象，而list，dict等是可以修改的对象。
        不可变类型：变量a = 5之后再赋值 a = 10，这里实际上是新生成一个个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
        可变类型：
'''

print("--------不可变对象实例--------")

def ChangeInt(a):
    a = 10;

a = 5
ChangeInt(a)
print(a)

'''
函数参数类型
    必须参数
        必须参数须以正确的顺序传入函数，调用时的数量必须和声明时的一样
        调用函数时，必须传入一个参数，不然会出现语法错误
    关键字参数
        函数调用使用关键字参数来决定传入的参数值，
        使用关键字参数允许函数调用时参数的顺序与声明时不一致
    默认参数
        调用函数时，如果没有传递参数，则会使用默认值，
    不定长参数
        一个函数可以处理比当初声明时更多的参数。这些参数叫做不定长参数。
        *vartuple 相当于空元组
        **var_args_dict 相当于空字典
        
'''

#必须参数
print("--------------必须参数实例------------")
# def a(str):
#     print(str)
#     return
# a()     #在调用函数的时候，没有给定参数，会报错

# 关键字参数
print("--------------关键字参数实例------------")

def a(name,age):
    print("name:",name)
    print("age:",age)
    return
a(age=23,name="wang")

# 默认参数
print("--------------默认参数实例------------")
def a(name,age=25):
    print("name:",name)
    print("age:",age)
    return
a(name="wang")
a(name="wang",age=35)


# 不定长参数

print("--------------不定长参数实例------------")

def a(arg1,*vartuple):
    print("arg1:",arg1)
    print("vartuple:",vartuple)
    return
a(1,2,3,4,5)


'''
匿名函数
    语法：lambda[arg1,...]:expression
'''

