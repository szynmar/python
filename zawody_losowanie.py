# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:48:16 2025

@author: Ala
"""
import random

maxLos1 = 5
maxLos2 = 10
pktZ1 = 0
pktZ2 = 0
suma1=0
suma2=0
i=0
iMax=100000

while i < iMax:
    losZ1=random.randint(0, maxLos1)
    suma1=suma1+losZ1
    losZ2=random.randint(0, maxLos2)
    suma2=suma2+losZ2

    info = "  Remis"
    if losZ1 > losZ2:
        pktZ1 += 1
        info = f"  Runde nr {i} wgral zawodnik nr 1"
    elif losZ1 < losZ2:
        pktZ2 += 1
        info = f"  Runde nr {i} wygral zawodnik nr 2"

    if i % int(0.1*iMax) == 0:
        print(info)

    i+=1

print("-"*20)
print(f"wynik Z1<->Z2: {pktZ1} <-> {pktZ2}")

if pktZ1 > pktZ2:
    print(f"Mecz wgral zawodnik nr 1 ")
elif pktZ1 < pktZ2:
    print(f"Mecz wygral zawodnik nr 2 ")
else:
    print(f"Remis ")

print(f"Srednia zawaodnika nr 1 {suma1/i}, a srednia zawodnika nr 2 {suma2/i}")
print(f"czyli zawodnik nr 2 mial srednia {suma2/suma1} razy wieksza")
    
def nextRandInt():
    yield random.randint(1,100);

print(next(nextRandInt()))

for i in range(10):
    print(next(nextRandInt()))