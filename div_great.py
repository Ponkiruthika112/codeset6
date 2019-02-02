def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
n,k=map(int,input().split())
print(gcd(n,k))
#this is for to find the greatest no divide by both

