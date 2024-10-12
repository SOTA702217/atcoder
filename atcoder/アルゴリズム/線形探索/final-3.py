n=int(input())
s=[]
t=[]
ans=0
for i in range(n):
    S,T=map(str,input().split())
    s.append(S)
    T=int(T)
    t.append(T)
k,l=map(int,input().split())
for i in range(n):
    if k<=t[i]<=l:
        ans=s[i]
        print(ans)

