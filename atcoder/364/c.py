N,X,Y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))


AB_A=sorted(zip(A,B),reverse=True)
AB_A_A, AB_A_B=zip(*AB_A)
# print(AB_A_A, AB_A_B)
AB_B = sorted(zip(B, A), reverse=True)
AB_B_B, AB_B_A = zip(*AB_B)
# print(AB_B_A, AB_B_B)

count=0
ta=0
tb=0

for i in range(N):
    ta+=AB_A_A[i]
    tb+=AB_B_B[i]
    # print(ta,tb)
    count+=1
    if ta>X or tb>Y:
        break