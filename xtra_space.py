# your code goes here
s=input()
k=" "
for i in range(0,len(s)):
	if s[i]==" "and s[i+1]==" ":
		k=s.replace(" ","")
	else:
		k=s
print(k)
#remove extra spaces
