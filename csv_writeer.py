import csv

with open('CSV_Demo.csv','w') as f:
    heading = ['Name','Age','ETC']

    writer = csv.writer(f)
    writer.writerow(heading)

with open('CSV_Demo.csv','a',newline='') as d:
    data = ['ajsdgajkhg',343,'ahsgdjshg']

    writer = csv.writer(d)
    writer.writerow(data)
    
print('Success')