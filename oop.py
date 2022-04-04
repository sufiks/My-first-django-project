a,b,count=int(input()),int(input()),0
for i in range(a,b+1):
    if (i**3)%4==0 or (i**3)%9==0:
        count+=1
print(count)




