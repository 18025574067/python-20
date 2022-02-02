"""
1、判断队列是否已满
2、判断队列是否为空
3、取出队列中消息的个数

"""
import multiprocessing


# 创建一个长度为 3 的队列
queue = multiprocessing.Queue(3)

queue.put(1)
queue.put(2)
queue.put(3)

value = queue.get()

# 1、判断队列是否已满
# queue.full() 判断队列是否为满，如果是True= 满，如果是False= 未满
isFull = queue.full()
print("is_full-->", isFull)

value = queue.get()
# 3、取出队列中消息的个数
print("消息的个数：", queue.qsize())

value = queue.get()
# 2、判断队列是否为空
# queue.empty() 判断队列是否为空，如果是True= 空，如果是False= 未空
isEmpty = queue.empty()
print("isEmpty-->", isEmpty)


