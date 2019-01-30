# your code goes here
a,b=map(str,input().split())
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
if abs(a.count("1")-b.count("1"))==1:
	print("yes")
else:
	print("no")
#did\f
#j.fg
		

