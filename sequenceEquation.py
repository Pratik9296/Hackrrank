'''
Created on 23-Aug-2017

@author: pratik
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input().strip())
a=raw_input().strip().split(' ')
counter=1
for i in a:
    index1=a.index(str(counter))+1
    index2=a.index(str(index1))+1
    print index2
    counter+=1
    