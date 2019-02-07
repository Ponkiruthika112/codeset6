n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
        for j in range(i+1,n):
                k=l[i]+l[j]
                for m in range(j+1,n):
                        if l[m]==k:
                                print(l[i],l[j],l[m])
                                break
               
#for printing nos
