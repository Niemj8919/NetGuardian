import sys

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

f = open("06%s.log" % date)

count = 0

res = dict()

while True:
    line = f.readline()
    count += 1
    if count <= 8: continue
    if not line: break
    info = line.split()

    if len(info) <= 3:
        continue
    
    if info[2].startswith("202.120"): continue
    if info[2] == "10.10.39.76": continue
    if info[2].startswith("10.10.254"): continue
    if inninn(info[2]) and not inninn(info[4]):
        if info[2] not in res:
                res[info[2]] = dict()
                res[info[2]]['data'] = [0,0,0]
                res[info[2]]['domain'] = set()
        if info[9] == '-': pass
        else: res[info[2]]['data'][0] += int(info[9])
        res[info[2]]['data'][1] += 1
        res[info[2]]['domain'].add(info[4])

    if count % 100000 == 0: print(count)

for ip in res:
    res[ip]['data'][2] = len(res[ip]['domain'])
    res[ip]['domain'] = 'cleaned'


import json

with open("exf_06%s" % date, "w") as fo:
        json.dump(res, fo)