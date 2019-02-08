n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
i=0
while i<k-1:
    l.remove(l[0])
    i=i+1
print(l[0])
#k th largest element
