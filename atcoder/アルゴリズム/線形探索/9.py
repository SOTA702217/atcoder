n=int(input())
a=list(map(int,input().split()))
k=int(input())
sorted_a=sorted(a,reverse=True)
ans=0
for i in range(n):
    if sorted_a[i]<=k:
        ans=sorted_a[i]
        break
print(ans)
