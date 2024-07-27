N,K=map(int,input().split())
A=list(map(int,input().split()))

mi=100000000000000
A.sort()
for i in range(K+1):
    if A[i+N-K-1]-A[i]<mi:
      mi=A[i+N-K-1]-A[i]
      
print(mi)

