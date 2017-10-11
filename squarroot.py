'''
Created on 24-Aug-2017

@author: pratik
'''
import math
n=int(raw_input().strip())
for i in range(n):
    a,b=raw_input().strip().split(' ')
    a,b=[int(a),int(b)]
    count=0
    while(a<=b):
        sq=math.sqrt(a)
        if(sq-math.floor(sq)==0):
            count+=1    
            flag=True
            break
        else:
            a=a+1
    index=math.sqrt(a)       
    index=index+1
    a=index**2      
    while(a<=b):
        count+=1
        index+=1
        a=index**2
    print count            