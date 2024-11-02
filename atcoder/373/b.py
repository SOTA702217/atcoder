S=input()
eng='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx2=0
ans=0

for i in eng:
    idx=0
    for j in S:
        if i==j:
            ans+=abs(idx2-idx)
            idx2=idx
            # print(i,ans)
            break
        idx+=1

idx=0
for i in S:
    if i=='A':
        ans-=idx
        break
    idx+=1

print(ans)
