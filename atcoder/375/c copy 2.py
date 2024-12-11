N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N // 2):
    A_copy = [row[:] for row in A] 
    for a in range(i, N - i):
        for b in range(i, N - i):
            A_copy[b][N-a-1] = A[a][b]
    A = [row[:] for row in A_copy]
    # print('=========================')
    # for row in A:
    #     print(''.join(row))


for row in A:
    print(''.join(row))