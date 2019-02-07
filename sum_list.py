n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
        for j in range(i+1,n):
                k=l[i]+l[j]
                if l.count(k)>0:
                        print(l[i],l[j],k)
#for printing nos
