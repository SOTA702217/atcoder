N=int(input())
AL=0
AR=0
ans=0
L=0
R=0
for i in range(N):
    A,S=map(str,input().split())
    A=int(A)
    if S=="L":
        if L==0:
            AL=A
            L=1
        ans+=abs(A-AL)
        AL=A
    else:
        if R==0:
            AR=A
            R=1
        ans+=abs(A-AR)
        AR=A
    # print(ans)
print(ans)