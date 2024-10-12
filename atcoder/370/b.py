N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=1
for j in range(1,N+1):
    if ans>=j:
        ans=A[ans-1][j-1]
        
    else:
        ans=A[j-1][ans-1]
        
print(ans)
