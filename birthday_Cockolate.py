'''
Created on 10-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    index=0
    counter=0
    if(n==1 and m==1):
        if(s[0]==d):
            counter=1
    else:        
        while(index<n-m):
            sum,index2,temp=(0,0,index)
            while(index2<m):
                #print s[index],
                sum=sum+s[index]
                index+=1
                index2=index2+1 
            #print    
            #print sum       
            if(sum==d):
                counter=counter+1    
            index=temp+1 
            #print "index:",index   
    return counter        

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
