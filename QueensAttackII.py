'''
Created on 18-Aug-2017

@author: pratik
'''
#!/bin/python

import sys

def leftCount(rObstacle,cObstacle,rQueen,cQueen,n):
    #print "lllllllllllllllllllllllllllllll"
    #print rObstacle," ",cObstacle
    count=0
    if(rObstacle==rQueen and cQueen>cObstacle):
        count=cQueen-cObstacle-1
        #print count
    else:
        count=cQueen-1
        #print "else first "
        #print count
    temp=cQueen-1
    temp1=n-rQueen
        #print temp,temp1,"temps"
    if(temp<temp1):
        leftUpGo=temp
    else:
        leftUpGo=temp1
    #print "left Up Go",leftUpGo    
    for i in range(leftUpGo):
        if(rObstacle==rQueen+i+1 and cObstacle==cQueen-i-1):
            break
        else:
            count+=1
    #print "else second"
    #print count           
    temp2=rQueen-1   
    if(temp<temp2):
        leftDownGo=temp
    else:
        leftDownGo=temp2  
    #print "leftDownGo",leftDownGo
    for i in range(leftDownGo):
        if(rObstacle==rQueen-i-1 and cObstacle==cQueen-i-1):
            break
        else:
            count+=1
    #print "else Third"
    #print count       
    #print "before Return",count    
    return count        

def rigthSide(rObstacle,cObstacle,rQueen,cQueen,n):
    #print "rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"
    #print rObstacle," ",cObstacle
    count=0
    if(rObstacle==rQueen and cQueen<cObstacle):
        count=cObstacle-cQueen-1
        #print count
    else:
        count=n-cQueen
        #print "else first "
        #print count
    temp=n-cQueen
    temp1=n-rQueen
        #print temp,temp1,"temps"
    if(temp<temp1):
        leftUpGo=temp
    else:
        leftUpGo=temp1
    #print "left Up Go",leftUpGo    
    for i in range(leftUpGo):
        if(rObstacle==rQueen+i+1 and cObstacle==cQueen+i+1):
            break
        else:
            count+=1
    #print "else second"
    #print count           
    temp2=rQueen-1   
    if(temp<temp2):
        leftDownGo=temp
    else:
        leftDownGo=temp2  
    #print "leftDownGo",leftDownGo
    for i in range(leftDownGo):
        if(rObstacle==rQueen-i-1 and cObstacle==cQueen+i+1):
            break
        else:
            count+=1
    #print "else Third"
    #print count       
    #print "before Return",count    
    return count       

def Up_and_down_count(rObstacle,cObstacle,rQueen,cQueen,n):
    #print "U/D------------------------"
    count=0
    if(cQueen==cObstacle):
        if(rObstacle<rQueen):
            count+=rQueen-rObstacle-1
            count+=n-rQueen
        else:
            count+=rObstacle-rQueen-1
            count+=rQueen-1    
    
    else:
        count+=rQueen-1+n-rQueen
    return count
n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
left=[]
right=[]
colCount=[]
if(k==0):
    left.append(leftCount(n+1, n+1, rQueen, cQueen, n))
    right.append(rigthSide(n+1, n+1, rQueen, cQueen, n))
    colCount.append(Up_and_down_count(n+1, n+1, rQueen, cQueen, n))
for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    #print "rObstacle",rObstacle
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    count=leftCount(rObstacle,cObstacle,rQueen,cQueen,n)
    left.append(count)
    count=rigthSide(rObstacle, cObstacle, rQueen, cQueen, n)
    right.append(count)
    count=Up_and_down_count(rObstacle, cObstacle, rQueen, cQueen, n)
    colCount.append(count)
    #print "+++++++++++++++++++"
    
print min(left)+min(right)+min(colCount)