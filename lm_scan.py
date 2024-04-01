import sys
import math

date = sys.argv[1]

win = sys.argv[2]

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


f = open("./06%s.log" % date)
tflag = True
start = 0
length = int(86400/int(win))
print(length)

total = dict()
slice = [{} for i in range(length)]
print(slice)


hs = ['80', '22', '21', '23', '3306', '443', '53', '445', '137', '8080', '8888', '139', '3389', '135', '1433', '1521']

count = 0
while True:
    line = f.readline()
    count += 1
    if count <= 8: continue
    if not line: break
    info = line.split()
    if len(info) <= 3:
        continue
    if tflag:
        start = float(info[0])
        tflag = False
    
    index = int((float(info[0]) - start)/int(win))
    if index > len(slice) - 1: break
    if index < 0: continue

    if inninn(info[2]) and inninn(info[4]):
        if info[2] not in slice[index]:
            slice[index][info[2]] = dict()
            slice[index][info[2]]['s2'] = 0
            slice[index][info[2]]['s3'] = 0
            slice[index][info[2]]['total'] = 0
            slice[index][info[2]]['dst'] = dict()

        slice[index][info[2]]['total'] += 1
        if info[4] not in slice[index][info[2]]['dst']:
            slice[index][info[2]]['dst'][info[4]] = 0
        slice[index][info[2]]['dst'][info[4]] += 1

        dport = info[5]
        weight = 0.1
        if dport in hs:
            weight = 1
        if info[11] == "REJ" or info[11] == "S0":
            slice[index][info[2]]['s2'] += weight

    if count % 100000 == 0: print(count)

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

import json

for i in range(length):
    f = open("./bothunter/06%s_%s.log" % (date, str(i)), "w")
    json.dump(slice[i], f)
    


        
            
    

    




