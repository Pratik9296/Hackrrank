'''
Created on 24-Aug-2017

@author: pratik
'''
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
length=len(arr)
while(length!=0):
    print length
    #print arr
    small=min(arr)
    while small in arr: arr.remove(small)
    arr=[x-small for x in arr]
    length=len(arr)