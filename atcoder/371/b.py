N,M=map(int,input().split())
A=[]

for i in range(M):  
    flag=0
    a,b=map(str,input().split())
    if b=='M':
        for j in range(len(A)):
            if A[j]==a:
                print('No')
                flag=1
                break
    else:
        print('No')
        flag=1
    if flag==0:
        print('Yes')
        A.append(a)
