#this is to print *
s=input()
p=list(s)
k=len(s)//2
y=""
p[k]="*"
if len(s)%2==0:
	p[k-1]="*"
h=y.join(p)
print(h)
