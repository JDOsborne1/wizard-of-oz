# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:36:14 2017

@author: Joe
"""

import csv
import matplotlib.pyplot as plt
import math
import statistics as stat

##Opening and floating data
cur = []
intensity = []   
   
numcur = []
numint = []
#opening Data
with open("C:\\Users\\Joe\\Documents\\Year 3 Labs\\Laser Diode\\Current Intensity at 16C.txt", 'r') as f:
    file_reader = csv.reader(f, delimiter ='\t')
    for line in file_reader:
        cur.append(line[0])
        intensity.append(line[1:])
#
#floating data  
for i in range(len(cur[1:])):
    numcur.append(float(cur[i+1]))
    inttrack = []
    for j in intensity[i+1]:
        inttrack.append(float(j))
    numint.append(inttrack)
#    
##    
##determining and plotting raw errors
meanint = []

interr = []

newmeanint = []
newinterr = []
#averaging data
for i in numint:
    meanint.append(stat.mean(i))
#
#getting SEM
for i in numint:
    interr.append(stat.stdev(i)/math.sqrt(len(i)))
#
#Normalising
for i,j in zip(meanint,interr):
    a = max(meanint)
    newmeanint.append(i/a)
    newinterr.append(j/a)
#
#Plotting
plt.errorbar(numcur, newmeanint, newinterr, fmt='.',label = 'Diode at constant 16°C')
plt.xlabel('Current [mA]')
plt.ylabel('Normalised Intensity')
plt.title('Graph of Intensity vs Current')
#
##


#
##
##fitting
from scipy.optimize import curve_fit
import numpy as np

def fitFunction(t, a, b):
    return a*t + b
#Getting gradient and intercept of straight line part of graph
fitParameters, fitCovariances = curve_fit(fitFunction, ncurr, nintensity, sigma = nintensityerr, absolute_sigma =True)
parameternames = ['Gradient', 'Intercept']
for i in range(len(fitParameters)):
    print('Parameter {0} = {1} ± {2}'.format(parameternames[i],fitParameters[i],fitCovariances[i][i]))
#
#graphing the straight line made by fit
nnc=np.array(nc)
yval=fitFunction(nnc,fitParameters[0],fitParameters[1])
plt.plot(nnc,yval)
xint=-fitParameters[1]/fitParameters[0]
print(xint)
g,h,j,k = fitCovariances[1][1], fitParameters[1], fitCovariances[0][0], fitParameters[0]
for i in [g,h,j,k]:
    i = float(i)
dxint = xint*pow(pow(g/i,2)+pow(j/k,2),1/2)


plt.plot(np.full(10,xint),np.linspace(0,1,10),linestyle='dashed',label='Intercept at {0} ± {1}mA for 16°C'.format(round(xint,2),round(dxint,2)))
#
plt.legend(loc=2,fontsize='x-small')
plt.show()
##
import numpy as np
import csv
import matplotlib.pyplot as plt
import peakutils

wave = []
inte = []

with open("C:\\Users\\Joe\\Documents\\Year 3 Labs\\Laser Diode\\sun rect.txt", 'r') as f:
    file_reader = csv.reader(f, delimiter ='\t')
    for line in file_reader:
        try:
            inte.append(line[1])
            wave.append(line[0])
        except IndexError:
            pass 

numinte = []
numwave = []       
for i in inte:
    numinte.append(float(i))     
for i in wave:
    numwave.append(float(i))

norminte = []
a = max(numinte)
for i in numinte:
    norminte.append(i/a)
npnumwave = np.array(numwave)
npnorminte = np.array(norminte)    
#peaks

maxima = peakutils.indexes(npnorminte,thres=0.3,min_dist=10)
print(npnumwave[maxima][0])
vert = np.linspace(0,1,1000)
for i in range(len(maxima)):
    plt.plot(np.full(1000,npnumwave[maxima][i]),vert,label='Peak at {0} nm'.format(npnumwave[maxima][i]))
#

plt.plot(npnumwave, npnorminte, '.')
plt.xlabel('Wavelength [nm]')
plt.ylabel('Normalised Intensity')
plt.title('Wavelength - Intensity relation of Sunlight')
plt.legend(loc=0,fontsize='x-small')
plt.grid(b=True, which='major',axis = 'x', color='b', linestyle='-')
plt.grid(b=True, which='minor',axis = 'x', color='r', linestyle='--')
plt.minorticks_on()
plt.show()#add in straight line fitting

#plotting fit
ntemp = np.array(numtemp)
yval=fitFunction(ntemp,fitParameters[0],fitParameters[1])
plt.plot(ntemp,yval)