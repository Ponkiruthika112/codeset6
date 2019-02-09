n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
if l==k:
    print("yes")
else:
    print("no")
    
#list is sorted or not
