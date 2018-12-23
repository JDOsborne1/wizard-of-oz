# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:42:27 2017

@author: Joe
"""
##imports
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
##defines
def get(St,Ty):
    if Ty == "int":
        try:
            Va = int(input(St) )
            return Va
        except ValueError:
            return get(St,Ty)
    elif Ty == "float":
        try:
            Va = float(input(St) )
            return Va
        except ValueError:
            return get(St,Ty)

def fitFunction(t, a, b):
    return a*t + b
#labels
_label = input("Graph Name >")
xquantity = input("Quantity on the X-axis >")
yquantity = input("Quantity on the Y-axis >")
xunits = input('Units of {0} >'.format(xquantity))
yunits = input('Units of {0} >'.format(yquantity))
plt.xlabel('{0} / {1}'.format(xquantity,xunits))
plt.ylabel('{0} / {1}'.format(yquantity,yunits))


x_values = []
y_values = []
y_error_values = []
x_error_values = []

##csv reading
read = input('would you like to read from a csv file? Y/N')
if read == 'Y':
    with open("C:\\Users\\Joe\\OneDrive\\Documents\\PythonLibrary\\dampedsindata.csv",'r') as f:
        file_reader = csv.reader(f,delimiter = ',')
        for line in file_reader:
            if len(line) == 4:
                x, y, xerr, yerr = map(float, line) ### maps the function float to each string in the line
                x_values.append(x)
                y_values.append(y)
                x_error_values.append(xerr)
                y_error_values.append(yerr)
else:
    pass

##manual data input
datain = input('would you like to manually input data? Y/N')
if datain == 'Y':
    state = 0
    while state != "fin":
        x = get("X value := ","float")
        y = get("Y value := ","float")
        xerr = get("X error value :=","float")
        yerr = get("Y error value :=","float")
        state = input("fin to finish")
        x_values.append(x)
        y_values.append(y)
        x_error_values.append(xerr)
        y_error_values.append(yerr)
else:
    pass

##sorting code
sort = input('would you like to sort the data Y/N')
if sort == 'Y':
    combi_values = []
    a = len(x_values)
    for i in range(a):
        combi_values.append([x_values[i],y_values[i],x_error_values[i],y_error_values[i]])
        def getkey(item):
            return item[0]### change this to 1 to sort by y values
    combi_values.sort(key = getkey)
    x_values = []
    y_values = []
    y_error_values = []
    x_error_values = []
    for i in range(a):
        x_values.append(combi_values[i][0])
        y_values.append(combi_values[i][1])
        x_error_values.append(combi_values[i][2])
        y_error_values.append(combi_values[i][3])
else:
    pass
   
##fitting
fitParameters, fitCovariances = curve_fit(fitFunction, x_values,y_values)
for i in range(len(fitParameters)):
    print('Parameter {0} = {1} ± {2}'.format(i+1,fitParameters[i],fitCovariances[i][i]))
x_fit_values = np.array(x_values)
y_fit_values = fitFunction(t = x_fit_values,
                           a = fitParameters[0],
                           b = fitParameters[1]
                           )
plt.plot(x_fit_values,
         y_fit_values,
         label='fitting curve for {0} against {1}'.format(xquantity,yquantity),
         linestyle = 'solid'
         )
#graphing
plt.errorbar(x_values, y_values,
             y_error_values,x_error_values,
             fmt = '',label = _label,
             linestyle='None'
             )
plt.axis([-1+min(x_values),1+max(x_values),-1+min(y_values),1+max(y_values)])
plt.legend(loc=0)
plt.show()


