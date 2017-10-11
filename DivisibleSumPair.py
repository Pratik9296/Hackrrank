'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    counter=0
    for index in range(0,n-1):
        for index2 in range(index+1,n):
            sum=ar[index]+ar[index2]
            if(sum%k==0):
                counter+=1
    return counter            

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
