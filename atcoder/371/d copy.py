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

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

prefix_sum = [0]
for p in P:
    prefix_sum.append(prefix_sum[-1] + p)

Q = int(input())
import bisect
for _ in range(Q):
    l, r = map(int, input().split())
    left = bisect.bisect_left(X, l)
    right = bisect.bisect_right(X, r)
    ans = prefix_sum[right] - prefix_sum[left]
    print(ans)


