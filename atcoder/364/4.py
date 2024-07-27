N,Q=map(int,input().split())
a=list(map(int,input().split()))
k=[]
for i in range(Q):
    bi,ki=map(int,input().split())
    k.append(ki)
    b=sorted(abs(ai-bi) for ai in a)[ki-1]
    print(b)
