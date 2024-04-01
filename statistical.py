import matplotlib.pyplot as plt
import numpy as np
t_file = [501, 502, 503, 504, 505, 506, 507, 508, 509]
t_file = np.arange(501, 510)
print(t_file)
edges = [144160171, 142886970, 152344099, 141186793, 147751467,141323508,127497940,145720086,143468151]

'''
f1 = open("stat.txt")
nodes = f1.readlines()
for i in range(len(nodes)):
    nodes[i] = int(nodes[i][:-1])
print(nodes)
f2 = open("stat_inner.txt")
total = f2.readlines()
inner = list()
outer = list()
for i in range(len(total)):
    if i % 2 == 0:
        inner.append(int(total[i][:-1]))
    else:
        outer.append(int(total[i][:-1]))

inninn = [50726,46932713,32762,47493275,35955,46686658,63976,52561329,67389,53114712,68175,50802195,48879,40756746,72448,52877539,64275,49790664]

innernodes = list()
inneredge = list()
for i in range(len(inninn)):
    if i % 2 == 0:
        innernodes.append(inninn[i])
    else:
        inneredge.append(inninn[i])

oneway = [23579,110646,22839,51477,28535,58648,53820,98437,53682,99415,56674,95993,40425,76549,59470,100222,50091,104354]
innerconeway = list()
outerconeway = list()

for i in range(len(oneway)):
    if i % 2 == 0:
        innerconeway.append(oneway[i])
    else:
        outerconeway.append(oneway[i])


plt.bar(t_file+0.2, edges, color = 'r', width = 0.2, label = 'total')
plt.bar(t_file, inneredge,width = 0.2, color = 'b', label = 'interact')
plt.legend()
plt.savefig("edges.png")
plt.cla()


plt.bar(t_file+0.2, inner, color = 'r', width = 0.2, label = 'total')
plt.bar(t_file, innernodes,width = 0.2, color = 'b', label = 'interact')
plt.legend()
plt.savefig("inner.png")
plt.cla()

plt.bar(t_file, inner, color = 'r', label = 'inner')
plt.bar(t_file, outer, bottom = innerconeway, color = 'b', label = 'outer')
plt.legend()
plt.savefig("nodes.png")
plt.cla()


plt.bar(t_file, innerconeway, color = 'r', label = 'inner')
plt.bar(t_file, outerconeway, bottom = innerconeway, color = 'b', label = 'outer')
plt.legend()
plt.savefig("oneway.png")
plt.cla()

'''

date = np.arange(0,24)

f0 = open("stat-traffic.txt")
t = list()
temp = list()
while True:
    line = f0.readline()[:-1]
    if not line:
        t.append(temp)
        break
    if line.startswith("050"):
        t.append(temp)
        temp = []
        continue
    temp.append(int(line))
print(len(t))

for i in range(len(t)):
    for j in range(len(t[i])):
        t[i][j] /= 1000000000

for i in range(1, len(t)):

    plt.plot(np.arange(len(t[i]) - 2), t[i][1:-1])
    plt.savefig("traffic_050%d.png" % i)
    plt.cla()

