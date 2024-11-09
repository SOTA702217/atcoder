N=int(input())
A=list(map(int,input().split()))
B=[]
dict={}

for i in range(N):
    if dict.get(A[i])==None:
        B.append(-1)
        key=A[i]
        value=i+1
        dict[key]=value
    else:
        B.append(dict.get(A[i]))
        key=A[i]
        value=i+1
        dict[key]=value

print(' '.join(map(str,B)))
