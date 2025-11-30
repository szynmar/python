# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:09:07 2025

@author: Ala
"""
import os
import sys
import urllib.request

cwd=os.getcwd()
print(cwd)
dir = os.path.join(cwd, 'strony')
if not os.path.exists(dir):
    print(f"Katalog {dir} nie istnieje, wiec go tworze")
    os.mkdir(dir)

pagesDL = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pagesDL:
    fileName = page['name']+'.html'
    pathStr = os.path.join(dir, fileName)
    page['pathStr']=pathStr
    print(f"{page['name']}: {page['url']}")
    print(f"{page['name']}: {page['pathStr']}")

for page in pagesDL:
    try:
        urllib.request.urlretrieve(page['url'], page['pathStr'])
        print(f"Pobralem {page['name']}")
    except:
        pass
        print(f"Blad dla {page['name']}: {sys.exc_info()}")
