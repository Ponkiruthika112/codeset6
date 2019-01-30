n,k=map(int,input().split())
c=0
for i in range(n,k+1):
	if i==2:
		c=c+1
	for j in range(2,i):
		if i%j==0:
			break
		if j==i-1 and i%j!=0:
			c=c+1
print(c)
	
	#between the gn nos find out prime nos
#thisn
