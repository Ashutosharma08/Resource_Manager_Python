import psutil
import time
import GPUtil
import csv
process_name = 'LiDAR360.exe'
name=psutil.Process(5412)

sleep_time= 2
mins = 60

with open('Resource_Usage.csv','w') as f:
    header = ['Process Name','CPU Usage','GPU Usage','Memory Usage']
    writer = csv.writer(f)
    writer.writerow(header)

for i in range(int((mins*60)/sleep_time)):

    cpu=name.cpu_percent(interval=2)/ psutil.cpu_count()
    name1=name.name()
    memory=name.memory_percent()

    print("Name % = " + str(name1))
    abc = GPUtil.showUtilization(useOldCode=True)
    print(abc)
    # print(GPUtil.showUtilization())
    print("CPU % = " + str(cpu))
    print("Memory % = " + str(memory))

    print("----------------------")
    lst = [name1,cpu,abc,memory]
    with open('Resource_Usage.csv','a',newline='') as d:
        writer = csv.writer(d)
        writer.writerow(lst)
        del lst # for creating list for new row entry
    time.sleep(sleep_time)
    

