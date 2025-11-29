# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:48:16 2025

@author: Ala
"""
import random

maxLos = 5
pktZ1 = 0
pktZ2 = 0
for i in range(10):
    losZ1=random.randint(0, maxLos)
    losZ2=random.randint(0, maxLos)
    print(f"- Wylosowano {losZ1} i {losZ2}")
    
    if losZ1 > losZ2:
        pktZ1 += 1
        print(f"  Runde nr {i} wgral zawodnik nr 1")
    elif losZ1 < losZ2:
        pktZ2 += 1
        print(f"  Runde nr {i} wygral zawodnik nr 2")
        
print(f"wynik Z1<->Z2: {pktZ1} <-> {pktZ2}")
    
        
if pktZ1 > pktZ2:
    print(f"Mecz {i} wgral zawodnik nr 1")
elif pktZ1 < pktZ2:
    print(f"Runde nr {i} wygral zawodnik nr 2")
else:
    print("Remis")
    
