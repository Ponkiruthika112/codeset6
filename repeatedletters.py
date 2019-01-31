# your code goes here
s=input()
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
d=[0]*36
for i in s:
	for j in range(0,len(l)):
		if i==l[j] or i.lower()==l[j]:
			d[j]=d[j]+1
k=d.index(max(d))
print(l[k])
#to find repeated one
