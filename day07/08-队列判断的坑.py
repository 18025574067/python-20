import multiprocessing

# 创建队列
queue = multiprocessing.Queue(3)

queue.put(1)
queue.put(1)
queue.put(1)

# 判断是否为空
isEmpty = queue.empty()
print("isEmpty-->", isEmpty)



