'''
Created on 23-Aug-2017

@author: pratik
'''
def saveThePrisoner(n, m, s):
    return 0 if((s+m-1)%5==0) else (s+m-1)%5
    rem=(s+m-1)%n
    if(rem==0):
        return n
    else:
        return rem
        

t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
