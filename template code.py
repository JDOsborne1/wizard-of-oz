# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:45:56 2017

@author: Joe
"""

'''Generic template, and testing'''
###imports
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

###defines
def an_(n):
    return 1/(n+1)
def bn_(n):
    return 2**n
## defines a generalised matrix summing algorithm
def sum_arrays(x,n,placeholder):
    '''x is expected to be a list of arrays to be summed, 
    and n is expected to be the index of the sum
    and placeholder is expected to be the relevant zero matrix'''
    for i in range(0,n):
        placeholder = placeholder + x[i]
    return placeholder
def kronecker_delta(m,n):
    if m == n:
        return 1
    else:
        return 0
def reverse_kronecker_delta(m,n):
    if m == n:
        return 0
    else:
        return 1


###test code