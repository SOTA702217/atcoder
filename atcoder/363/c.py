from itertools import permutations

# 入力の読み込み
N, K = map(int, input().split())
S = input()

# 順列の生成
perms = set(''.join(p) for p in permutations(S))

def is_palindrome(s):
    return s == s[::-1]

# 回文を含まない順列のカウント
count = 0

for perm in perms:
    has_palindrome = False
    for i in range(N - K + 1):
        substring = perm[i:i+K]
        if is_palindrome(substring):
            has_palindrome = True
            break  # 回文を見つけたのでこの順列を無視
    if not has_palindrome:
        count += 1

print(count)
