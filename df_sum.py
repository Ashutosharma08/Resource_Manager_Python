import pandas as pd
import numpy as np
import csv
import psutil
import GPUtil
# df = pd.read_csv('Resource_Usage3.csv')
# print(df.head())
# df_sum = df['CPU Usage'].sum()
# print(df_sum)
# print(df.dtypes)


name_lst = []

for i in range(5):
    name = 'Process_'+str(i)+'_'+'.csv'
    name_lst.append(name)

for i in range(len(name_lst)):
    with open(name_lst[i],'w',newline='') as f:
        header = ['PID', 'Process Name', 'CPU Usage', 'GPU Usage', 'Memory Usage', 'IO_Usage', 'Timestamp']
        writer = csv.writer(f)
        writer.writerow(header)

