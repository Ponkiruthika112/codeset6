n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
k=0
j=0
for i in range(0,m):
        while j<len(a):
                if b[i]==a[j]:
                        a.remove(a[j])
                        c=c+1
                        break
                else:
                        j=j+1
        j=0
        if c==0:
                print("NO")
                break
        k=k+1
        c=0
if k==m:
        print("YES")
                
                
#subarray
