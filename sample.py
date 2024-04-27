N=int(input())
A=list(map(int,input().split()))
ball=[]

for i in range(N):
  ball.append(A[i])
  while len(ball)>1:
    if ball[len(ball)-1]!=ball[len(ball)-2]:
      break
    else:
      ball.append(ball[len(ball)-1]+1)
      ball.pop(len(ball)-2)
      ball.pop(len(ball)-2)
      

print(len(ball))