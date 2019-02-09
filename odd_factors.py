n=int(input())
s=""
for i in range(1,n):
    if n%i==0 and i%2!=0:
        s=s+str(i)+" "
if i==n-1 and n%2!=0:
    s=s+str(i)+" "
print(s.strip())
#odd factors
