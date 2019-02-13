n=int(input())
l=list(map(int,input().split()))
k=[]
s=list(set(l))
for i in range(0,len(s)):
       k.append(l.count(s[i]))
print(max(k))
#max
