N=int(input())
A=list(map(int, input().split()))

p=[[]for _ in range(N+1)] 

for idx, val in enumerate(A,1):
    p[val].append(idx)

total=0
for val_p in p:
    if val_p==[]:
        continue
    a=0
    for pos in val_p:
        c=(pos-a) * (N-pos+1)
        total+=c
        a=pos

print(total)
