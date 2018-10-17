'''
Date: 16th, April, 2018
Author: FishSoup
'''
# _*_ coding: utf-8 _*_

import numpy as np
import pandas as pd
import csv

date = []
package_series = []
package_id = []
pv =[]
uv =[]
playtime =[]

with open('E:\Code\packageRankSystem\dataFile\package_day.csv', newline='') as csvfile:
    # reader = csv.DictReader(csvfile)
    reader = csv.reader(csvfile)
    # reader = np.array(reader)
    for row in reader:
        row = np.array(row)
        row = row[0:7]
        print(row)
    # date, cid, gid, buydevice, pv, uv, play_time, *no_use = reader
    # print(*no_use)
        y = np.transpose(row)
        y = row.reshape(len(row), 1)
        print(y)
        date.append(y[0])
        package_series.append(y[1])
        package_id.append(y[2])
        pv.append(y[4])
        uv.append(y[5])
        playtime.append(y[6])
