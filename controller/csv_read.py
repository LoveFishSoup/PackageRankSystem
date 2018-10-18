# -*- coding: utf-8 -*-

"""
Date: 16th, April, 2018
Author: FishSoup
Description:
This file aims to open specific csv file and extract specific data
and classify them into different coloums.
"""
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import decimal

def divide(num, den, prec):
    a = (num*10**prec) / den
    s = str(a).zfill(prec+1)
    return s[0:-prec] + "." + s[-prec:]

def normalisedList(original_list):
    # normalised data set
    list_min = min(original_list)
    list_max = max(original_list)
    #print(pv_min)
    #print(pv_max)
    list_dif = list_max - list_min
    norm_list = []
    for row in original_list:
        num = row - list_min
        n = divide(num, list_dif, 4)
        norm_list.append(n)
    #print(pv_nor)
    return norm_list

# load csv file
with open('E:\Code\packageRankSystem\dataFile\package_day.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    pv = []
    uv = []
    playtime = []
    for row in reader:
        row = np.array(row)
        row = row[4:7]
        pv.append(row[0])
        uv.append(row[1])
        playtime.append(row[2])

        # remove quotation mark
        pv = list(map(int, pv))
        uv = list(map(int, uv))
        playtime = list(map(int, playtime))
        print(pv)
        
pv = np.array(pv)
uv = np.array(uv)
playtime = np.array(playtime)

norm_pv = normalisedList(pv)
#print(norm_pv)
norm_uv = normalisedList(uv)
norm_playtime = normalisedList(playtime)


len_pv = len(pv)
#len_uv = len(uv)
#len_playtime = len(playtime)




'''
# illustrate the result
fig = plt.figure()
plt.subplot(311)
axis_x = np.arange(0,1,1/len_pv)
plt.scatter(axis_x, norm_pv, c='r', marker='*', s=15)
plt.title('normalised pv data')
plt.axis('auto')


plt.subplot(312)
axis_x = np.arange(0,1,1/len_pv)
plt.scatter(axis_x, norm_uv, c='b', marker='*', s=15)
plt.title('normalised uv data')
plt.axis('auto')

plt.subplot(313)
axis_x = np.arange(0,1,1/len_pv)
plt.scatter(axis_x, norm_playtime, c='g', marker='*', s=15)
plt.title('normalised playtime data')
plt.axis('auto')
plt.show()
'''

"""
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


def divide(num, den, prec):
    a = (num*10**prec) // den
    s = str(a).zfill(prec+1)
    return s[0:-prec] + "." + s[-prec:]

def normalisedList(original_list):
    # normalised data set
    list_min = min(original_list)
    list_max = max(original_list)
    #print(pv_min)
    #print(pv_max)
    list_dif = list_max - list_min
    norm_list = []
    for row in original_list:
        num = row - list_min
        n = divide(num, list_dif, 4)
        norm_list.append(n)
    #print(pv_nor)
    return norm_list


# load csv file
with open('E:\Code\packageRankSystem\dataFile\package_day.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    pv = []
    uv = []
    playtime = []
    for row in reader:
        row = np.array(row)
        row = row[4:7]
        pv.append(row[0])
        uv.append(row[1])
        playtime.append(row[2])

        # remove quotation mark
        pv = list(map(int, pv))
        uv = list(map(int, uv))
        playtime = list(map(int, playtime))
        
pv = np.array(pv)
uv = np.array(uv)
playtime = np.array(playtime)

#norm_pv = normalisedList(pv)

len_pv = len(pv)
y = np.zeros((len_pv))

#fig = plt.figure()
#plt.subplot(311)
n, bins, patches = plt.hist(pv, 100, normed=1, facecolor='g', alpha=0.75)
plt.hist(pv, bins=10, color='steelblue', normed=True )
sns.distplot(pv, rug=True)
#plt.axis([-2,2,0,1])
plt.axis('auto')
plt.show()

#plt.hist(pv, bins = 50, color='steelblue', normed=True)

'''
pv_max = max(pv)
pv_min = min(pv)
pv_range = pv_max - pv_min
len_pv = len(pv)
print("pv length is:", len_pv)
pv_interval = int(pv_range/5)
pv_rest = pv_range%5

if  pv_rest > 2:
    pv_interval = pv_interval + 1
print(pv_interval)
A=0
B=0
C=0
D=0
E=0

for row in pv:
    if row < pv_interval:
        E=E+1
        #print(row)
    elif row < pv_interval*2:
        D=D+1
    elif row < pv_interval*3:
        C=C+1
    elif row < pv_interval*4:
        B=B+1
    else:
        A=A+1

print(A)
print(B)
print(C)
print(D)
print(E)

Rank_pv = A*5/len_pv + B*4/len_pv + C*3/len_pv + D*2/len_pv + E*1/len_pv
print(Rank_pv)

'''







"""
