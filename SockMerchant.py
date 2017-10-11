'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    count=0
    set1=set(ar)
    for el in set1:
        maxcount=ar.count(el)
        maxcount//=2
        count=count+maxcount
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
