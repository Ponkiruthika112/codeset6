n=int(input())
l=str(n)
c=0
for i in range(0,len(l)):
    if int(l[i:i+2])<10 and len(l[i:i+2])==2:
        c=c+0
    elif int(l[i:i+2])<26 and len(l[i:i+2])==2:
        c=c+1
    else:
        c=c+0
print(c+c//2+1)
    
#permutation
