# 暂停一秒输出，并格式化当前时间。
# 格式化时间

'''
捎带一点点time模块的知识
    time模块所包含的函数能够实现以下功能：
        获得当前时间
        操作时间和日期
        从字符串读取时间
        格式化时间为字符串
    time中重要的函数
            函数                      描述
        asctime([tuple])            将时间元组转换为字符串
        localtime()                 将秒数转换为日期元组，以本地时间为准
        mktime(tuple)               将时间元组转换为本地时间
        sleep(secs)                 休眠(不做任何事情)secs秒
        strptime(string[.format])   将字符串解析为时间元组
        time()                      当前时间
'''
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


