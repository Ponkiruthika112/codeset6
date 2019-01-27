#for odd nos
n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
for i in range(0,n):
	if l[i]%2!=0:
		p.append(l[i])
print(p[k-1])
