'''
Created on 23-Aug-2017

@author: pratik
'''

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
E=100
c = map(int,raw_input().strip().split(' '))
for i in range(k,n+1,k):
    if(i==n):
        if(c[0]==0):
            E=E-1
        else:
            E=E-3    
    elif(c[i]==0 and i !=n):
        E=E-1
    else:
        E=E-3
    print i,E    
print E            
    