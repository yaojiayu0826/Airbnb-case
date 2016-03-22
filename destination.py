import csv
from collections import Counter
from matplotlib import pyplot as plt

with open('train_users_2.csv','rU') as f:
    reader = csv.reader(f, delimiter = ',')
    reader.next()
    cc = Counter(row[15] for row in reader)


countries = list()
num = list()
for des,count in cc.most_common():
        countries.append(des)
        num.append((count*100.0)/sum(cc.values()))

fig, ax = plt.subplots()
xaxis = [i + 0.1 for i,country in enumerate(countries)]
plt.bar(xaxis,num,0.8)
plt.ylabel("Number of People Visiting Percentage")
plt.xlabel("Destination")
plt.title("Number of People Percentage v.s. Destination")
plt.xticks([i + 0.5 for i,x in enumerate(countries)],countries)
for i, v in enumerate(num):
    ax.text(i + 0.1, v + 0.1, "%.5s" %str(v), color='black')
plt.show()

countries = list()
num = list()
del cc['NDF']
for des,count in cc.most_common():
        countries.append(des)
        num.append((count*100.0)/sum(cc.values()))

fig, ax = plt.subplots()
xaxis = [i + 0.1 for i,country in enumerate(countries)]
plt.bar(xaxis,num,0.8)
plt.ylabel("Number of People Visiting Percentage without NDF")
plt.xlabel("Destination")
plt.title("Number of People Percentage v.s. Destination")
plt.xticks([i + 0.5 for i,x in enumerate(countries)],countries)
for i, v in enumerate(num):
    ax.text(i + 0.1, v + 0.1, "%.5s" %str(v), color='black')
plt.show()
