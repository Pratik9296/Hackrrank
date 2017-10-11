'''
Created on 11-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def solve(n, data):
    # Complete this function
    if(p>n//2):
        if(n%2==0):
            n+=1
        count=(n-p)//2
    else:
        count=p//2
    return count            

n = int(raw_input().strip())
p = raw_input().strip()
result = solve(n, p)
print(result)
