# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:51:56 2017

@author: Joe
"""

import numpy as np
import matplotlib.pyplot as plt

def inflating_frac(init_num,init_den,incr,limit):
    fractions = []
    for i in range(limit):
        new_frac = (init_num + (incr*i))/(init_den + (incr*i))
        fractions.append(new_frac)
    x_values = np.linspace(0,incr,limit)
#    print(len(fractions))
#    print(len(x_values))
    plt.plot(x_values,fractions)
#    print(fractions)
for j in range(100):
    inflating_frac(j,10000,1,200000)
plt.show()

   