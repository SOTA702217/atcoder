N=int(input())
count=0
S=[]
flag=0
for i in range(N):
    j=input()
    S.append(j)

for i in S:
    if flag==1:
        print('No')
        exit()
    if i=='sweet':
        count+=1
        if count==2:
            flag=1
    else:
        count=0
    print(count)

print('Yes')
