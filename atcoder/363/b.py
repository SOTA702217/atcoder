N,T,P=map(int,input().split())
L=list(map(int,input().split()))

L.sort(reverse=True)

a=T-L[P-1]

if a<=0:
    a=0
    print(a)
else:
    print(a)