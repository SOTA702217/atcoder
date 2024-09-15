N=int(input())
A=list(map(int,input().split()))
ans=0  
for i in range(N):
    for j in range(i+1,N):
        d=A[j]-A[j-1]
        if j+1<N and A[j]+d==A[j+1]:
            continue
        else:
            ans+=j-i+1
            break
print(ans+1)