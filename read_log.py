# c2_pre.py DE_pre.py history.py feature.py lm_scan.py
import json
import sys
import time
import psutil
import threading

thread_flag = False

cout = open("monireadlog%s.txt" % sys.argv[1], "w")
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

hahaha = time.time()

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
import os;
inlist = os.listdir("./optc_unzip")


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

def filt_de(info):
    if info[2].startswith("202.120"): return True
    if info[2] == "10.10.39.76": return True
    if info[2].startswith("10.10.254"): return True
    return False
       

# general
date = sys.argv[1]
fin = open("./2019-09-%s/conn1.log" % date)
#fin = open("06%s.log" % date)


# for lm_scan
lm_win = sys.argv[2]
tflag = True
start = 0
length = int(86400/int(lm_win))
print(length)
slice = [{} for i in range(length)]
print(slice)
hs = ['80', '22', '21', '23', '3306', '443', '53', '445', '137', '8080', '8888', '139', '3389', '135', '1433', '1521']

# for de_trans
res_de = dict()

# for history
res = dict()

# for rdp abnormal
rdp = dict()

# for PHD
ave = dict()

# for T
tt = dict()

flag = 0

def reading(f):
    flag = 0
    tflag = True
    count = 0
    while True:
        #if count == 1000000: break
        line = f.readline()
        count += 1
        if not line: break
        if count <= 8: continue
        info = line.split()
        if len(info) <= 3: 
            print("oh")
            flag= 1
            continue

        if flag: print(line)

        # for PHD
        if info[9] == "-" or not inninn(info[2]): pass
        else:
            #ave_orig = float(info[9]) / float(info[16])
            #ave_resp = float(info[10]) / float(info[18])

            if info[2] not in ave:
                ave[info[2]] = [0,0,0,0]

            
            ave[info[2]][0] += 1
            if float(info[18]) > 20 * float(info[16]) and float(info[18]) > 200:
                ave[info[2]][1] += 1
            
            if float(info[16]) < 5 and float(info[18]) == 0 and float(info[18]) != 0:
                ave[info[2]][2] += 1
            
            if (float(info[9]) +  float(info[10])) / float(info[8]) < 12 and float(info[8]) > 120:
                ave[info[2]][3] += 1
        
        if count % 100000 == 0: print(count)

        
        # for yixin's report
        if info[5] == '3389' and inninn(info[2]):
            if flag: print("oooooowooweiowieoiwoeioweiowieoi")
            if info[2] not in rdp:
                rdp[info[2]] = [0,0]
            if info[11] == 'S0' or info[11] == "REJ":
                rdp[info[2]][1] += 1
            rdp[info[2]][0] += 1
            #rdp[info[2]].append([float(info[0]), info[11]])
        if count % 100000 == 0: print(count)

    #    if count % 100000 == 0: print(count)
    #    continue
        # for de_trans
        if not filt_de(info):
            if inninn(info[2]) and not inninn(info[4]):
                if info[2] not in res_de:
                    res_de[info[2]] = dict()
                    res_de[info[2]]['data'] = [0,0,0]
                    res_de[info[2]]['domain'] = set()
                if info[9] == '-': pass
                else: res_de[info[2]]['data'][0] += int(info[9])
                res_de[info[2]]['data'][1] += 1
                res_de[info[2]]['domain'].add(info[4])
        
        # for lm_scan
        if tflag:
            start = float(info[0])
            tflag = False
        
        index = int((float(info[0]) - start)/int(lm_win))
        if index > len(slice) - 1: continue

        if inninn(info[2]) and inninn(info[4]):
            try:
                if info[2] not in slice[index]:
                    slice[index][info[2]] = dict()
                    slice[index][info[2]]['s2'] = 0
                    slice[index][info[2]]['s3'] = 0
                    slice[index][info[2]]['total'] = 0
                    slice[index][info[2]]['dst'] = dict()
            except:
                print(line)
                continue

            slice[index][info[2]]['total'] += 1
            if info[5] not in slice[index][info[2]]['dst']:
                slice[index][info[2]]['dst'][info[5]] = 0
            slice[index][info[2]]['dst'][info[5]] += 1

            dport = info[5]
            weight = 0.1
            if dport in hs:
                weight = 1
            slice[index][info[2]]['s2'] += weight
        
        # for T:
        if inninn(info[2]):
            if info[2] not in tt:
                tt[info[2]] = dict()
            if info[4] not in tt[info[2]]:
                tt[info[2]][info[4]] = list()
            tt[info[2]][info[4]].append(float(info[0]))
            if info[4] == "132.197.158.98": print(info[4])
        # for cluster
        # Todo
        # for history
        if 1 == 1:
            if info[2] not in res:
                res[info[2]] = dict()
                res[info[2]]['traffic'] = 0
                res[info[2]]['domain'] = set()
                res[info[2]]['connection'] = 0
                res[info[2]]['single'] = 0
                res[info[2]]['shabi'] = 0
            else:
                if info[9] == "-":
                    pass
                else:
                    res[info[2]]['traffic'] += int(info[9])
                    res[info[2]]['traffic'] += int(info[10])
                            
                    if int(info[10]) != 0 and int(info[9]) / int(info[10]) > 20:
                        res[info[2]]['shabi'] += 1
                res[info[2]]['domain'].add(info[4])
                res[info[2]]['connection'] += 1
                if info[11] == "S0":
                    res[info[2]]['single'] += 1
                
        if 1 == 1:
            if info[4] not in res:
                res[info[4]] = dict()
                res[info[4]]['traffic'] = 0
                res[info[4]]['domain'] = set()
                res[info[4]]['connection'] = 0
                res[info[4]]['single'] = 0
                res[info[4]]['shabi'] = 0
            else:
                if info[9] == "-":
                    pass
                else:
                    res[info[4]]['traffic'] += int(info[9])
                    res[info[4]]['traffic'] += int(info[10])
                    if int(info[10]) != 0 and int(info[9]) / int(info[10]) > 20:
                        res[info[4]]['shabi'] += 1
                res[info[4]]['domain'].add(info[2])
                res[info[4]]['connection'] += 1
                if info[11] == "S0":
                    res[info[4]]['single'] += 1
        
        if count % 100000 == 0: print(count)
        #if count == 1000000: break
    
reading(fin)

#for file in inlist:
#    reading("./optc_unzip/%s" % file)

import math
for window in slice:
    print("ok")
    print(len(window))
    for ip in window:
        h = 0
        for dst in window[ip]['dst']:
            p = window[ip]['dst'][dst] / window[ip]['total']
            h -= (p * math.log(p))
        
        if len(window[ip]['dst']) == 1:
            window[ip]['s3'] = 0
        else:
            window[ip]['s3'] = h / math.log(len(window[ip]['dst']))
        window[ip]['dst'] = len(window[ip]['dst'])



for ip in res_de:
    res_de[ip]['data'][2] = len(res_de[ip]['domain'])
    res_de[ip]['domain'] = 'cleaned'
with open("./data_ex/data_ex_09%s" % date, "w") as f:
    json.dump(res_de,f)


for ip in res:
      res[ip]['domain'] = len(res[ip]['domain'])
#print(len(info))
with open("./historyc/history09%s.json" % (date),"w") as f:
      json.dump(res,f)


for i in range(length):
    f = open("./bothunter/09%s_%s.log" % (date, str(i)), "w")
    json.dump(slice[i], f)

with open("./rdp/rdp09%s.json" % date, "w") as f:
    json.dump(rdp, f)

with open("./C2C/tt09%s.json" % date, "w") as f:
    json.dump(tt, f)


with open("./phd/phd09%s.json" % date, "w") as f:
    json.dump(ave, f)

hahahaha = time.time() - hahaha

print(hahahaha)
thread_flag = True
print("ok")