#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:18:32 2017

@author: kqiao
"""

import random as ra
import matplotlib.pyplot as plt

def dis(x,y):
    return x**2+y**2
def sign(x):
    return x/abs(x) 
delta = 0.1
trail_n = 40000
hit_n = 0
x,y = 0,0
x1,y1 = [],[]
for i in range(trail_n):
    dx ,dy = ra.uniform(-delta,delta),ra.uniform(-delta,delta)
#    if abs(x+dx)<1 and abs(y+dy)<1:
#        x += dx
#        y += dy

    x += dx
    y += dy
    if abs(x) > 1:
        if sign(x) > 0: x -=2
        else: x += 2
    if abs(y) > 1:
        if sign(y) > 0: y -=2
        else: y += 2
        
    if dis(x,y) < 1:
        hit_n += 1
    x1.append(x)
    y1.append(y)
print(4.0*float(hit_n)/trail_n)
plt.plot(x1,y1,'g-')
plt.show()