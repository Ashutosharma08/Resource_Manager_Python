import psutil
import time
import GPUtil
import csv
import pandas as pd
# process_name = 'LiDAR360.exe'
name = psutil.Process(15500)
name_1 = psutil.Process(9996)
name_2 = psutil.Process(1476)
name_3 = psutil.Process(14976)

print(name.pid)
# print("Hello")
sleep_time = 2
mins = 60
# start = time.time()
with open('Resource_Usage3.csv', 'w') as f:
    header = ['PID','Process Name', 'CPU Usage', 'GPU Usage', 'Memory Usage','IO_Usage','Timestamp']
    writer = csv.writer(f)
    writer.writerow(header)

lst_name = [name,name_1,name_2,name_3]


def res_info(i):
    pid = i.pid
    cpu = i.cpu_percent(interval=2)/ psutil.cpu_count()
    name1 = i.name()
    memory = i.memory_percent()
    io = i.io_counters()
    gpu = GPUtil.showUtilization(useOldCode=True)

    return cpu,name1,memory,io,gpu,pid

for i in range(int(mins*60/sleep_time)):
    for j in range(len(lst_name)):
        count = 0
        cpu_total = 0
        cpu_usage, process_name, memory_usage, io_usage, gpu_usage,pid = res_info(lst_name[j])
        cpu_total =+cpu_usage
        lst_info = [pid,process_name, cpu_usage, gpu_usage, memory_usage, io_usage,time.time()]

        print("Process Name: " + str(process_name))
        print("CPU Usage: " + str(cpu_usage))
        print("memory_usage: " + str(memory_usage))
        print("IO Usage: " + str(io_usage))
        print("GPU Usage: " + str(gpu_usage))
        count =+ 1
        if count == 4:
            print("Total CPU: "+str(cpu_total))
        print("----------------------------")

#         with open('Resource_Usage3.csv', 'a', newline='') as d:
#             writer = csv.writer(d)
#             writer.writerow(lst_info)
#             # writer.writerow([])
#             if count == 4:
#                 cpu_total = 0
#                 count = 0
#
#             del lst_info
#         time.sleep(sleep_time)
#
# df = pd.read_csv('Resource_Usage3.csv')
#
# for i in range(4):
#     name = 'PID'+str(i)
#     df[name]=''
#
# for i in range(4):
#     if i == 1:
#         df['PID1'] = df.loc[df['PID']==df['PID'][0],'CPU Usage'].sum








# for i in range(int((mins * 60) / sleep_time)):
#     cpu = name.cpu_percent(interval=2) / psutil.cpu_count()
#     name1 = name.name()
#     memory = name.memory_percent()
#
#     print("Name % = " + str(name1))
#     abc = GPUtil.showUtilization(useOldCode=True)
#     print(abc)
#     # print(GPUtil.showUtilization())
#     print("CPU % = " + str(cpu))
#     print("Memory % = " + str(memory))
#
#     print("----------------------")
#     lst = [name1, cpu, abc, memory]
#     with open('Resource_Usage.csv', 'a', newline='') as d:
#         writer = csv.writer(d)
#         writer.writerow(lst)
#         del lst  # for creating list for new row entry
#     time.sleep(sleep_time)


