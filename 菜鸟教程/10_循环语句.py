'''
循环语句
    while循环
        while 判断条件:
            语句
        在python中没有do...while循环

    for循环
        for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
            for <variable> in <sequence>:
                <statements>
            else:
                <statements>

'''
print("=======---for循环---=========")
# for循环
languages = ["C", "C++", "Perl", "Python"]
for language in languages:
    print(language)

print("=======---使用break跳出for循环---=========")
# 使用break跳出for循环
languages = ["C", "C++", "Perl", "Python"]
for language in languages:
    if language == "Perl":
        print("跳出循环")
        break
    print(language)


print("=======---range()函数---=========")
# range()函数
for x in range(5,9):
    print(x)
print("=======---range()函数---=========")
# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for x in range(5,9,2):
    print(x)


print("=======---range()函数---=========")
# 可以结合range()和len()函数以遍历一个序列的索引,如下所示
for i in range(len(languages)):
    print(i,"\t",languages[i])

print("=======---range()函数---=========")
# 创建函数列表
list(range(5))
print(list(range(5)))
print(type(list(range(5))))


'''
break和continue语句及循环语句中的else
    1、break可以跳出for循环和while循环
    2、如果从 for 或 while 循环中终止，任何对应的循环 else 块将不执行    
'''
print("=======---查询质数---=========")
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
'''
pass语句
    1、pass是空语句，是为了保持程序结构的完整性。
    2、pass 不做任何事情，一般用做占位语句
'''
print("=======---pass语句---=========")
while False:
    pass    # 等待键盘中断 (Ctrl+C)


print("=======---pass语句---=========")
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")