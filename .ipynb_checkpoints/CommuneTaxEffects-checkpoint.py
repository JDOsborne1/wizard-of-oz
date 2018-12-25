# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:06:32 2017

@author: Joe
"""
import numpy as np
#model of the taxation changes when wealth is pooled and averaged, currently only 
#considering income tax on basic employment income

#incomes = [50,50,50,50]

incomes_i = []
for i in range(1,250):
    incomes_i.append(i)    
#print(incomes_i)
incomes1 = incomes_i

# incomes in thousands of £ per year
def taxation(incomes):
#incomes expected as a list

#taxing process
    band0 = []
    band1 = []
    band2 = []
    band3 = []

    for i in incomes:
        if i - 11.5 < 0:
            band0.append(i)
            band1.append(0)
            band2.append(0)
            band3.append(0)
            continue
        elif i - 45 < 0:
            band0.append(11.5)
            band1.append(i-11.5)
            band2.append(0)
            band3.append(0)
            continue
        elif i - 150 < 0:
            band0.append(11.5)
            band1.append(33.5)
            band2.append(i-45)
            band3.append(0)
            continue
        else:
            band0.append(11.5)
            band1.append(33.5)
            band2.append(105)
            band3.append(i-150)
#print(band0,band1,band2,band3)
    band_allowance = np.array(band0)
    band_basic = np.array(band1)
    band_higher = np.array(band2)
    band_additional = np.array(band3)


    taxed_income = band_allowance*0 + band_basic*0.2 + band_higher*0.4 + band_additional*0.45
    gross_income = np.array(incomes)
    return gross_income,taxed_income

print("sum taxed income from all individuals",sum(taxation(incomes1)[1]))
print('gross income',taxation(incomes1)[0]) 
print('breakdown of taxed income',taxation(incomes1)[1])
print('percentage of income lost as tax',100*taxation(incomes1)[1]/taxation(incomes1)[0])

#conclusion so far is that the commune tax system is only tax efficient for the 
#individuals when there is a high incedence of people with low or very low income
#a situation which, when genuine, the government ought to be satisfied with.


import matplotlib.pyplot as plt

plt.plot(taxation(incomes1)[0],taxation(incomes1)[1],xlabel = "Gross Income")
#plt.legend(loc=0)
plt.show()
#plt.plot(taxation(incomes1)[0],(100*taxation(incomes1)[1]/taxation(incomes1)[0]),xlabel='Gross Income',ylabel='Percentage of income taken as tax')
#plt.legend(loc=0)
#plt.show()

