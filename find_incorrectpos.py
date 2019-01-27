#this is to find the position of inorder nos 
n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l)):
	k.append(l[i])
k.sort()
i=0
while i<len(l):
	if l[i]!=k[i]:
		print(i)
		break
	i=i+1
