#this is my code
n=int(input())
for i in range(2,n):
	if n%i==0:
		print("yes")
		break
if i==n-1:
	print("no")
