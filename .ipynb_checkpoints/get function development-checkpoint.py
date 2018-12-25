# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:57:05 2017

@author: Joe
"""

def get(string,numtype,bounds):
    try:
        value = float(input(string))  
    except ValueError:
        return get(string,numtype,bounds)
    if value in bounds:
        return value
    else:
        return get(string,numtype,bounds)
a = get("gimme a:","number",[0,1,22])
print(a)