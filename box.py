# your code goes here
n=int(input())
l=list(map(int,input().split()))
l.sort()
i=0
c=1
while i<len(l)-1:
	if l[i]==l[i+1]:
		c=c+1
		i=i+2
	else:
		i=i+1
print(c)
#box
	
