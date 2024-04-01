import sys
import json
import random
import time
fgt = open(sys.argv[5])
gt = json.load(fgt)
steps = gt['steps']['lecdpk']['steps']
t = list()
for step in steps:
    ts = step['run']
    ri = ts.split("T")[0]
    miao = ts.split("T")[1][:-1]
    
    timeA = time.strptime(ri + " " + miao, "%Y-%m-%d %H:%M:%S")
    ts = time.mktime(timeA) + 28800
    t.append(ts)

t[0] -= 90
t[len(t) - 1] += 90
print(len(t))

# 1687535980 1687622390

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

start = sys.argv[3]
end = sys.argv[4]

fhttp = open("./http06%s.log" % start)


#finhttp = open("./menupass9/http.log")

ddddd = list()
for i in range(int(start), int(end)+1):
    if i < 10:
        f = open("./0500s/050%s.log" % str(i))
    else:
        f = open("./06%s.log" % str(i))
    count = 0
    while True:
            line = f.readline()
            count += 1
            if count <= 8:
                continue
            info = float(line.split()[0])
            ddddd.append(info)
            break

print(ddddd)
def random_(time, thr, m):
    temp = set()
    for i in range(len(ddddd)):
        if time > ddddd[i]:
            set_date = i + int(start)
            
        else:
            #print(set_date)
            break
    f = open("./0500s/filt_05%s.log" % set_date)
    while True:
                line = f.readline()
                count += 1
                if count <= 8:
                    continue
                if count % 1000000 == 0:
                    print(count)

                if not line:
                    break
                info = line.split()
                #if float(info[0]) < time - thr:
                #    continue
                #if float(info[0]) > time + thr:
                #    break
                #    continue
                if m == 1:
                    if info[2] in inner_ip:
                        temp.add(info[2])
                    if info[4] in inner_ip:
                        temp.add(info[4])
                elif m == 0:
                    temp.add(info[2])
                    temp.add(info[4])

    return temp


#1687535990 1687622390

def Insert(T_insert, src,d,flow):
    for i in range(len(ddddd)):
        if T_insert > ddddd[i]:
            insert_date = i + int(start)
        else:
            break
    info = flow.split()
    info[0] = str(T_insert)
    info[2] = src
    info[4] = d
    print(info)
    flow = " ".join(info)
    f = open("./06%s.log" % insert_date,"a")
    f.write(flow)
    print(insert_date)
    print(flow)

def randindex(list):
    a = random.randint(0, len(list) - 1)
    return list[a]

def gain(t1,t2,src):
    for i in range(len(ddddd)):
        if t1 > ddddd[i]:
            date1 = i + int(start)
        else:
            break
    for i in range(len(ddddd)):
        if t2 > ddddd[i]:
            date2 = i + int(start)
        else:
            break
    res = set()
    for j in range(date1, date2 + 1):
        f = open("./0500s/filt_05%s.log" % str(j))
        count = 0
        while True:
                    line = f.readline()
                    count += 1
                    if count <= 8:
                        continue
                    if count % 1000000 == 0:
                        print(count)

                    if not line:
                        break
                    info = line.split()
                    if float(info[0]) < t1 - 1000:
                        continue
                    if float(info[0]) > t2 + 1000:
                        break
                        continue
                    
                    if info[2] == src:
                        res.add(info[4])
                    if info[4] == src:
                        res.add(info[2])
    return res






t0 = float(sys.argv[1])
t1 = float(sys.argv[2])




#t = [1688008209,1688008269,1688008308,1688008370,1688008411,1688008494,1688008585,1688008686,1688008752,1688008855,1688008944,1688009092,1688009174,1688009214,1688009413,1688009473,1688009562,1688009641,1688009744,1688009849,1688009909,1688009969]
#t = [1687835405,1687835507,1687835547,1687835592,1687835637,1687835687,1687835732,1687835787,1687835812,1687835852,1687835912,1687835952]
#t = [1687835482,1687835507,1687835547]
tL = [4]
label = []
#label = [[1,1],[1,1],[1,1],[0,1],[0,1],[0,1],[0,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,10],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]

ftag = open("tags.json", "w")
tags = dict()
for j in range(len(t)):
    tags[str(j)] = list()

def inserthttp(s, d, uuid):
    finhttp = open("./menupass9/http.log")
    fhttp = open("./http06%s.log" % start, "a")
    print(start)
    while True:
        line = finhttp.readline()
        if not line: break
        info = line.split()
        if info[1] != uuid: continue
        print("ok")
        T_insert = (float(info[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
        info[0] = str(T_insert)
        info[2] = s
        info[4] = d
        string = " ".join(info)
        fhttp.write(string + "\n")
    finhttp.close()
    fhttp.close()

with open("./menupass9/conn.log") as f:
    F_a = f.readlines()
    print(len(F_a))
    temp = list()
    #for i in range(len(F_a)):
    #    if ":" in F_a[i].split()[2] or ":" in F_a[i].split()[4]:
    #        continue
    #    temp.append(F_a[i])
    #F_a = temp
print(F_a)
print(len(F_a))
if tL == []:
    pass # todo
print("stage1")

with open("./historyc/history06%s.json" % start) as f:
    date = json.load(f)
stat = dict()
for ip in date:
    if ip not in stat:
        stat[ip] = dict()
        stat[ip]['traffic'] = list()
        stat[ip]['domain'] = list()
        stat[ip]['connection'] = list()
        stat[ip]['shabi'] = list()
        stat[ip]['flag'] = 0
        stat[ip]['appear'] = 0
    flag = 0
    if date[ip]['connection'] == 0: pass
    elif date[ip]['shabi'] / date[ip]['connection'] > 0.35 or date[ip]['single'] / date[ip]['connection'] > 0.7:
        flag = 1
    if stat[ip]['flag'] == 1: continue
    else: stat[ip]['flag'] = flag

    stat[ip]['traffic'].append(date[ip]['traffic'])
    stat[ip]['domain'].append(date[ip]['domain'])
    stat[ip]['connection'].append(date[ip]['connection'])
    stat[ip]['appear'] += 1
    stat[ip]['shabi'].append(date[ip]['shabi'])


for ip in stat:
    if stat[ip]['domain'][0] < 5 and not inninn(ip) and stat[ip]['shabi'][0] > 0:
        temp = random.randint(1,10)
        if temp >= 7:
            src = ip
            break
print(src)
dst = src

fout = open("./06%s.log" % start, "a")

inserted = 0
for j in range(0, len(t) - 1):
    print("start a stage")
    if j == 0:
        F_aj = list() # todo
        for flow in F_a:
            info = flow.split()[0]
            if float(info) < t[j+1] and float(info) > t[j]:
                F_aj.append(flow)

        T_start = (t[j]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        T_end = (t[j+1]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        N_lm = 1
        Lm_list = list()
        #r = 0
        for ip in stat:
            if inninn(ip):
                a = random.randint(1, 10)
                if a >= 7 and "202.120" not in ip and ip != src:
                    Lm_list.append(ip)                 
            if len(Lm_list) == N_lm: break
        #fout = open("./07%s.log" % start, "a")
        cut = 0
        for flow in F_aj:
            T_insert = (float(flow.split()[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
            info = flow.split()
            info[0] = str(T_insert)
            info[2] = src
            info[4] = Lm_list[cut % N_lm]
            cut += 1
            string = " ".join(info)
            print(string)
            inserthttp(src, Lm_list[cut % N_lm], info[1])
            fout.write(string + "\n")
        dst = Lm_list[0]
         
    elif j in tL:
        #src = dst
        F_aj = list() # todo
        for flow in F_a:
            info = flow.split()[0]
            if float(info) < t[j+1] and float(info) > t[j]:
                F_aj.append(flow)
        print(F_aj)
        
        T_start = (t[j]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        T_end = (t[j+1]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        N_lm = 30
        Lm_list = list()
        #r = 0
        for ip in stat:
            if inninn(ip):
                a = random.randint(1, 10)
                if a >= 7 and ip != src:
                    Lm_list.append(ip)                 
            if len(Lm_list) == N_lm: break
        #fout = open("./07%s.log" % start, "a")
        cut = 0
        for flow in F_aj:
            T_insert = (float(flow.split()[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
            info = flow.split()
            info[0] = str(T_insert)
            info[2] = src
            info[4] = Lm_list[cut % N_lm]
            cut += 1
            string = " ".join(info)
            print(string)
            inserthttp(src, Lm_list[cut % N_lm], info[1])
            fout.write(string + "\n")
        while True:
            a = random.randint(0, cut - 1)
            if "202.120" not in Lm_list[a]:
                dst = Lm_list[a] 
                break          

    else:
        print(j)
        ll = j - 1
        if ll in tL:
            src = dst
        if ll == 0:
            src = dst
        
        F_aj = list() # todo
        for flow in F_a:
            info = flow.split()[0]
            if float(info) < t[j+1] and float(info) > t[j]:
                F_aj.append(flow)

        T_start = (t[j]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        T_end = (t[j+1]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        N_lm = 1
        Lm_list = list()
        #r = 0
        if j == len(t) - 2:
            for ip in stat:
                if stat[ip]['domain'][0] < 5 and not inninn(ip) and stat[ip]['shabi'][0] > 0:
                    temp = random.randint(1,10)
                    if temp >= 7 and ip != src:
                        Lm_list.append(ip)
                if len(Lm_list) == N_lm: break
        else:
            for ip in stat:
                if inninn(ip):
                    a = random.randint(1, 10)
                    if a >= 7 and "202.120" not in ip and ip != src:
                        Lm_list.append(ip)                 
                if len(Lm_list) == N_lm: break
        #fout = open("./07%s.log" % start, "a")
        cut = 0
        for flow in F_aj:
            T_insert = (float(flow.split()[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
            info = flow.split()
            info[0] = str(T_insert)
            info[2] = src
            info[4] = Lm_list[cut % N_lm]
            cut += 1
            string = " ".join(info)
            print(string)
            inserthttp(src, Lm_list[cut % N_lm], info[1])
            fout.write(string + "\n") 


            


exit()
print("stage2")
for j in range(0, len(t) - 1):
    print("start a round")
    if j in tL:
        #src = dst
        F_aj = list() # todo
        for flow in F_a:
            info = flow.split()[0]
            if float(info) < t[j+1] and float(info) > t[j]:
                F_aj.append(flow)
        
        T_start = (t[j]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        T_end = (t[j+1]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        C_src = gain(T_start,T_end,src)#Todo
        print(len(C_src))
        print("half clear")

        N_lm = 10
        Lm_list = []

        r = 0
        temp = random_(T_end, 400, 1)
        print(len(temp))
        p = 2
        while(len(temp) == 0):
            temp = random_(T_end, 400 * p, label[j][0])
            p += 1
            print(len(temp))
        while r < N_lm:
            temp = list(temp)
            a = random.randint(0, len(temp) - 1)
            #if temp[a] in C_src:
            Lm_list.append(temp[a])
            r += 1
        print("almost")
        for flow in F_aj:
            T_insert = (float(flow.split()[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
            a = randindex(Lm_list)
            Insert(T_insert, src, a, flow)
            tags[str(j)].append([flow, src, a, T_insert])

        dst = randindex(Lm_list)
    
    else:
        print(j)
        ll = j - 1
        if ll in tL:
            src = dst 
        F_aq = list() # todo
        for flow in F_a:
            info = flow.split()[0]
            if float(info) < t[j+1] and float(info) > t[j]:
                F_aq.append(flow)
        print(F_aq)
        T_start = (t[j]-t[0])/(t[-1] - t[0])*(t1-t0) + t0
        T_end = (t[j+1]-t[0])/(t[-1] - t[0])*(t1-t0) + t0

        C_src = gain(T_start,T_end,src)#todo
        print(len(C_src))
        print("half clear")
        
        host = list()
        m = 0
        temp = random_(T_end, 400, label[j][0])
        print(len(temp))
        p = 2
        while(len(temp) == 0):
            temp = random_(T_end, 400 * p, label[j][0])
            p += 1
            print(len(temp))
        while m < label[j][1]:
            temp = list(temp)
            a = random.randint(0, len(temp) - 1)
            #if temp[a] in C_src:
            host.append(temp[a])
            m += 1
        print("almost")
        for flow in F_aq:
            T_insert = (float(flow.split()[0]) - t[0])/(t[-1] - t[0]) * (t1 - t0) + t0
            a = randindex(host)
            Insert(T_insert, src, a, flow)
            tags[str(j)].append([flow, src, a, T_insert])

        
json.dump(tags,ftag)
    



