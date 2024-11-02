N,M,K=map(int,input().split())

A=list(map(int,input().split()))

n=K-sum(A)
print(n)

A_list=list(enumerate(A))

sorted_A=sorted(A_list,key=lambda x:x[1],reverse=True)

for i in range(N):
    A_list[i]=0