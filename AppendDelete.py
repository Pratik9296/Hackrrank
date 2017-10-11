'''
Created on 24-Aug-2017

@author: pratik
'''

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
if(len(s)==0):
    pass
else:
    len_s=len(s)
    len_t=len(t)
    for i in range(len_s):
        if not (s[i]==t[i]):
            break
    remain_s=s[i:]
    remain_t=t[i:]
    if(len(remain_s)+len(remain_t)<k):
        print "No"
        