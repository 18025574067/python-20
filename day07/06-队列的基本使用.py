"""
队列是 multiprocessing 模块提供的一个类

1）创建队列
2）放值
3）取值

"""
import multiprocessing


# 1）创建队列
# multiprocessing.Queue(n), n代表队列长度
queue = multiprocessing.Queue(5)

# 2）放值
queue.put(1)     # 放入1
queue.put("hello")
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({"a": 10, "b": 100})

# 队列长度为5, 放入第6 个数据，默认会进行了阻塞状态，等待队列先取出值再放入新值
# queue.put(10)
# put_nowait()表示放入值，如果己满，不再等待，直接报错
# queue.put_nowait(100)

# 3）取值
value = queue.get()
print(value)
print("==" * 20)

value = queue.get()
print(value)
print("==" * 20)

value = queue.get()
print(value)
print("==" * 20)

value = queue.get()
print(value)
print("==" * 20)

value = queue.get()
print(value)
print("==" * 20)

# ---------- 队列己空 -------------
# 当队列己空，再取值，会进入阻塞状态，等待放入值，再取值
# value = queue.get()
# print(value)
# print("==" * 20)

# get_nowait(), 当队列为空的时候，不再等待放入新的值，直接报错
# value = queue.get_nowait()
# print(value)
# print("==" * 20)

