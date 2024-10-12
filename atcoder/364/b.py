H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C=[]

for i in range(H):
    C.append(list(input()))

X=input()

for i in range(len(X)):
    if X[i]=='L':
        if Sj>1 and C[Si-1][Sj-2]=='.':
            Sj-=1
    elif X[i]=='R':
        if Sj<W and C[Si-1][Sj]=='.':
            Sj+=1
    elif X[i]=='U':
        if Si>1 and C[Si-2][Sj-1]=='.':
            Si-=1
    elif X[i]=='D':
        if Si<H and C[Si][Sj-1]=='.':
            Si+=1
print(Si, Sj)