import json
from sklearn.cluster import MeanShift
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
import numpy as np
import sys
import time
haha = time.time()
def minmax(a):
    min = 0
    max = 0
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
        if a[i] > max:
            max = a[i]
    if min != max:
        for i in range(len(a)):
            a[i] /= (max - min)



with open("impo09%s.json" % sys.argv[1]) as f:
    data = json.load(f)

spike = list()
dspike = list()
burst = list()
dburst = list()
http = list()
name = list()
for ip in data:
    name.append(ip)
    spike.append(data[ip]['data'])
    dspike.append(data[ip]['domain'])
    burst.append(data[ip]['burst'])
    dburst.append(data[ip]['dburst'])
    http.append(data[ip]['ua'])

spike_ = spike
dspike_ = dspike
burst_ = burst
dburst_ = dburst
http_ = http
X_ = list()
for i in range(len(spike)):
    X_.append([spike_[i], dspike_[i], burst_[i], dburst_[i], int(http_[i])])


minmax(spike)
minmax(dspike)
minmax(burst)
minmax(dburst)

X = list()

for i in range(len(spike)):
    X.append([spike[i], dspike[i], burst[i], dburst[i], int(http[i])])

'''
number = 3

cluster = KMeans(n_clusters=number).fit(X)

y_pred = cluster.labels_

ans = [0 for i in range(number)]

for i in range(len(y_pred)):
    ans[y_pred[i]] += 1

    #if y_pred[i] == 0:
    #    print(X_[i])
print(ans)
'''

def doit(method):
    for number in range(2, 4):
        if method == 1:
            cluster = SpectralClustering(n_clusters=number,n_jobs=-1).fit(X)
        elif method == 2:
            cluster = DBSCAN(eps=0.1,n_jobs=-1).fit(X)
        elif method == 3:
            cluster = KMeans(n_clusters=number,n_jobs=-1).fit(X)
        elif method == 4:
            cluster = MeanShift(bandwidth=0.6).fit(X)
        elif method == 5:
            cluster = AgglomerativeClustering(n_clusters=number).fit(X)

        y_pred = cluster.labels_
        print(np.unique(y_pred))

        ans = [0 for i in range(len(np.unique(y_pred)))]
        for i in y_pred:
            ans[i] += 1

        print(ans)
        print(metrics.silhouette_score(X, y_pred, metric='euclidean', sample_size=None,
    random_state=None))
    print(' ')

    res = dict()
    for i in range(len(y_pred)):
        if int(y_pred[i]) in res:
            res[int(y_pred[i])].append(name[i])
        else:
            res[int(y_pred[i])] = [name[i]]
    with open("clutser%s_%d.json" % (sys.argv[1], method), "w") as f:
        json.dump(res,f)

#doit(5)
doit(1)
#doit(3)

print(time.time()-haha)


