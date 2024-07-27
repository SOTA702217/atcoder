N,K,X=map(int,input().split())

B=list(map(int,input().split()))

B.append(0)

for i in range(N,K-1,-1):
    if i==K:
        B[i]=X
    else:
        B[i]=B[i-1]
        
print(*B)