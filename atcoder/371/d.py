# 問題文
# 数直線上に 
# N 個の村があります。
# i 番目の村は座標 
# X 
# i
# ​
#   にあり、
# P 
# i
# ​
#   人の村人がいます。

# Q 個のクエリに答えてください。
# i 番目のクエリは以下の形式です。

# 整数 
# L 
# i
# ​
#  ,R 
# i
# ​
#   が与えられる。座標が 
# L 
# i
# ​
#   以上 
# R 
# i
# ​
#   以下の村に住んでいる村人の人数の総数を求めよ。
# 制約
# 1≤N,Q≤2×10 
# 5
 
# −10 
# 9
#  ≤X 
# 1
# ​
#  <X 
# 2
# ​
#  <…<X 
# N
# ​
#  ≤10 
# 9
 
# 1≤P 
# i
# ​
#  ≤10 
# 9
 
# −10 
# 9
#  ≤L 
# i
# ​
#  ≤R 
# i
# ​
#  ≤10 
# 9
 
# 入力される数値は全て整数
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N
# X 
# 1
# ​
  
# … 
# X 
# N
# ​
 
# P 
# 1
# ​
  
# … 
# P 
# N
# ​
 
# Q
# L 
# 1
# ​
  
# R 
# 1
# ​
 
# ⋮
# L 
# Q
# ​
  
# R 
# Q
# ​
  
# 出力
# Q 行出力せよ。

# i (1≤i≤Q) 行目には、
# i 番目のクエリに対する答えを出力せよ。

N=int(input())
X=list(map(int,input().split()))
P=list(map(int,input().split()))
Q=int(input())

for i in range(Q):
    ans=[]
    l,r=map(int,input().split())
    for j in range(len(X)):
        # print('aaaaa',X[j],l,r)
        if l<=X[j] and X[j]<=r:
            ans.append(P[j])
            # print(ans)
    if len(ans)==0:
        print(0)
    else:   
        print(sum(ans))

