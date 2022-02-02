# 1、导入psutil模块
import psutil

# 2、获取CPU信息
# 2.1 获取CPU核心数
print(psutil.cpu_count())
# 获取CPU物理核心数
print(psutil.cpu_count(logical=False))
# 2.2 CPU使用率
print(psutil.cpu_percent(interval=0.5))
# CPU每个核心的使用率
print(psutil.cpu_percent(interval=0.5, percpu=True))

# 3、获取内存信息
# 3.1 获取内存的整体信息
print(psutil.virtual_memory())
# 3.2 内存的使用率
print(psutil.virtual_memory().percent)

# 4、获取硬盘信息
# 4.1 获取硬盘的分区信息
print(psutil.disk_partitions())
# 4.2 获取指定磁盘信息
print(psutil.disk_usage("/"))
# 4.3 硬盘的使用率
print(psutil.disk_usage("/").percent)

# 5、获取网络信息
# 5.1 获取收到的数据包数量
print(psutil.net_io_counters().bytes_recv/1024/1024)
# 5.2 获取发送的数据包数量
print(psutil.net_io_counters().bytes_sent/1024/1024)

# 6、获取开机时间
print(psutil.boot_time())
