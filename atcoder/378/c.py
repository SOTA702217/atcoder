N=int(input())
A=list(map(int,input().split()))
B=[]
L=[0]*N

for i in range(N):
    if L[A[i]]==0:
        B.append(-1)
        L[A[i]]=i+1
        print(L)
    else:
        B.append(L[A[i]])
        L[A[i]]=i+1
        print(L)
print(B)
