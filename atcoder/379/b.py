N,K=map(int,input().split())
S=input()
count=0
ans=0

for i in range(N):
    if count==0:
        if S[i]=='O':
            for j in range(i,i+K):
                if i+K>N:
                    break
                if S[j]=='O':
                    if j==i+K-1:
                        count=K-1
                        ans+=1
                    continue
                else:
                    break
    else:
        count-=1
print(ans)