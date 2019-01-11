#this is my code
s=input()
c=0
d=0
for i in s:
	if i.isalpha():
		c=c+1
	elif i.isdigit():
		d=d+1
if c>0 and d>0:
	print("Yes")
else:
	print("No")
