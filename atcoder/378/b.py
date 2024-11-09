N=int(input())
Q=[]
R=[]


for i in range(N):
    q,r=map(int,input().split())
    Q.append(q)
    R.append(r)

P=int(input())

for i in range(P):
    t,d=map(int,input().split())
    q=Q[t-1]
    r=R[t-1]

    if d%q==r:
        print(d)
    else:
        ans=(d//q+1)*q+r
        if ans-q>=d:
            ans-=q
        print(ans)

