#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###========+=========+=========+=========+=========+=========+=========+=
## PROGRAM : pocket_disks.py
## PURPOSE : implement SMAC algorithm 2.18 (hard-sphere-cluster) 
##           for four disks in a square of sides 1
## LANGUAGE: Python 2.5
##========+=========+=========+=========+=========+=========+=========+
from random import uniform as ran, choice
def box_it(x):
   x[0]=x[0]%1.
   if x[0] < 0 : x[0]=x[0]+1
   x[1]=x[1]%1.
   if x[1] < 0 : x[1]=x[1]+1
   return x
def dist(x,y):
   d_x= abs(x[0]-y[0])%1
   d_x = min(d_x,1-d_x)
   d_y= abs(x[1]-y[1])%1
   d_y = min(d_y,1-d_y)
   return  d_x**2 + d_y**2
def T(x,Pivot):
   x=(2*Pivot[0]-x[0],2*Pivot[1]-x[1])
   return x
#
# Program starts here
#
Others=[(0.25,0.25),(0.25,0.75),(0.75,0.25),(0.75,0.75)]
sigma_sq=0.15**2
for iter in range(10000):
   a = choice(Others)
   Others.remove(a)
   Pocket = [a]
   Pivot=(ran(0,1),ran(0,1))
   while Pocket != []:
      a = choice(Pocket)
      Pocket.remove(a)
      a = T(a,Pivot)
      for b in Others[:]:  # "Others[:]" is a copy of "Others"
         if dist(a,b) < 4*sigma_sq:
            Others.remove(b)
            Pocket.append(b)
      Others.append(a)
print(Others, ' ending config ')