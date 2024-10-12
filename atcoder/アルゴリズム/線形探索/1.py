n=int(input())
a_i=list(map(int,input().split()))
k=int(input())
ans=0

for i in range(n):
    if a_i[i]==k:
        ans+=1
print(ans)