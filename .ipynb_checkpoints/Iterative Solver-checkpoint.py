# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from time import sleep
def f(x):
    y = 3*(1-np.exp(-1*x))
    return y
x=float(3)
end = 0
precision = 0.000001
while end != 1:
    dummy = x
    print(x)
    x=f(x)
    if dummy - x < precision:
        end = 1
    sleep(0.5)
