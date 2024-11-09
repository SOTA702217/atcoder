A1,A2,A3,A4=map(int,input().split())
ans=0

if A1==A2:
    ans+=1
    A1=5
    A2=6
if A1==A3:
    ans+=1
    A1=5
    A3=7
if A1==A4:
    ans+=1
    A1=5
    A4=8
if A2==A3:
    ans+=1
    A2=6
    A3=7
if A2==A4:
    ans+=1
    A2=6
    A4=8
if A3==A4:
    ans+=1
    A3=7
    A4=8
print(ans)