#this is my code to find even odd or odd
n,m=map(int,input().split())
d=abs(n-m)
if d%2==0:
	print("even")
else:
	print("odd")
