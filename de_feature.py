import json
import sys
date = sys.argv[1]


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

with open("./data_ex/exf_09%s_qwm" % date, "w") as f:
    json.dump(data,f)