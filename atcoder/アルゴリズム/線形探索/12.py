n=int(input())
s=[]
t=[]
ans=0
for i in range(n):
    S,T=map(str,input().split())
    s.append(S)
    T=int(T)
    t.append(T)
k=int(input())
for i in range(n):
    if t[i]>=k:
        ans=s[i]
        print(ans)

