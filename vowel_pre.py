#this pgm is to find vowels in a string OR NOT
s=input()
c=0
for i in s:
	if i=='a' or i=='e' or i=="i" or i=="o" or i=="u":
		c=c+1
		break
if c==1:
	print("yes")
else:
	print("no")
