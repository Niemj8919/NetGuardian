import json
import time
import psutil
import threading
import sys
thread_flag = False
cout = open("monidfs%s.txt" % sys.argv[1], "w")
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
f = open("./2019-09-25/conn1.log")
#f = open("06%s.log" % sys.argv[1])
import os
inlist = os.listdir("./optc25")
#inlist = []
#f = open("23Sep19-red##AIA-1-25.ecar-last.json.gz.log")
res = dict()
times = dict()

count = 0
while True:
    
    line = f.readline()
    count += 1
    if not line: break
    if count <= 8:
        continue

    info = line.split()
    if len(info) <= 3:
        print("oh")
        continue
        
    if info[2] not in res:
        res[info[2]] = dict()
        res[info[2]]['flag'] = 0
    if info[4] not in res[info[2]]:
        res[info[2]][info[4]] = 1


    if info[2] not in times:
        times[info[2]] = dict()
    if info[4] not in times[info[2]]:
        times[info[2]][info[4]] = list()
    #ts1 = info[6].split("T")[2]
    #ttemp = info[6].split("T")[1].split("-")[2].split(".")
    #min = ttemp[2]
    #timeA = time.strptime(ts1 + " " + min, "%Y-%m-%d %H:%M:%S")
                                
    #if len(ttemp) == 2: ts = time.mktime(timeA) + int(ttemp[1]) / 100
    #else: ts = time.mktime(timeA)
        #print(ts)
    times[info[2]][info[4]].append(float(info[0]))

    
        
    if count % 100000 == 0:
        print(count)
        #if count == 1000000:
        #    break



for file in inlist:
    f = open("./optc25/%s" % file)
    count = 0
    print(file)
    while True:
        line = f.readline()
        count += 1
        if not line: break
        if count <= 8:
            continue

        info = line.split()
        if len(info) <= 3:
            print("oh")
            continue
        
        if info[0] not in res:
            res[info[0]] = dict()
            res[info[0]]['flag'] = 0
        if info[2] not in res[info[0]]:
            res[info[0]][info[2]] = 1


        if info[0] not in times:
            times[info[0]] = dict()
        if info[2] not in times[info[0]]:
            times[info[0]][info[2]] = list()

        
        ts1 = info[6].split("T")[0]
        ttemp = info[6].split("T")[1].split("-")[0].split(".")
        min = ttemp[0]
        timeA = time.strptime(ts1 + " " + min, "%Y-%m-%d %H:%M:%S")
                                
        if len(ttemp) == 2: ts = time.mktime(timeA) + int(ttemp[1]) / 100
        else: ts = time.mktime(timeA)
        #print(ts)
        times[info[0]][info[2]].append(ts)
        
    
        
        if count % 100000 == 0:
            print(count)
        #if count == 1000000:
        #    break

try: os.system("mkdir 09%s" % sys.argv[1])
except: 
    print("ok")
    pass

for ip in times:
    f = open("./09%s/%s.json" % (sys.argv[1],ip), "w")
    for d in times[ip]:
        times[ip][d].sort()
    json.dump(times[ip], f)

print(len(res))
with open("dfs09%s.json" % sys.argv[1],"w") as f:
    json.dump(res, f)

print(time.time() - haha)
thread_flag = True