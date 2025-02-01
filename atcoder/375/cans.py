N = int(input())
A = [list(input()) for _ in range(N)]
B = [['' for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        c = min(x, N - 1 - x, y, N - 1 - y)
        t = c % 4
        nx, ny = x, y
        for _ in range(t):
            # 回転操作を t 回適用
            nx, ny = ny, N - 1 - nx
        B[nx][ny] = A[x][y]

for row in B:
    print(''.join(row))
