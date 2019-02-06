n=int(input())
l=list(map(int,input().split()))
print(l)
c=0
s=""
for j in range(0,len(l)):
        if j==l[j]:
                s=s+str(l[j])+" " 
                c=c+1
if c==0:
        print(-1)
else:
        print(s.strip())
#index_value
