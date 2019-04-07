# 输入某年某月某日，判断这一天是这一年的第几天？
import sys

day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))
sum = 0
if 0 < month < 13:
    sum = days[month-1]
else:
    print("输入的日期不对")

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) and (month == 2):
    if day > day_of_month[month - 1] + 1:
        print("该月最多有29天")
        sys.exit()
else:
    if day > day_of_month[month - 1]:
        print("该月最多有", day_of_month[month-1], "天")
        sys.exit()

if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) and (month > 2):
    sum = sum + day + 1
    print(year, "的第" , sum, "天")
else:
    sum = sum + day
    print(year, "的第", sum, "天")

