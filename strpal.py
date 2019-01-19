# your code goes here to find palindrome
s=input()
k=""
for i in range(len(s)-1,-1,-1):
	k=k+s[i]
if k==s:
	print("palindrome")
else:
	print("not palindrome")
