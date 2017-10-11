'''
Created on 18-Aug-2017

@author: pratik
'''
n=input()
start=5
likes=0
for i in range(n):
    likes+=start//2
    start=(start//2)*3
print likes    