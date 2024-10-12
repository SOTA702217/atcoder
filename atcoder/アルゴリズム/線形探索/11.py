n=int(input())
x=[]
y=[]
ans=0
for i in range(n):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)
x_s,x_t=map(int,input().split())
y_s,y_t=map(int,input().split())
for i in range(n):
    if x_s<=x[i]<=x_t and y_s<=y[i]<=y_t:
        ans+=1
print(ans)
