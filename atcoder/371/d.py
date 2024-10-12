N=int(input())
X=list(map(int,input().split()))
P=list(map(int,input().split()))
Q=int(input())

for i in range(Q):
    ans=[]
    l,r=map(int,input().split())
    for j in range(len(X)):
        # print('aaaaa',X[j],l,r)
        if l<=X[j] and X[j]<=r:
            ans.append(P[j])
            # print(ans)
    if len(ans)==0:
        print(0)
    else:   
        print(sum(ans))

