N = int(input())
A = list(map(int, input().split()))

ans = 0
length = 1  

for i in range(1, N):
    if i > 1 and A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
        length += 1
    else:
        length = 1
    ans += length 
ans += N
print(ans)

