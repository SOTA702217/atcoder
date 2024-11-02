S = input()
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
idx2 = 0
ans = 0

p = {}
for idx, c in enumerate(S):
    if c not in p:
        p[c] = idx

for char in eng:
    if char in p:
        idx = p[c]
        ans += abs(idx2 - idx)
        idx2 = idx
print(ans)
