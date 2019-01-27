#to find product of digits
n=int(input())
p=1
r=0
while n>0:
	r=n%10
	p=p*r
	n=n//10
print(p)
