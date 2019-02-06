n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
s=""
for i in range(0,n):
        s=s+str(l[i])
print(int(s))
#largest
