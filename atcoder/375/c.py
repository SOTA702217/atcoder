import numpy as np

N=int(input())
A = [list(input()) for _ in range(N)]
A = np.array(A)

#処理
A=np.array(A)


for i in range(N // 2):
    x_range = np.arange(i, N - i)
    y_range = np.arange(i, N - i)
    x_idx, y_idx = np.meshgrid(x_range, y_range, indexing='ij')
    A_copy = A
    A_copy[y_idx, N - 1 - x_idx] = A[x_idx, y_idx]
    A = A_copy


for row in A:
    print(''.join(row))