a,b,c,d,e,f=map(int,input().split())
g,h,i,j,k,l=map(int,input().split())
flag=0

if j<=a or k<=b or l<=c:
  flag=1

if d<=g or e<=h or f<=i:
  flag=1
  
if flag==0:
  print("Yes")
else:
  print("No")

