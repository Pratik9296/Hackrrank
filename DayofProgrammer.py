'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def solve(year):
    leap_date=12
    mm='09'
    non_leap_date=13
    if(year>=1700 and year<=1917):
        if(year%4==0):
            date="{}.{}.{}".format(leap_date,mm,year)
        else:
            date="{}.{}.{}".format(non_leap_date,mm,year)   
    elif(year==1918):
        if(year%4==0):
            date="{}.{}.{}".format(leap_date+13,mm,year)
        else:
            date="{}.{}.{}".format(non_leap_date+13,mm,year)
    else:
        if(year%400==0  or(year%4==0 and year%100!=0)):
            date="{}.{}.{}".format(leap_date,mm,year)
        else:
            date="{}.{}.{}".format(non_leap_date,mm,year)    
    return date        
year = int(raw_input().strip())
result = solve(year)
print(result)
