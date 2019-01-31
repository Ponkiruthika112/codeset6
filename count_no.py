# your code goes here
n=int(input())
s=list(map(int,input().split()))
for i in range(0,len(s)):
	if s.count(s[i])==1:
		print(s[i])
		break
 #count
