# 問題文
# あなたはゲームをプレイしています。

# N 人の敵が一列に並んでおり、前から 
# i 番目の敵の体力は 
# H 
# i
# ​
#   です。

# あなたは 
# 0 で初期化された変数 
# T を使い、全ての敵の体力が 
# 0 以下になるまで次の行動を繰り返します。

# T を 
# 1 増やす。その後、体力が 
# 1 以上である最も前の敵を攻撃する。このとき、
# T が 
# 3 の倍数ならばその敵の体力は 
# 3 減り、そうでないなら 
# 1 減る。
# 全ての敵の体力が 
# 0 以下になったときの 
# T の値を求めてください。

# 制約
# 1≤N≤2×10 
# 5
 
# 1≤H 
# i
# ​
#  ≤10 
# 9
 
# 入力は全て整数
# 入力
# 入力は以下の形式で標準入力から与えられる。

# N
# H 
# 1
# ​
  
# H 
# 2
# ​
  
# … 
# H 
# N
# ​
 
# 出力
# 答えを出力せよ。

N = int(input())
H = list(map(int, input().split()))

T = 0  

for health in H:

    cycle_position = (T % 3)
    
    full_cycles = max((health - (3 - cycle_position) % 3 * 1 - (cycle_position == 0) * 2) // 5, 0)

    damage = full_cycles * 5
    
    T += full_cycles * 3
    
    remaining_health = health - damage
    while remaining_health > 0:
        T += 1
        if T % 3 == 0:
            remaining_health -= 3
        else:
            remaining_health -= 1

print(T)

