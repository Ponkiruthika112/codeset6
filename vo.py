s=input()
l=list(s)
for i in range(0,len(l)):
	if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u" or l[i]=="A" or l[i]=="E" or l[i]=="I" or l[i]=="O" or l[i]=="U":
		l.remove(l[i])
