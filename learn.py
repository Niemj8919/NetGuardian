from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import random
import json
import joblib



with open("phish.json") as f:
    phish_raw = json.load(f)

with open("legal.json") as f:
    legal_raw = json.load(f)

train_list = list()

for data in phish_raw:
    train_list.append(phish_raw[data])

for data in legal_raw:
    train_list.append(legal_raw[data])

random.shuffle(train_list)

scaler = MinMaxScaler()
scaler = scaler.fit(train_list)
train_list = scaler.transform(train_list)

print(train_list)

X = list()
labels = list()
for data in train_list:
    X.append(data[:-1])
    labels.append(data[-1])

X = np.array(X)
labels = np.array(labels)

X_learn = X[:4000]
labels_learn = labels[:4000]
X_test = X[4000:]
labels_test = labels[4000:]


clf = SVC(gamma = 0.5)

clf.fit(X_learn,labels_learn)

y_pred = clf.predict(X_test)

print(accuracy_score(labels_test, y_pred))
print(precision_score(labels_test, y_pred))










with open("test.json") as f:
    test_raw = json.load(f)

train_list = list()

for data in test_raw:
    test_raw[data].append(data) 
    train_list.append(test_raw[data])

random.shuffle(train_list)

X = list()
labels = list()
for data in train_list:
    X.append(data[:-1])
    labels.append(data[-1])

scaler = MinMaxScaler()
scaler = scaler.fit(X)
X = scaler.transform(X)

X = np.array(X)

y_pred = clf.predict(X)

count = 0

joblib.dump(clf, "phish_model.pkl")

print(len(y_pred))

for oo in y_pred:
    if oo == 1:
        count += 1
print(count)