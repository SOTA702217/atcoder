N=int(input())

A=list(map(int,input().split()))
W=list(map(int,input().split()))

a=[0]*N
# print(a)

sum=0

flag=0

for i in range(N):
    # print(A[i])
    if a[A[i]-1]==0:
        a[A[i]-1]=W[i]
    else:
        if a[A[i]-1]<W[i]:
            print(a[A[i]-1])
            sum+=a[A[i]-1]
            a[A[i]-1]=W[i]
        else:
            sum+=W[i]
print(sum)
