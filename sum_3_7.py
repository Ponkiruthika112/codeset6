# your code goes here
n=int(input())
if n%3==0 or n%7==0:
	print("yes")
else:
	k=n%3
	y=n-k
	i=0
	while i<y:
		s=y-3
		if s+7==n:
			print("yes")
			break
		else:
			y=s
			i=i+1
	else:
		print("no")
#for sum of 3 and 7
