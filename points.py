import math
def colinear(x1,y1,x2,y2):
    s=((y2-y1)*(y2-y1))+((x2-x1)*(x2-x1))
    return math.sqrt(s)
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
p1=colinear(x1,y1,x2,y2)
p2=colinear(x2,y2,x3,y3)
p3=colinear(x3,y3,x1,y1)
print(p1,p2,p3)
if p3==p1+p2 or p1==p2+p3 or p2==p1+p3:
    print("yes")
else:
    print("no")
#to find the given points lies on the same line
