# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:23:39 2017

@author: Joe
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
##defines 
def an_(n):
    return (pow(-1,n)-1)/pow(n,2)
def bn_(n):
    return pow(-1,n)*(-1/n)
a0_ = 3.1415/2
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
        
## generalises the number of sin waves generated and summed, this can be seperated
## in order to sum less waves than are generated
n=400
## creates the linespace
x_values = np.linspace(-10,10,1000)
x_array = np.array(x_values)

## using the linespace and the iteration number, generates the sine waves
listo=[]
for i in range(1,n+1):
    listo.append(a0_ + an_(i)*sp.sin(x_array*i)+bn_(i)*sp.cos(x_array*i))
 

##tests the matrix summing algorith with the generated sine waves
plt.plot(sum_arrays(listo,n,np.zeros(len(listo[0]))))