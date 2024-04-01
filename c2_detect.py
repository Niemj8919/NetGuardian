##before run this, please run c2c.py and 2c2.py for preprocessing

import json
import sys
import numpy as np
date = sys.argv[1]

with open("./C2C/c2_final_09%s.json" % date) as f:
    data = json.load(f)

with open("./C2C/final_tt09%s.json" % date) as f:
    data2 = json.load(f)



yx = dict()
dt = dict()
sus22 = dict()
no = list()

for pair in data2:
    if "132.197.158.98" in pair:
        print(pair)
    t = data2[pair]
    #print(t)
    t.sort()

    delta = list()
    epsilon = list()

    for i in range(len(t) - 1):
        delta.append(t[i + 1] - t[i])
    mean = np.mean(delta)
    std = np.std(delta, ddof = 0)
    mutate = std / mean
    if mutate >= 1:
        no.append(pair)
    delta.sort()
    if "142.20.58.149" in pair:
        print(delta)
    for i in range(len(delta) - 1):
        epsilon.append(delta[i + 1] - delta[i])
    flag = False
    ct = 0
    for i in range(len(epsilon)):
        if epsilon[i] > 0.5 * mean or epsilon[i] < -0.5 * mean:
            ct += 1
    if ct < len(epsilon) / 10: 
        if mutate < 0.3 and len(delta) > 100:
            sus22[pair] = data2[pair]
    
    

    #tmp = -int(len(delta) / 100)
    #delta = delta[-tmp:tmp]
    #if "142.20.58.149" in pair and "132.197.158.98" in pair: 
    #    print(delta)
    #    exit()
    
    
    

    if "132.197.158.98" in pair: print(mutate)

    if len(delta) >= 10 and mutate < 0.1:
        sus22[pair] = data2[pair]
    

for pair in data:
    yx[pair] = [0,0,0,0,0]
    yx[pair][0] = len(data[pair]['R'])
    temp = 0
    stat = dict()
    for ts in data[pair]['R']:
        temp += len(ts)
        for domain in ts:
            if domain in stat:
                stat[domain] += 1
            else: stat[domain] = 1
    yx[pair][1] = temp / yx[pair][0]
    max = 0
    for domain in stat:
        if stat[domain] > max:
            max = stat[domain]
    yx[pair][2] = max

    tl = data[pair]['T']
    tl.sort()
    delta = list()
    for i in range(len(tl) - 1):
        delta.append(tl[i + 1] - tl[i])
    
    if yx[pair][0] >= 3:
        mean = np.mean(delta)
        std = np.std(delta, ddof = 0)
        yx[pair][3] = std / mean
        yx[pair][4] = mean
    else:
        yx[pair][3] = 100
        yx[pair][4] = 100000
    
    #if len(delta) <= 10 and yx[pair][3] < 0.15 and yx[pair][4] > 120:
    #    sus22[pair] = yx[pair]
    
    dt[pair] = delta


ct = 0
sus = dict()
for pair in yx:
    if yx[pair][0] >= 4 and yx[pair][1] <= 0.4: 
        #print(pair + str(yx[pair]))
        sus[pair] = yx[pair]
        ct += 1
    elif yx[pair][0] >= 4 and yx[pair][1] <= 1 and yx[pair][2] <=1: 
        #print(pair + str(yx[pair]))
        sus[pair] = yx[pair]
        ct += 1
print(ct)

times = dict()

for pair in sus:
    ip = pair.split("#####")[0]
    domain = pair.split("#####")[1]
    if domain not in times:
        times[domain] = set()
    times[domain].add(ip)

ct = 0
sus2= dict()
for pair in sus:
    domain = pair.split("#####")[1]
    if len(times[domain]) >= 10 or sus[pair][3]  >  0.15 or sus[pair][4]  < 600:
        continue
    sus2[pair] = sus[pair]
    #print(pair + str(yx[pair]) + str(dt[pair]))

print(len(sus22))

cer = dict()
for pair in sus22:
    ips = pair.split("#####")
    if ips[0] not in cer:
        cer[ips[0]] = 0
    if ips[1] not in cer:
        cer[ips[1]] = 0
    cer[ips[0]] += 1
    cer[ips[1]] += 1

for pair in data2:
    ips = pair.split("#####")
    if ips[0] in cer and cer[ips[0]] >= 10 and len(data2[pair]) > 100 and pair not in no:
        sus22[pair] = data2[pair]
    if ips[1] in cer and cer[ips[1]] >= 10 and len(data2[pair]) > 100 and pair not in no:
        sus22[pair] = data2[pair]


with open("./C2C/c2_feature_06%s.json" % date, "w") as fout:
    json.dump(sus2, fout)

with open("./C2C/c2_feature_06%s_2.json" % date, "w") as fout:
    json.dump(sus22, fout)