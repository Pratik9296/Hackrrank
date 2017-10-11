'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    sum=0
    for index in range(n):
        if(index!=k):
            sum=sum+ar[index]
    share=sum//2 
    if(share==b):
        return "Bon Appetit"
    else:
        return b-share       
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
