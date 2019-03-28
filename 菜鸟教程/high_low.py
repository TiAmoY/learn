#该实例演示了数字猜谜游戏
import random

guess = random.randint(0,100)
print("数字猜谜游戏")
number = int(input("请输入数字："))
while number!=guess:
    if number < guess:
        print("猜小了！！！")
        number = int(input("请输入数字："))
    else:
        print("猜大了！！！")
        number = int(input("请输入数字："))
if number == guess:
    print("恭喜你，猜对了！！！")
