# your code goes here
n,k=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
for i in range(0,len(p)):
    l.append(p[i])
    if i==len(p)-1:
        print(max(l))
    else:
        print(max(l),end=" ")
    
#this is to append
