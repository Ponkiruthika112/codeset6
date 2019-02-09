a,b=map(str,input().split())
k=b[0]
c=0
for i in range(0,len(a)):
    if a[i]==b[0]:
        s=a[i:i+len(b)]
        if s==b:
            c=c+1
if c==0:
    print("no")
else:
    print("yes")
#substring
