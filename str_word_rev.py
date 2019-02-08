s=input()
j=0
for i in range(0,len(s)):
    if s[i]==" ": 
        k=s[j:i]
        j=i+1
        print(k[::-1],end=" ")
    elif i==len(s)-1:
        k=s[j:i+1]
        print(k[::-1])
#to print a string 
