# 問題文
# 長さ 
# N の整数列 
# A=(A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#  ) が与えられます。また、
# f(l,r) を以下で定義します。

# (A 
# l
# ​
#  ,A 
# l+1
# ​
#  ,…,A 
# r−1
# ​
#  ,A 
# r
# ​
#  ) に含まれる値の種類数
# 次の式の値を求めてください。

# i=1
# ∑
# N
# ​
  
# j=i
# ∑
# N
# ​
#  f(i,j)


# 制約
# 1≤N≤2×10 
# 5
 
# 1≤A 
# i
# ​
#  ≤N
# 入力される数値は全て整数
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N
# A 
# 1
# ​
  
# … 
# A 
# N
# ​
 
# 出力
# 答えを出力せよ。

N=int(input())
A=list(map(int, input().split()))

p=[[]for _ in range(N+1)] 

for idx, val in enumerate(A,1):
    p[val].append(idx)

total=0
for val_p in p:
    if val_p==[]:
        continue
    a=0
    for pos in val_p:
        c=(pos-a) * (N-pos+1)
        total+=c
        a=pos

print(total)
