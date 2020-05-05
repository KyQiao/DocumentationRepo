#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:58:33 2017

@author: kqiao
"""

import numpy as np
import matplotlib.pylab as plt
T = 2.1
exp = 0.013
x = np.linspace(1,3,10000)
y = abs(x - T)**(exp)
plt.plot(x,-y)
plt.show()