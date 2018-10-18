# -*- coding: utf-8 -*-

"""
Date: 17th, Oct, 2018
Author: FishSoup
Description:
"""

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

def divide(num, den, prec):
    a = (num*10**prec) // den
    s = str(a).zfill(prec+1)
    return s[0:-prec] + "." + s[-prec:]

# Data Normalisation
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
#with open('E:\\Code\\packageRankSystem\\dataFile\\xuetang_rank_check.csv', newline='', encoding = 'gbk') as csvfile:
with open(r'E:\Code\packageRankSystem\dataFile\xuetang_rank_check.csv', newline='', encoding = 'utf-8') as csvfile:
    reader = csv.reader(csvfile)
    pv = []
    uv = []
    playtime = []
    gid = []
    for row in reader:
        #print(row)
        row = np.array(row)
        row = row[2:6]
        gid.append(row[0])
        pv.append(row[1])
        uv.append(row[2])
        playtime.append(row[3])

# remove quotation mark
gid = list(map(int, gid))
pv = list(map(int, pv))
uv = list(map(int, uv))
playtime = list(map(int, playtime))
#print(playtime)

# data Normalisation
norm_pv = normalisedList(pv)
print(norm_pv)
norm_uv = normalisedList(uv)
norm_playtime = normalisedList(playtime)

# remove quotation mark
norm_pv = list(map(float, norm_pv))
norm_uv = list(map(float, norm_uv))
norm_playtime = list(map(float, norm_playtime))

ceil_pv = []
ceil_uv = []
ceil_playtime = []
# number multiuple 100 and ceil
for i in norm_pv:
    i = math.ceil(i*100)
    ceil_pv.append(i)
# print(ceil_pv)

for i in norm_uv:
    i = math.ceil(i*100)
    ceil_uv.append(i)
print(ceil_uv)

for i in norm_playtime:
    i = math.ceil(i*100)
    ceil_playtime.append(i)
print(ceil_playtime)

matrix_three = np.array([ceil_pv,ceil_uv,ceil_playtime])

matrix_three = matrix_three.T
basic_data = pd.DataFrame(matrix_three)
print(matrix_three)

score = []
# for items in basic_data.iterrows():
#     # items = np.array(items)
#     print(items[0],items[1],items[2])
    # it_pv = items[0]
    # it_uv = items[1]
    #it_dur = items[2]
    # single_score = 0.3*it_pv + 0.3*it_uv + 0.4*it_dur
    # single_score = 0.3*items[0] + 0.3*items[1] + 0.4*items[2]
    # score = score.append(single_score)

# print(score)
# illustration

plt.subplot(311)
plt.bar(range(len(gid)), ceil_pv,color = 'b', tick_label=gid)
#plt.show()

plt.subplot(312)
plt.bar(range(len(gid)), ceil_uv,color = 'r', tick_label=gid)
#plt.show()

plt.subplot(313)
plt.bar(range(len(gid)), ceil_playtime,color = 'g', tick_label=gid)
plt.show()
