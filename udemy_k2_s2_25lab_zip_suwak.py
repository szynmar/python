# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

resList = list(zip(projects, leaders))

print(f"res: {resList}")
for p, l in resList:
    print(f"The leader of {p} is {l}")
    
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
enDates = list(enumerate(dates))

for i,d in enDates:
    print(f"{i}: {d}")
    
for i, (p,l) in enumerate(resList):
    print(f"{i}: {p} -> {l}")

for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print(f"{i} The leader of {p} started {d} is {l}")