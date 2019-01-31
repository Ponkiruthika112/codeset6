s=input()
l=list(s)
i=0
while i<len(l):
	if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u" or l[i]=="A" or l[i]=="E" or l[i]=="I" or l[i]=="O" or l[i]=="U":
		l.remove(l[i])
	else:
	    i=i+1
p="".join(l)
print(p[::-1])
#to remove vowel
