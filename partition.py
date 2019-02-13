n,a,b=map(int,input().split())
x=n//a
y=n//b
c=0
for i in range(0,x):
    for j in range(y,0,-1):
        if a*i+b*j==n and (i+j)%2==0:
            c=c+1
if c==0:
    print("no")
else:
    print("yes")
#partition
