'''
Created on 11-Aug-2017

@author: pratik
'''
def solve(n,p):
    level=0
    count=0
    flag=True
    for c in p:
        if(c=='U'):
            level=level+1
            if(level==0):
                count+=1
        elif(c=='D'):
            level-=1      
    return count-1          
n=int(raw_input().strip())
p=raw_input().strip()
result=solve(n,p)
print result