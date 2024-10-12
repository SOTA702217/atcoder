N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N // 2):
    A_copy=A
    for j in range(i, N - i):
        A[i][j] = A_copy[j][N - i-1]
        A[j][i]=A_copy[i][N-j-1]
        # for row in A_copy:
        #     print(''.join(row))
        # print(i,j)
    for row in A:
        print(''.join(row))

for row in A:
    print(''.join(row))