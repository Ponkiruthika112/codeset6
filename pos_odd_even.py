n=int(input())
l=list(map(int,input().split()))
p=""
for i in range(0,n):
        if i%2==0 and l[i]%2!=0:
                p=p+str(l[i])+" "
        elif i%2!=0 and l[i]%2==0:
                p=p+str(l[i])+" "
print(p.strip())
#odd nd even
