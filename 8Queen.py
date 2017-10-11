'''
Created on 18-Aug-2017

@author: pratik
'''
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

"""left=(rQueen,1)
right=(rQueen,n)
up=(n,cQueen)
down=(1,cQueen)
leftUp=(rQueen+min(cQueen-1,n-rQueen),cQueen-min(cQueen-1,n-rQueen))
rigthUp=(rQueen+min(n-cQueen,n-rQueen),cQueen+min(n-cQueen,n-rQueen))
leftDown=(rQueen-min(cQueen-1,rQueen-1),cQueen-min(cQueen-1,rQueen-1))
rightDown=(rQueen-min(n-cQueen,rQueen-1),cQueen+min(n-cQueen,rQueen-1))"""
left_distance=cQueen-1
right_distance=n-cQueen
up_distance=n-rQueen
down_distance=rQueen-1
left_up_distance=(cQueen-1) if(cQueen-1<n-rQueen) else (n-rQueen)    
left_down_distance=(rQueen-1) if(rQueen-1<cQueen-1) else (cQueen-1)
right_up_distance=(n-cQueen) if(n-cQueen<n-rQueen) else (n-rQueen)
right_down_distance=(n-cQueen) if(n-cQueen<rQueen-1) else (rQueen-1)

for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    
    cut=0
    if(rQueen==rObstacle and cObstacle<cQueen):
        cut=cQueen-cObstacle-1
        if(cut<left_distance):
            left_distance=cut
    elif(rQueen==rObstacle and cObstacle>cQueen):
        cut=cObstacle-cQueen-1
        if(cut<right_distance):
            right_distance=cut
    elif(cQueen==cObstacle and rQueen<rObstacle):
        cut = rObstacle-rQueen-1
        if(cut<up_distance):
            up_distance=cut                
    elif(cQueen==cObstacle and rQueen>rObstacle):
        cut = rQueen-rObstacle-1
        if(cut<down_distance):
            down_distance=cut 
    elif(rObstacle-rQueen==cQueen-cObstacle):
        cut=cQueen-cObstacle-1
        if(cut<left_up_distance):
            left_up_distance=cut
    elif(rQueen-rObstacle==cQueen-cObstacle):
        cut=cQueen-cObstacle-1
        if(cut<left_down_distance):
            left_down_distance=cut
            
    elif(rObstacle-rQueen==cObstacle-cQueen):
        cut=cObstacle-cQueen-1
        if(cut<right_up_distance):
            right_up_distance=cut
    elif(rQueen-rObstacle==cObstacle-cQueen):
        cut=cObstacle-cQueen-1
        if(cut<right_down_distance):
            right_down_distance=cut        
                    
              
sum=left_distance+right_distance+left_up_distance+left_down_distance+right_up_distance+right_down_distance+up_distance+down_distance
print sum