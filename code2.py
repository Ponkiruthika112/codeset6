#thud
s=input()
c=0
for i in s:
	if i=="1" or i=="0":
		c=c+1
if c==len(s):
	print("yes")
else:
	print("no")
