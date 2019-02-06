n=int(input())
l=list(map(int,input().split()))
p=[]
s=""
for i in range(0,n):
        if l.count(l[i])>1:
                p.append(l[i])
p.sort()
i=0
while i<len(p)-1:
        if p[i]==p[i+1]:
                p.remove(p[i])
        else:
                i=i+1
for i in range(0,len(p)):
        s=s+str(p[i])+" "
print(s.strip())
#repeated nos        

