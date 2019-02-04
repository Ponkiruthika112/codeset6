n=int(input())
l=[]
size=[]
for i in range(0,n):
    k=input()
    size.append(len(k))
    l.append(k)
y=[]
b=""
min=min(size)
for j in range(0,min):
    for i in range(0,len(l)):
        s=l[i]
        r=s[j]
        y.append((s[j]))
    if y.count(r)==len(l):
        b=b+r
print(b)
#prefix
