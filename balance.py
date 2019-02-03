s=input()
c=0
for i in s:
	if i=="(":
		c=c+1
	else:
		c=c-1
if c==0:
	print("yes")
else:
	print("no")
#balanced or not 
