'''
条件控制
'''

# if语句
'''
if语句形式如下
    if condition_1:
        statement_block_1
    elif condition_2:
        statement_block_2
    else:
        statement_block_3
        
注：
    Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
    1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
    2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
    3、在Python中没有switch – case语句。
'''

#实例
# var = 100
# if var:
#     print("ture")
#     print(var)
# var = 0
# if var:
#     print("ture")
#     print(var)
# else:
#     print("false")
#     print(var)

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")