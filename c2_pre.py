import sys

import csv

import time
import threading
import psutil
thread_flag = False

cout = open("monic2pre%s.txt" % sys.argv[1], "w")
def gather(pid):
    global thread_flag
    p = psutil.Process(pid)

    while True:
        cpu_percent = p.cpu_percent(interval=5)
        
        #cpu_percent2 = psutil.cpu_percent(interval=5)  # 采样时间5秒 第二种方法
        mem_info = psutil.Process().memory_info()
        mem_percent = mem_info.rss
        
            # 打印数据
        print(
            f"CPU使用率 {cpu_percent}% 内存使用 {mem_percent} Bytes")
        
        cout.write(
            f"CPU使用率 {cpu_percent}% 内存使用 {mem_percent} Bytes" + "\n")
        
        if thread_flag: break
        import time 
        time.sleep(1)

cpu_process = psutil.Process()
pid = cpu_process.pid
print(pid)
Threader = threading.Thread(target=gather, args = (pid,))
Threader.start()






haha = time.time()
top_d = dict()

crypto = dict()
mining = dict()

with open("crypto.txt") as f:
    while True:
        line = f.readline().rstrip()
        if not line: break
        crypto[line] = 1



with open("top-1m.csv") as f:
    reader = csv.reader(f)
    
    for row in reader:
        top_d[row[1]] = 1

print(len(top_d))
           
'''
def inninn(node):
    if node.startswith("202.120"):
                return 1
    elif node.startswith("192.168"):
                return 1
    elif node.startswith("10."):
                return 1 
    elif node.startswith("172"):
        if int(node.split(".")[1]) >=16 and int(node.split(".")[1]) <=31:
                    return 1
        else: return 0
    else:
                return 0
'''
def inninn(node):
    if node.startswith("202.120"):
                return 1
    elif node.startswith("192.168"):
                return 1
    elif node.startswith("10."):
                return 1 
    elif node.startswith("172"):
        if int(node.split(".")[1]) >=16 and int(node.split(".")[1]) <=31:
                    return 1
        else: return 0
    else:
                return 0

date = sys.argv[1]

f = open("./2019-09-%s/dns1.log" % date)
#f = open("dns06%s.log" % date)
count = 0
countr = 0
kl = dict()

nxdomain = dict()

spike = dict()
temp = dict()


while True:
    line = f.readline()
    count += 1
    if count <= 8: continue
    if not line: break
    info = line.split()

    if len(info) <= 3:
        continue

    
    if not inninn(info[2]): continue
    if info[2].startswith('202.120'): continue
    
    # yixin's report
    if info[14] == '3' or info[15] == "NXDOMAIN":
        if info[2] not in nxdomain:
            nxdomain[info[2]] = 0
        nxdomain[info[2]] += 1

    sld = '.'.join(info[9].split('.')[-2:])

    if sld in crypto: 
        if info[2] not in mining:
            mining[info[2]] = 0
        mining[info[2]] += 1

    if ".local" in info[9]: continue
    if '.' not in info[9]: continue
    if 'usst.edu.cn' in info[9]: continue
    if info[9].endswith(".arpa"): continue

    
    #print(sld)
    if sld == "com.cn":
        sld = '.'.join(info[9].split('.')[-3:])
    if sld in top_d: continue
    

    countr += 1
    
    name =  info[2]

    if name not in kl:
        kl[name] = dict()
    if info[9] not in kl[name]:
        kl[name][info[9]] = set()
    kl[name][info[9]].add(float(info[0]))

    if countr % 100000 == 0: 
        print(countr)

print(len(kl))

for name in kl:
    for domain in kl[name]:
            kl[name][domain] = list(kl[name][domain])

import json

with open("./C2C/c2_09%s.json" % date, "w") as fout:
    json.dump(kl, fout)

with open("./yixin/nxdomain_09%s.json" % date, "w") as fout:
    json.dump(nxdomain, fout)

with open("./yixin/mining_09%s.json" % date, "w") as fout:
    json.dump(mining, fout)

print(time.time() - haha)
thread_flag = True