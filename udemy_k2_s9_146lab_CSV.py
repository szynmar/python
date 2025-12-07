# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 13:35:01 2025

@author: Ala
"""

import csv
import os
 
fld = os.path.join(os.getcwd(), "udemy_pliki")
with open(os.path.join(fld, "data.csv"), newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #for row in csvreader:
    #    print('|'.join(row))
    
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break
