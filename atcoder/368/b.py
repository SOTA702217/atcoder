N=int(input())
A=list(map(int, input().split()))
flag=1

count=0
while flag==1:
    
    A.sort(reverse=True)
    # print(A)
    if A[1] <=0:
        # print(A[1])
        flag = 0
        break
    A[0]-=1
    A[1]-=1
    count+=1

print(count)