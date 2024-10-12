n=int(input())
a_i=list(map(int,input().split()))
k=int(input())

for i in range(n):
    if a_i[i]==k:
        print(i+1)