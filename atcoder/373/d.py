N,M=map(int,input().split())
X=[1]*N

for i in range(M):
    u,v,w=map(int,input().split())
    X[u-1]=X[v-1]-w

ans=' '.join(map(str,X))

print(ans)
