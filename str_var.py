# your code goes here
a,b,c=map(str,input().split())
k=int(c)
p=a[0]

for i in a:
	a=a.replace(p,"1")
	b=b.replace(p,"1")
	if i!="1":
		a=a.replace(i,"1")
		b=b.replace(i,"1")
for i in b:
	if i!="1":
		b=b.replace(i,"0")
if b.count("0")==k:
	print("yes")
else:
	print("no")
#for str varying
