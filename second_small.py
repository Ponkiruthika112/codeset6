# your code goes here
n=int(input())
l=list(map(int,input().split()))
l.sort()
l.remove(l[0])
print(l[0])
#for second small no
