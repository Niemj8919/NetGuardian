import json

with open("finally25.json") as f:
    links = json.load(f)
print(len(links))
rank = dict()
del links['142.20.60.1']
for ip in links:
    links[ip].sort()
with open("s125.json") as f:
    data = json.load(f)
    for ip in data:
        rank[ip] = data[ip]
with open("s225.json") as f:
    data = json.load(f)
    for ip in data:
        if ip in rank:
            if data[ip] > rank[ip]:
                rank[ip] = data[ip]
        else: rank[ip] = data[ip]
with open("s325.json") as f:
    data = json.load(f)
    for ip in data:
        if ip in rank:
            if data[ip] > rank[ip]:
                rank[ip] = data[ip]
        else: rank[ip] = data[ip]
with open("s425.json") as f:
    data = json.load(f)
    for ip in data:
        if ip in rank:
            if data[ip] > rank[ip]:
                rank[ip] = data[ip]
        else: rank[ip] = data[ip]
res = list()
flags = dict()
for ip in links:
    flags[ip] = 1

sC = dict()

def Check(graph, s, e, path=[]):  # s起点，e终点
    path = path + [s]
    #print(path)
   # name = "##".join(path)
    #if name not in sC:
    #    sC[name] = 0
    # print('path',path)   取消注释查看当前path的元素
    if s == e:
        # print('回溯')
        return [path]

    paths = []
    # 存储所有路径
    flags[s] = 0
    for node in graph[s]:
        if node not in path and flags[node]:
            ns = Check(graph, node, e, path)
            #flags[node] = 1
            for n in ns:
                paths.append(n)
    # print(paths,'回溯')
    #print(paths)
    return paths
pathss = list()
count = 0
for ip1 in links:
    count += 1
    for ip2 in links:
        if ip1 != ip2: 
            #print(ip1 + " " + ip2)
            allpath = Check(links,ip1,ip2)
            #if ip1 == '142.20.56.202' : print("ok" + str(pa))
            for pa in allpath:
                pathss.append(pa)
            #for p in allpath:
            #    print("路径有:%s"%p)
        for ip in links:
            flags[ip] = 1
    print(count)
    #if count == 100: break

print(len(pathss))

print(sC)
        


for i in range(len(pathss)):
    if pathss[i][0] == "142.20.56.202":
        pathss[i].insert(0,"132.197.58.198")
    


score = dict()
count = 0
for link in pathss:
    count += 1
    #print(count)
    #print(link)
    score[";".join(link)] = 0
    flag = 0
    for ip in link:
        if ip == "132.197.58.198":
            flag = 1
        else: score[";".join(link)] += rank[ip]
    if not flag: score[";".join(link)] /= len(link)
    else: score[";".join(link)] /= (len(link) - 1)
#print(score)

with open("xxxxxa25.json","w") as f:
    json.dump(score, f)