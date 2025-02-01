N,Q=map(int,input().split())
lst=[1]*N
p=list(range(N))

for _ in range(Q):
    ans=0
    i=list(map(int,input().split()))
    if i[0]==1:
        P=i[1]-1
        H=i[2]-1

        oldp=p[P]
        p[P]=H

        lst[oldp]-=1
        lst[H]+=1
    elif i[0]==2:
        ans=sum(1 for x in lst if x>1)
        print(ans)
