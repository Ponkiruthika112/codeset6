# your code goes here
n,k=map(int,input().split())
l=list(map(int,input().split()))
p=n-(k%n)
g=[]
h=""
for i in range(p,len(l)):
	g.append(l[i])
for i in range(0,p):
	g.append(l[i])
for i in range(0,len(g)):
	h=h+str(g[i])+" "
print(h.strip())
#for left shifting
