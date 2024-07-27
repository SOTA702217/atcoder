S,T=input().split()
T=list(T)
flag=0

for c in range(1,len(S)):
    for w in range(c,len(S)):
        answer=[]
        for i in range(c-1,len(S),w):
            answer.append(S[i])
        if answer==T:
            print('Yes')
            flag=1
            break
    if flag==1:
        break
    
if flag==0:
    print('No')