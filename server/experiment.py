import time


# 定义消费者模型
def consumer():
    while True:
        y = yield
        time.sleep(1)  # 一秒后处理数据
        print("处理了数据", y)


# 定义生产者模型
def producer():
    con = consumer()  # 拿到消费者对象，并且激活使用
    next(con)
    for i in range(10):
        time.sleep(1)
        print("发送数据", i)
        con.send(i)


producer()  # 直接调用生产者模型
