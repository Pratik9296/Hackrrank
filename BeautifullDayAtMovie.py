'''
Created on 18-Aug-2017

@author: pratik
'''
i,j,k=raw_input().strip().split(' ')
i,j,k=int(i),int(j),int(k)
counter=0
for number in range(i,j):
    if((number-int(str(number)[::-1]))%k==0):
        counter+=1
print counter        