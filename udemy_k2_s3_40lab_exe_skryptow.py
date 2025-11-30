# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""
import os
import sys
import urllib.request

pliki = os.listdir()
for i in range(len(pliki)):
    print(f"i={i} : {pliki[i]}")
    

nr = input('Wybirz nr pliku: ')
plik = pliki[int(nr)]
print(plik)

with open(plik,'r') as f:
    content = f.read()
    
    exec(content)
