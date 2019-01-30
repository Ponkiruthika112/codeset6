# your code goes here
def change(a):
	c=1
	for i in range(0,len(a)):
		a=a.replace(a[0],str(c))
		c=c+1
		if a[i]!=1:
			a=a.replace(a[i],str(c))
	return a
s,h=map(str,input().split())
j=change(s)
k=change(h)
if j==k:
	print("yes")
else:
	print("no")
#check the gn two strings are isomorphic
