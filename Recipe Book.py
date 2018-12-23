# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 17:27:11 2018

@author: pi
"""
import pandas as pd
d = {'pasta /g':[400], 'Onion (whole)':[1],'Garlic /cloves':[3],'Tuna /g':[400],'Tomatoes /g':[400]}
df = pd.DataFrame(data=d,index=['Tuna Pasta Bake'])
intro = pd.DataFrame(data={'Garlic /cloves':[3],'Rice /g':[200],'Spring onion (whole)':[3],'Eggs':[2],'Chilli':[1],'Squash':[1],'Chickpeas /g':[400]},index=['Spicy Chickpea and Squash soup'])
df.append(intro)
