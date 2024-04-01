import json
import random
START = "101.94.251.160"
import time

ta = time.time()
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

with open("dfs.json") as f:
    matrix = json.load(f)
count = 0
candi = set()
for ip in matrix:
    if inninn(ip):
        a = random.randint(1,10)
        if a >= 9:
            candi.add(ip)
            count += 1
        if count == 1000: break
print(len(candi))

def tdfs(node, t, start):
    fin = open("./0624/%s.json" % node)
    data = json.load(fin)
    fin.close()

    for v in matrix[node]:
        if v == 'flag':
            continue
        if v not in matrix:
            return
        if matrix[v]['flag'] == 1 or v == start:
            continue
        d_flag = False
        for i in range(len(data[v])):
            if data[v][i] > t:
                d_flag = True
                t_next = data[v][i]
                matrix[v]['flag'] = 1
                break

        if not d_flag:
            return
        else: 
            #print(v)
            tdfs(v, t_next, start)
        
        
count = 0
for ip in candi:
    count += 1
    print(ip)
    print(count)
    tdfs(ip, 0, ip)
    for ip in matrix:
        matrix[ip]['flag'] = 0

tb = time.time()

print(tb - ta)