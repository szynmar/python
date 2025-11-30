# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""
import os

dir = 'C:\\Marcin\\progr\\python\\'
pathStr = dir + 'testowy.txt'

with open(pathStr,'r') as f:
    content = f.read()
    
    print(content)
    

pathStr = dir + 'XXXudemy_k2_s2_13lab_pliki.py'
if os.path.exists(pathStr):
    print(f"--jest plik {pathStr}")
    with open(pathStr, 'r') as f:
        for line in f:
            print(f"{line}")
else:
    print(f"--brak pliku {pathStr}")