def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

l,r=map(int,input().split())
k=gcd(l,r)
print(l*r//k)
#smallest divisible
