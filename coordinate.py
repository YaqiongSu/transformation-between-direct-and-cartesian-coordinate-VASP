# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:07:58 2019

@author: Yaqiong Su
"""

import numpy as np
import pandas as pd
import linecache as lc

f1 = open('POSCAR','rb')
f2 = open('head','wb')
f3 = open('direct','wb')
f4 = open('lattice','wb')

i = 0
while True:
    line = f1.readline()
    i+=1
    if i < 7:
        f2.write(line)
    if i == 7:
        f2.write('Cartesian \n')
    if i > 8:
        f3.write(line)
    if i > 300:
        break
f1.close()
f2.close()
f3.close()
with open('head','rb') as f22:
    i = 0
    while True:
        line = f22.readline()
        i+=1
        if i> 2 and i < 6:
            f4.write(line)
        if i > 300:
            break
f4.close()
    
#with open('matrix','rb') as f33:
#    for data in f33.readlines():
#        data = data.strip('\n')
#        nums = data.split()
#        nums = [float(x) for x in nums]
#        direct = np.array(nums)
#        print direct
direct = np.loadtxt('direct')
print "direct coordinate"
print  direct
lattice = np.loadtxt('lattice')
print "lattice"
print  lattice
cartesian = np.dot(direct,lattice)
print"cartesian coordinate"
print cartesian
np.savetxt('cartesian',cartesian)

f5 = open('Cartesian_POSCAR','ab')
with open('head','rb') as f:
    for lines in f.readlines():
        f5.write(lines)
with open('cartesian','rb') as f0:
    for lines in f0.readlines():
        f5.write(lines)
f5.close()
print "Cartesian_POSCAR"
with open('Cartesian_POSCAR','rb') as f:
    for lines in f.readlines():
        print lines

          

