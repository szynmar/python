# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""
import os

folder = 'C:\\Marcin\\progr\\python\\'
p = folder + 'testowy.txt'

with open(p,'r') as f:
    content = f.read()
    
    print(content)
    

p = folder + 'XXXudemy_k2_s2_13lab_pliki.py'
if os.path.exists(p):
    print(f"--jest plik {p}")
    with open(p, 'r') as f:
        for line in f:
            print(f"{line}")
else:
    print(f"--brak pliku {p}")