n,k=map(int,input().split())
for i in range(n,k+1):
	if i==2:
		print(i,end=" ")
	for j in range(2,i):
		if i%j==0:
			break
		if j==i-1 and i%j!=0:
			print(i,end=" ")
	#between the gn nos find out prime nos
