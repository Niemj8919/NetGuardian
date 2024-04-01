import json
import os
from matplotlib import pyplot as plt

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
    
files = os.listdir("./biohazard")

traffic = []
traffic1 = []
traffic2 = []
traffic3 = []
traffic4 = []

flow = []
flow1 = []
flow2 = []
flow3 = []
flow4 = []

server = []

innode = []

tinnode = []

outnode = []

stable = dict()
tstable = dict()

ave = []
tave = []


def work(month):
    for i in range(1, 32):
        
        if i < 10: a = "0" + str(i)
        else: a = str(i)
        try:
            with open("./biohazard/2023-0%s-%s_res.json" % (month,a)) as f:
                data1 = json.load(f)
            with open("./biohazard/2023-0%s-%s_high.json" % (month,a)) as f:
                data2 = json.load(f)
        except:continue

        if data1['flow'] < 60000000: continue
        
        traffic.append(data1['traffic'])
        traffic1.append(data1['traffic1'])
        traffic2.append(data1['traffic2'])
        traffic3.append(data1['traffic3'])
        traffic4.append(data1['traffic4'])

        flow.append(data1['flow'])
        flow1.append(data1['flow1'])
        flow2.append(data1['flow2'])
        flow3.append(data1['flow3'])
        flow4.append(data1['flow4'])

        innode.append(len(data1['innode']))
        outnode.append(len(data1['outnode']))

        a = 0
        for node in data1['innode']:
            if node.startswith("202.120."):
                a += 1
        server.append(a)


        temp = []
        tp = []
        ct = 0
        tct = 0
        for ip in data2:
            if not inninn(ip): continue

            temp.append(len(data2[ip]['inbound']) + len(data2[ip]['outbound']))
            
            if len(data2[ip]['inbound']) + len(data2[ip]['outbound']) >= 10:
                tp.append(ip)
                tct += len(data2[ip]['inbound'])
                tct += len(data2[ip]['outbound'])
                if ip not in tstable:
                    tstable[ip] = 0
                tstable[ip] += 1

            ct += len(data2[ip]['inbound'])
            ct += len(data2[ip]['outbound'])

            if ip not in stable:
                stable[ip] = 0
            stable[ip] += 1
        ave.append(ct / len(temp))
        tave.append(tct / len(tp))

        tinnode.append(len(tp))
        print("ok" + str(i))


work("5")
work("6")
work("7")
work("8")

print(len(traffic))

res = dict()

res['traffic'] = traffic
res['traffic1'] = traffic1
res['traffic2'] = traffic2
res['traffic3'] = traffic3
res['traffic4'] = traffic4

res['flow'] = flow
res['flow1'] = flow1
res['flow2'] = flow2
res['flow3'] = flow3
res['flow4'] = flow4

res['server'] = server
res['innode'] = innode
res['outnode'] = outnode


res['ave'] = ave
res['stable'] = stable

res['tave'] = tave
res['tstable'] = tstable
res['tinnode'] = tinnode

with open("QZA.json", "w") as f:
    json.dump(res,f)

               






# 总流量
# 三个分流量

#总flow
#三个分flow

#内网、外网节点
# 服务器节点

## 内网ip通信节点数均值

## 稳定通信内网节点
