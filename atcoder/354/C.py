N=int(input())
card=[]

for i in range(N):
    A,C=map(int,input().split())
    card.append((C,A,i+1))

card.sort()
cost=10000000000
result=[]
power=0

for C,A,i in card:
    if power<A:
        result.append((i,A,C))
        power=A

result.sort()

result2=[]
for i,A,C in result:
    result2.append(i)
print(len(result2))
print(' '.join(map(str,result2)))