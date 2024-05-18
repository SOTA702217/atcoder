N=int(input())
user=[]
rate=0
for i in range(N):
    S,C=input().split()
    C=int(C)
    user.append((S,C))

user.sort()
rate=sum(C for S,C in user)

winner=rate%N

print(user[winner][0])