# 1、导入模块
import psutil
import datetime

# 2、定义变量保存CPU信息
cpu_per = psutil.cpu_percent(interval=0.5)

# 3、定义变量保存内存信息
momory_info = psutil.virtual_memory()

# 4、定义变量保存硬盘信息
disk_info = psutil.disk_usage("/")

# 5、定义变量保存网络收发量
net_info = psutil.net_io_counters()

# 获取系统当前时间
current_time = datetime.datetime.now().strftime("%F %T")

# 6、拼接字符串显示
log_str = "|---------------------|-----------------|-----------------|-------------------|-----------------------|\n"
log_str += "|       监控时间       |     CPU使用率    |    内存使用率    |     硬盘使用率     |        网络收发量      |\n"
log_str += "|                     |      共%d核CPU    |   总计%.2fG内存  |   总计%.2fG硬盘  |                      |\n" % (psutil.cpu_count(logical=False), momory_info.total/1024/1024/1024, disk_info.total/1024/1024/1024)
log_str += "|---------------------|-----------------|-----------------|-------------------|-----------------------|\n"
log_str += "| %s |      %s%%      |      %s%%      |       %s%%       |     收：%.fMb/发：%.fMb   |\n" % (current_time, cpu_per, momory_info.percent, disk_info.percent, net_info.bytes_recv/1024/1024, net_info.bytes_sent/1024/1024)
log_str += "|---------------------|-----------------|-----------------|-------------------|-----------------------|\n"
print(log_str)

# 7、保存监控信息到日志文件
f = open("./log.txt", "a")
f.write(log_str + "\n\n")
f.close()



