#this is to replace the string
s=input()
k=len(s)//2
y=""
y=y+s.replace(s[k],"*")
if len(s)%2==0:
	y=y.replace(s[k-1],"*")
print(y)
