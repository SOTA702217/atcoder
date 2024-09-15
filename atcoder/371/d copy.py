N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

prefix_sum = [0]
for p in P:
    prefix_sum.append(prefix_sum[-1] + p)

Q = int(input())
import bisect
for _ in range(Q):
    l, r = map(int, input().split())
    left = bisect.bisect_left(X, l)
    right = bisect.bisect_right(X, r)
    ans = prefix_sum[right] - prefix_sum[left]
    print(ans)


