#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:08:15 2017

@author: kqiao
"""

import matplotlib.pylab as plt
import numpy as np
n = 2
x = np.linspace(-10,10,1000)
y = x%n

plt.plot(x,y)
plt.show()