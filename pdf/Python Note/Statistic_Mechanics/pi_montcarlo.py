#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:04:48 2017

@author: kqiao
"""

import random as ra

trail_n=40000
hit_n=0
for i in range(trail_n):
    x,y = ra.uniform(-1.0,1.),ra.uniform(-1.0,1.)
    if x**2+y**2 < 1:
        hit_n += 1

print(4.0*hit_n/trail_n)