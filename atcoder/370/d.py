H,W,Q=map(int,input().split())
R=[]
C=[]
S=[[0]*W for i in range(H)]

for i in Q:
    r,c=map(int,input().split())
    R.append(r)
    C.append(c)

for i in range(Q):
    S[R[i]-S[R[i]][C[i]]][C[i]-[R[i]][C[i]]]+=1
    S[R[i]-1][C[i]-1]+=1
    