'''
Created on 24-Aug-2017

@author: pratik
'''
def remove(a,b,k,arr):
    count1,count2=(0,0)
    for i in arr:
        if(i==a or i==b):
            pass
        elif((i+a)%k!=0):
            count1+=1
        elif((i+b)%k!=0):
            count2+=1
        else:
            pass
    if(count1<count2):
        arr.remove(a)
    else:
        arr.remove(b)                
    
n,k=raw_input().strip().split(' ')
n,k=int(n),int(k)
arr=map(int,raw_input().strip().split(' '))
count=[]
for i in range(len(arr)-1):
    for j in range(i,len(arr)-1):
        ans=arr[i]+arr[j]
        if(ans%k==0):
            remove(arr[i], arr[j], k, arr)
print len(arr)            