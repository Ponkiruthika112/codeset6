 # your code goes here
n=int(input())
c=0
k=" "
for i in range(1,n+1):
	if n%i==0:
		if i==2:
			k=k+str(i)+" "
		for j in range(2,i):
			if i%j==0:
				break
			if j==i-1 and i%j!=0:
				k=k+str(i)+" "
print(k.strip())	
#this is to print prime factors
