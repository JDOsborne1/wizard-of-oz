# -*- coding: utf-8 -*-
"""

"""

##opening the csv file
#extracts the name and the co-ordinates
##
'''This whole following segment would be easier in sql, but what the hell'''
##extracts an exclusive list of the types of shop
shoptypes=[]
for i in shops:
    if i[0] not in shoptypes:
        shoptypes.append(i[0])
    else:
        pass
##
##slicing the data into seperated lists depending on the shoptype
seperatedshops = []
for i in shoptypes:
    seperatedshops.append([j for j in shops if j[0]==i])
##
''''''
##functional definition of plotting
#arguments taken are the shoptype
#may need to include fixed axis dimesions for ease of comparison
def ploto(name):
    
    

##

##iterating the plotting over each of the shoptypes
for s in shoptypes:

##