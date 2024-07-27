N,L,R=map(int,input().split())

A=list(range(1,N+1))
Ar=list(range(1,N+1))
for i in range((R-L+1)//2):
    Ar[L-1+i],Ar[R-1-i]=A[R-1-i], A[L-1+i]

print(*Ar)
