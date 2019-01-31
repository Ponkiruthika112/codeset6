l,r=map(int,input().split())
if r>l:
	l,r=r,l
if l%r==0:
	print(l)
else:
	print(l*r)
#for smallest div value
