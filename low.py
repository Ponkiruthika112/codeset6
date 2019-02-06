def low(l):
    s=min(l)
    m=l.index(min(l))
    for i in range(0,m+1):
        l.remove(l[0])
    return s
n,k=map(int,input().split())
l=list(str(n))
p=""
if k==0:
    print(n)
elif k==len(str(n)):
    print(0)
else:
    for i in range(0,len(str(n))-k):
        p=p+low(l)
    print(p)
#to print low nos
