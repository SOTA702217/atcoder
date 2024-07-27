import numpy as np

N,K=map(int,input().split())
b=np.arange(N*N).reshape(N, N)
for i in range(N):
    b[i]=list(map(int,input().split()))

c=list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        for k in c:
            if b[i][j]==k:
                b[i][j]=0
                break

count=0
for i in range(N):
    ans=0
    for j in range(N):
        ans+=b[i][j]
    if ans==0:
        count+=1

for j in range(N):
    ans=0
    for i in range(N):
        ans+=b[i][j]
    if ans==0:
        count+=1
        
ans=0
for i in range(N):
    ans+=b[i][i]
if ans==0:
    count+=1

ans=0
for i in range(N):
    ans+=b[i][N-1-i]
if ans==0:
    count+=1

print(count)