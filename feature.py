import json
import sys
date = int(sys.argv[1])
window = int(sys.argv[2])

import time
import threading
import psutil


thread_flag = False
cout = open("monifeature%s.txt" % sys.argv[1], "w")
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
#with open("impo%s.json" % date) as f:
#     res = json.load(f)

res = dict()

def inninn(node):
    if node.startswith("142.20"):
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


def addkey(ip):
    global res
    res[ip] = dict()
    res[ip]["dlist"] = set()
    res[ip]['data'] = 0
    res[ip]['temp'] = 0
    res[ip]['domain'] = 0
    
    res[ip]['btemp'] = 0
    res[ip]['burst'] = 0

    res[ip]['dtemp'] = 0
    res[ip]['dburst'] = 0
    
    res[ip]['http'] = set()
    res[ip]['ua'] = False
    
    res[ip]['flag'] = False
    res[ip]['dflag'] = False




data = 0
start = 0

flow = list()
dflow = list()

f = open("./2019-09-%s/conn1.log" % date)
#f = open("06%s.log" % date)
count = 0
while True:
            line = f.readline()
            count += 1
            if count <= 8:
                continue
            if count % 100000 == 0:
                print(count)
            #if count == 1000000:
            #     break

            if not line:
                break
            info = line.split()
            if len(info) < 3:
                print("oh")
                continue
            stamp = float(info[0])
            
            if stamp - start > 60:
                start = stamp
                for ip in res:
                    flow.append(res[ip]['temp'])
                    dflow.append(len(res[ip]['dlist']))
                    if res[ip]['temp'] > 9138:
                        res[ip]['data'] += 1
                        res[ip]['flag'] = True
                        res[ip]['btemp'] += 1
                    
                    if len(res[ip]['dlist']) > 10:   
                        res[ip]['domain'] += 1
                        res[ip]['dflag'] = True
                        res[ip]['dtemp'] += 1

                    if res[ip]['temp'] < 9138 and res[ip]['flag']:
                        res[ip]['flag'] = False
                        if res[ip]['btemp'] > res[ip]['burst']:
                            res[ip]['burst'] = res[ip]['btemp']
                        res[ip]['btemp'] = 0
                    
                    if res[ip]['temp'] < 10 and res[ip]['dflag']:
                        res[ip]['flag'] = False
                        if res[ip]['dtemp'] > res[ip]['dburst']:
                            res[ip]['dburst'] = res[ip]['dtemp']
                        res[ip]['dtemp'] = 0
                    
                    '''
                    if res[ip]['data'] < res[ip]['temp']:
                        res[ip]['data'] = res[ip]['temp']
                        res[ip]['flag'] = True

                    if len(res[ip]['dlist']) > res[ip]['domain']:
                        res[ip]['domain'] = len(res[ip]['dlist'])
                        res[ip]['dflag'] = True
                    
                    if res[ip]['flag']:
                        if 0.75 * res[ip]['data'] < res[ip]['temp']:
                            res[ip]['btemp'] += 1
                        else:
                            res[ip]['dflag'] = False

                            if res[ip]['btemp'] > res[ip]['burst']:
                                res[ip]['burst'] = res[ip]['btemp']
                                res[ip]['btemp'] = 0
                    
                    if res[ip]['dflag']:
                        
                        if 0.75 * res[ip]['domain'] < len(res[ip]['dlist']):
                            res[ip]['btemp'] += 1
                        else:
                            res[ip]['dflag'] = False
                            if res[ip]['dtemp'] > res[ip]['dburst']:
                                res[ip]['dburst'] = res[ip]['dtemp']
                                print(res[ip]['dburst'])
                                res[ip]['dtemp'] = 0
                    '''
                
                for ip in res:
                    res[ip]['dlist'] = set()
                    res[ip]['temp'] = 0

            if info[9] == '-' or info[10] == '-': continue
            sum = int(info[9]) + int(info[10])

            if inninn(info[2]):
                if info[2] not in res:
                    addkey(info[2])
                res[info[2]]['temp'] += sum
                res[info[2]]['dlist'].add(info[4])
            elif inninn(info[4]):
                if info[4] not in res:
                    addkey(info[4])
                res[info[4]]['temp'] += sum
                res[info[4]]['dlist'].add(info[2])
            

import math

print(len(flow))
print(len(dflow))
flow.sort()
dflow.sort()

result = dict()
result['a'] = flow
result['b'] = dflow

with open("list%s.json" % date, "w") as fout:
    json.dump(result,fout)
print(flow[math.ceil(0.95 * len(flow))])
print(dflow[math.ceil(0.95 * len(dflow))])
print(dflow[-1])



print("http")
count = 0

#for name in t_file:
for i in range(date - window, date):
    if i < 10:
        str_i = '0' + str(i)
    else:
        str_i = str(i)
    f = open('./http06%s.log' % str_i)
    #f = open("./0500s/http%s.log" % name)
    while True:
        line = f.readline()
        count += 1
        if count <= 8:
            continue
        #if count % 100000 == 0:
        #    print(count)
                #if count == 10000000:
                #     break

        if not line:
            break
        info = line.split()
        if len(info) < 3:
            print("oh")
            continue
        if info[2] in res:
            res[info[2]]['http'].add(info[12])


count = 0
print("user_agent")
f = open("./2019-09-%s/http1.log" % date) 
#f = open("http06%s.log" % date)
while True:
    line = f.readline()
    count += 1
    if count <= 8:
        continue
    if count % 100000 == 0:
        print(count)
    #if count == 1000000:
    #     break

    if not line:
        break
    info = line.split()
    if len(info) < 3:
        print("oh")
        continue
    if info[2] in res:
        if info[12] not in res[info[2]]['http']:
            res[info[2]]['ua'] = True


cc = 0
for ip in res:
    res[ip]['dlist'] = 'Beta'
    res[ip]['http'] = list(res[ip]['http'])
    if res[ip]['dburst'] != 0:
        cc += 1
print(cc)
with open("impo09%s.json" % date,"w") as f:
    json.dump(res, f)



thread_flag = True
print(time.time() - haha)

            
