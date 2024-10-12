n=int(input())
x=[]
y=[]
ans=0
for i in range(n):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)
x_n=x[n-1]
y_n=y[n-1]
k=int(input())
for i in range(n):
    x_d=abs(x_n-x[i])
    y_d=abs(y_n-y[i])
    if x_d+y_d<=k:
        ans+=1
print(ans)
