N,T=map(int,input().split())
S=input()
X=list(map(int,input().split()))
a=[]
sumn=0
for i in range(N):
    a.append(int(S[i]))   

for i in range(N):
    if a[i]==1:
        for j in range(i,N):
            if X[i]<X[j]:
                if (X[j]-X[i])/2<T:
                    sumn+=1
print(sumn)