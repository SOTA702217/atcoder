import math
p=(1+math.sqrt(5))/2
l,r=map(int,input().split())
ans1,ans2=l+(r-l)/(p+1),r-(r-l)/(p+1)
print(ans1,ans2)