# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""

coinsList = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 
                   1, 2, 5, 10, 20, 50, 100, 200, 500]
print(coinsList)
cntList = []
for i in range(0, len(coinsList)):
    cntList.append(0)
    
print(cntList)

dictB = dict(zip(coinsList, cntList))
#dodatkowy element
dictB[-1]=0
dictB[-2]=6

print(dictB)

dictB[100] += 1
dictB[20] += 1
dictB[5] += 1
dictB[0.5] += 1
 
dictB[50] += 1
dictB[20] += 2
dictB[5] += 1
dictB[2] += 2
 
dictB[100] += 1
dictB[50] += 1
dictB[2] += 1

for k in dictB:
    cnt = dictB[k]
    if cnt > 0:
        print(f"{k} -> {cnt}")