# 問題文
# N 個の料理があり、
# i 個目の料理の甘さは 
# A 
# i
# ​
#  、しょっぱさは 
# B 
# i
# ​
#   です。

# 高橋君はこれらの 
# N 個の料理を好きな順番で並べ、その順に食べようとします。

# 高橋君は並べた順番の通りに料理を食べていきますが、食べた料理の甘さの合計が 
# X より大きくなるかしょっぱさの合計が 
# Y より大きくなるとその時点で食べるのをやめます。

# 高橋君が食べることになる料理の個数としてあり得る最小値を求めてください。

# 制約
# 1≤N≤2×10 
# 5
 
# 1≤X,Y≤2×10 
# 14
 
# 1≤A 
# i
# ​
#  ,B 
# i
# ​
#  ≤10 
# 9
 
# 入力される値はすべて整数
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N 
# X 
# Y
# A 
# 1
# ​
  
# A 
# 2
# ​
  
# … 
# A 
# N
# ​
 
# B 
# 1
# ​
  
# B 
# 2
# ​
  
# … 
# B 
# N
# ​
 
# 出力
# 答えを出力せよ。

N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))


AB_A=sorted(zip(A,B),reverse=True)
AB_A_A, AB_A_B=zip(*AB_A)
# print(AB_A_A, AB_A_B)
AB_B = sorted(zip(B, A), reverse=True)
AB_B_B, AB_B_A = zip(*AB_B)
# print(AB_B_A, AB_B_B)

count=0
ta=0
tb=0

for i in range(N):
    ta+=AB_A_A[i]
    tb+=AB_B_B[i]
    # print(ta,tb)
    count+=1
    if ta>X or tb>Y:
        break