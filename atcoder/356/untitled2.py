import sys

N,M=map(int,input().split())

A=list(map(int,input().split()))

total=[0]*M
for i in range(N):
    X=list(map(int, input().split()))
    for j in range(M):
        total[j]+=X[j]
        
for i in range(M):
    if total[i]<A[i]:
        print("No")
        sys.exit()

print("Yes")

