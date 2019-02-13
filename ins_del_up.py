# your code goes here
def value(n):
	c=ord(n)-ord("a")+1
	return c
a,b=map(str,input().split())
a=a.lower()
b=b.lower()
k=len(a)
c=0
for i in range(0,k):
    if a[i]==b[i]:
        c=c+0
    else:
        x=value(a[i])
        y=value(b[i])
        c=c+abs(x-y)
if len(a)<len(b):
	for i in range(len(a),len(b)):
		c=c+value(b[i])
else:
	for i in range(len(b),len(a)):
		c=c+value(a[i])
print(c)
#for del
