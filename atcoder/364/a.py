# 問題文
# 高橋君は 
# N 個の料理を食べようとしています。

# i 番目に食べようとしている料理は、
# S 
# i
# ​
#  = sweet のとき甘い料理であり、
# S 
# i
# ​
#  = salty のとき塩辛い料理です。

# 高橋君は甘い料理を 
# 2 つ連続で食べると気持ち悪くなってしまい、その後料理が食べられなくなってしまいます。

# 高橋君がすべての料理を食べることができるか判定してください。

# 制約
# N は 
# 1 以上 
# 100 以下の整数
# S 
# i
# ​
#   は sweet または salty
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N
# S 
# 1
# ​
 
# S 
# 2
# ​
 
# ⋮
# S 
# N
# ​
 
# 出力
# 高橋君がすべての料理を食べることができるならば Yes を、できないならば No を出力せよ。

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
