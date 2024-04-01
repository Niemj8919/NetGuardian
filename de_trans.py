import json
import sys
date = sys.argv[1]
window = sys.argv[2]
import numpy as np
with open("./data_ex/data_ex_09%s" % date) as f:
    data_ = json.load(f)

#print(ctt)
s1_ = list()
for ip in data_:
    s1_.append(data_[ip]['data'][0])
r1 = np.percentile(s1_, 99)
#print(r1)

data = dict()
outdata = dict()
for ip in data_:
    if data_[ip]['data'][0] <= r1:
        data[ip] = data_[ip]['data']
    else:
        outdata[ip] = data_[ip]['data']

s1 = list()
s2 = list()
s3 = list()

for ip in data:

    s1.append(data[ip][0])
    s2.append(data[ip][1])
    s3.append(data[ip][2])




s1.sort()
s2.sort()
s3.sort()

import matplotlib.pyplot as plt

x = list(np.arange(len(s1) - 10, len(s1) - 1))

sum = 0
for i in range(len(s1) - 1):
    sum += s1[i]

sum_ = 0
for i in range(len(s1) - 1):
    sum_ += s1[i]
    if sum_  >= 0.1*sum:
        print(i)
        break

plt.savefig("./s1_%s.png" % date)


def QWM(s):
    q1 = np.percentile(s,25)
    q2 = np.percentile(s,50)
    q3 = np.percentile(s,75)


    return (q1 + 2*q2 + q3) / 4

qwm1 = QWM(s1)
qwm2 = QWM(s2)
qwm3 = QWM(s3)




for ip in data:
    data[ip][0] /= qwm1
    data[ip][1] /= qwm2
    data[ip][2] /= qwm3


history = list()

for i in range(int(window)):
    try:
        with open("./data_ex/exf_09%s_qwm" % str(int(date) - int(i) - 1)) as f:
            #print(str(int(date) - int(i) - 1))
            history.append(json.load(f))
    except:
        with open("./data_ex/exf_09%s_qwm" % str(int(date) - int(i) - 1)) as f:
            #print(str(int(date) - int(i) - 1))
            history.append(json.load(f))

ctt = 0
for ip in data_:
    count = 0
    for day in history:
        if ip in day:
            count += 1
    if count >= 5: ctt += 1


    #print(data[ip]['data'])

for i in range(len(s1)):
    s1[i]  = s1[i] / qwm1
for i in range(len(s2)):
    s2[i] /= qwm2
for i in range(len(s3)):
    s3[i] /= qwm3


center = [np.mean(s1), np.mean(s2), np.mean(s3)]
print(center)

#print(len(s1))

import math

def S1(x1, x2, x3, c):
    dist = math.sqrt( (x1 - c[0])*(x1 - c[0]) + (x2 - c[1])*(x2 - c[1]) + (x3 - c[2])*(x3 - c[2]) )
    return dist

count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def S2(ip, x1,x2,x3):
    global history
    temp = 0
    flag = False
    his_feat = list()
    for i in range(len(history)):
        if ip in history[i]:
            #if history[i][ip]['data'][0] == 0:
            #    print(history[i][ip]['data'])
            temp += 1
            dd = history[i][ip]
            dd.append(i)
            
            his_feat.append(dd)
    center = [[],[],[]]
    if temp >= int(window) / 3 or temp >= 3: flag = True
    count[temp] += 1
    if not flag:
        return flag, False, False
    for de in his_feat:
        center[0].append(de[0])
        center[1].append(de[1])
        center[2].append(de[2])

    center[0].sort()
    center[1].sort()
    center[2].sort()

    ctr = [0,0,0]
    ctr[0] = np.percentile(center[0], 50)
    ctr[1] = np.percentile(center[1], 50)
    ctr[2] = np.percentile(center[2], 50)

    if ctr[0] == 0: ctr[0] = 1

    dist = [(x1 - ctr[0]) / ctr[0], (x2 - ctr[1]) / ctr[1], (x3 - ctr[2]) / ctr[2]]
    #center[0] /= len(his_feat)
    #center[1] /= len(his_feat)
    #center[2] /= len(his_feat)

    #dist = math.sqrt( (x1 - center[0])*(x1 - center[0]) + (x2 - center[1])*(x2 - center[1]) + (x3 - center[2])*(x3 - center[2]))
    
    

    return flag,dist,math.sqrt(dist[0]*dist[0] + dist[1]*dist[1] + dist[2]*dist[2])
#print(outdata)
res = dict()


angle = dict()
for ip in data:
    res[ip] = [0,0,0]
    res[ip][0] = S1(data[ip][0], data[ip][1], data[ip][2], center)
    flag, dist, res[ip][1]= S2(ip, data[ip][0], data[ip][1], data[ip][2])
    angle[ip] = dist



polar = list()


print(count)
#print(res)
print(len(angle))

angle_dis = dict()
for ip in angle:
    if angle[ip] == False: 
        res[ip][2] = False
        continue
    else:
        phi = math.acos(angle[ip][2] / math.sqrt(math.pow(angle[ip][0], 2) + math.pow(angle[ip][1], 2) + math.pow(angle[ip][2], 2))) * 180 / math.pi
        theta = math.atan(angle[ip][1] / angle[ip][0]) * 180 / math.pi
        
        i = -90
        while True:
            if i < theta and (i + 6) >= theta:
                theta = i
                break
            i += 6
        
        i = 0
        while True:
            if i < phi and (i + 6) >= phi:
                phi = i
                break
            i += 6
        name = str(phi) + "###" + str(theta)
        if name not in angle_dis:
            angle_dis[name] = 0
        angle_dis[name] += 1

print(angle_dis)

max = 0
for pair in angle_dis:
    if angle_dis[pair] > max:
        max = angle_dis[pair]

for ip in angle:
        if angle[ip] == False: continue
        phi = math.acos(angle[ip][2] / math.sqrt(math.pow(angle[ip][0], 2) + math.pow(angle[ip][1], 2) + math.pow(angle[ip][2], 2))) * 180 / math.pi
        theta = math.atan(angle[ip][1] / angle[ip][0]) * 180 / math.pi
        
        i = -90
        while True:
            if i < theta and (i + 6) >= theta:
                theta = i
                break
            i += 6
        
        i = 0
        while True:
            if i < phi and (i + 6) >= phi:
                phi = i
                break
            i += 6
        name = str(phi) + "###" + str(theta)
        res[ip][2] = (max - angle_dis[name]) / max

#print(res['10.42.255.85'])


t1 = list()
t2 = list()
t3 = list()
for ip in res:
    t1.append(res[ip][0])
    if res[ip][1] == False: continue
    t2.append(res[ip][1])
    t3.append(res[ip][2])

t1.sort()
t2.sort()
t3.sort()

qwm1 = QWM(t1)
qwm2 = QWM(t2)
qwm3 = QWM(t3)

rank = dict()

for ip in res:
    if res[ip][1] == False:
        rank[ip] = res[ip][0]
    else:
        rank[ip] = (qwm1*res[ip][0] + qwm2*res[ip][1] + qwm3*res[ip][2]) / (qwm1 + qwm2 + qwm3)

#rank = sorted(rank.items(),key = lambda x:x[1],reverse = True)

with open("data_exfil_09%s.json" % date, "w") as fout:
    json.dump(rank, fout)


#for i in range(len(s1)):
#    res[s4[i]] = [0,0,0]
#    res[s4[i]][0] = S1(s1[i], s2[i], s3[i], center)