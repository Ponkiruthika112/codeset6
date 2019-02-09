s=input()
k=""
for i in s:
    if s.count(i)==1 and i!=" ":
        k=k+i+" "
print(k.strip())
#least repeated
