N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

X_A = [[x, a] for x, a in zip(X, A)]
X_A.sort()
p=1
ans=0



print(X_A)

sum_A=sum(A)

if sum_A!=M:
    print(-1)
    exit()

for i in range(1,M+1):
    #初期化
    exist=[]
    exist_k=[]
    sum_exist_k=0
    check=False

    x=X_A[i-1][0] #基準の位置
    a=X_A[i-1][1]-1 #余剰の石の数
    b=abs(x-p) #pointからの距離
    exist = [c for c in A if p <= c <= p+a] #pointからaまでのすでにある石の数
    b+=len(exist) #pointからaまでのすでにある石の数を足す

    while check==False:
        exist = any(p <= c <= p+b for c in A)#pointからbまでのすでにある石の数
        if exist:
            check=True
            b+=1
    p+=b#pointを更新

    for j in range(len(exist)):
        exist_k.append(x-exist[j])#かぶった石の位置からの距離を計算
    sum_exist_k=sum(exist_k)#かぶった石の位置からの距離の合計を計算

    #階数を計算
    #かぶった石の距離を引く
    #ansに足す

