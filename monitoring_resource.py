import psutil
# import wmi


process_iterator = psutil.process_iter()
prcs_lst = []

for proc in process_iterator:
        prcs_lst.append([proc.name(), proc.pid])

# for i in range(len(prcs_lst)):
#     print(prcs_lst[i])
lidar_idx=prcs_lst.index('LiDAR360.exe')
print(lidar_idx)
# prcs_lst[lidar_idx].cpu_percent()

