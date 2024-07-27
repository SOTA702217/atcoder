N=int(input())

L=[]
R=[]
X=[]

for i in range(N):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
    
for i in range(N):
    X.append((L[i]+R[i])//2)
# print(X)

total=sum(X)

while total!=0:
      a_sum=total
      for i in range(N):
          if total==0:
              break
          if total<0:
              p=min(-total,R[i]-X[i])
              X[i]+=p
              total+=p
          elif total>0:
              m=min(total,X[i]-L[i])
              X[i]-=m
              total-=m
      # print(X)
      if total==a_sum:
          break
if total==0:
    print('Yes')
    print(*X)
else:
  print('No')