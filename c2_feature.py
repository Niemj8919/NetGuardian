import json
import sys
date = sys.argv[1]
with open("./C2C/c2_09%s.json" % date) as f:
    data = json.load(f)

with open("./C2C/tt09%s.json" % date) as f:
    data2 = json.load(f)
for ip in data2:
    if ip == "142.20.56.202": print("ok")
res2 = dict()

for ip1 in data2:
    for ip2 in data2[ip1]:
        if ip2 == "132.197.158.98": print(ip2)
        #print(data2[ip1][ip2])
        #exit()
        name = ip1 + "#####" + ip2
        res2[name] = data2[ip1][ip2]


res = dict()


for ip in data:
    print(ip)
    print(len(data[ip]))
    if len(data[ip]) > 10000: continue
    count = 0
    for domain in data[ip]:
        count += 1
        print(count)
        if len(data[ip][domain]) > 100 or len(data[ip][domain]) < 3: continue
        name = ip + "#####" + domain
        res[name] = dict()
        res[name]['R'] = list()
        res[name]['T'] = data[ip][domain]
        for ts in data[ip][domain]:
            temp = set()
            for dm in data[ip]:
                if dm == domain: continue
                #if len(data[ip][dm]) > 100 or len(data[ip][dm]) < 3: continue
                for t in data[ip][dm]:
                    if t - ts > -5 and t - ts < 5:
                        temp.add(dm)
            res[name]['R'].append(list(temp))

for name in res2:
    if "132.197.158.98" in name:
        print(name)

with open("./C2C/c2_final_09%s.json" % date, "w") as f:
    json.dump(res,f)

with open("./C2C/final_tt09%s.json" % date, "w") as f:
    json.dump(res2,f)


