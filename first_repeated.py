n=int(input())
l=list(map(int,input().split()))
p=[]
s=""
for i in range(0,n):
        if l.count(l[i])>1:
                p.append(l[i])
k=[]
for i in range(0,len(p)-1):
        for j in range(i+1,len(p)):
                if p[i]==p[j]:
                        k.append([j-i,p[i]])
k.sort()
print(k[0][1])
#repeated one
