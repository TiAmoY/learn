'''
斐波那契数列
'''
a , b = 0 , 1
while b<10:
    print(b)
    a , b = b , a + b

# end关键字，可以将结果输出到同一行
a , b = 0 , 1
while b<10:
    print(b,end='\t')
    a , b = b , a + b