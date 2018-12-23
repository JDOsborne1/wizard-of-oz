# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:22:29 2018

@author: Joe
"""
import matplotlib.pyplot as plt
def taxbasic(income,baseratecut,baserate):
    takehome = baseratecut+((1 - baserate)*(income - baseratecut))
    return takehome
def inversetaxbasic(takehome,baseratecut,baserate):
    income = baseratecut+ ((1/(1-baserate))*(takehome-baseratecut))
    return income
br = 0.2
brc= 11850
   
set1=[]
a=10
b=35
locales=['Bristol','London','Manchester','Birmingham','Swansea']
localemult=[1,1.41,0.957,0.883,0.913]
for j in locales:
    set1=[] 
    for i in range(a,b):
       set1.append(inversetaxbasic(localemult[locales.index(j)]*taxbasic(i*1000,brc,br),brc,br))
    plt.plot([i*1000 for i in range(a,b)],set1,label=j)
plt.legend(loc=0)
plt.show()