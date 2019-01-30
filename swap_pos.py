l=input()
s=list(l)
i=0
while i<len(s):
	s[i],s[i+1]=s[i+1],s[i]
	i=i+2
print("".join(s))
#swap the even and odd position
