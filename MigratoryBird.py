'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    count=-1
    set1=set(ar)
    output=ar[0]
    for el in set1:
        maxcount=ar.count(el)
        if(maxcount>count):
            count=maxcount
            output=el
    return output        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)