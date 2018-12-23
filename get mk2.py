# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:57:05 2017

@author: Joe
"""

def get(string,bounds):
    if bounds == "int":
        try:
            return int(input(string))
        except ValueError:
            return get(string,bounds)
    if bounds == "number":
        try:
            return float(input(string))
        except ValueError:
            return get(string,bounds)
    else:
        value = input(string)
        if value in bounds:
            return value
        else:
            return get(string,bounds)
        
a = get("gimme a:",["1","3","7"])
print(a)