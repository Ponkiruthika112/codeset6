s=input()
c=0
for i in range(0,len(s)):
	if s[i]=="I":
		c=c+1
	elif s[i]=="V":
		if i>0 and s[i-1]=="I":
			c=c+4-1
		else:
			c=c+5
	elif s[i]=="X":
		if i>0 and s[i-1]=="I":
			c=c+9-1
		else:
			c=c+10
	elif s[i]=="L":
		c=c+50
	elif s[i]=="C":
		c=c+100
	elif s[i]=="D":
		c=c+500
	elif s[i]=="M":
		c=c+1000
print(c)
#convert roman to integer
	
