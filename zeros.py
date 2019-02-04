# your code goes here
n=int(input())
l=list(map(int,input().split()))
k=l.count(0)
i=0
s=""
while i<len(l):
    if l[i]==0:
        l.remove(l[i])
    else:
        i=i+1
for i in range(0,k):
    l.append(0)
for i in range(0,len(l)):
    s=s+str(l[i])+" "
print(s.strip())
#for append zeros at end
