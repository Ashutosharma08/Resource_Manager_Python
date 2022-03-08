import psutil

process_iterator = psutil.process_iter()
prcs_lst = []
prcs_name = 'chrome.exe'
lst_id = []

for proc in process_iterator:
    lst_id.append([proc.name(),proc.pid])

for i in range(len(lst_id)):
    if prcs_name == lst_id[i][0]:
        prcs_lst.append(lst_id[i][1])

print(prcs_lst)

for l in range(lst_id):
    exec()