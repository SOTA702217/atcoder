N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N // 2):
    for j in range(i, N - i - 1):
        temp = A[i][j]
        A[i][j] = A[j][N - 1 - i]
        A[j][N - 1 - i] = A[N - 1 - i][N - 1 - j]
        A[N - 1 - i][N - 1 - j] = A[N - 1 - j][i]
        A[N - 1 - j][i] = temp

for row in A:
    print(''.join(row))