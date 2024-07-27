S=input()
a='X'
answer=0
for i in S:
    if i=='R':
        a=i
    elif i=='M':
        if a=='R':
            answer=1
            print('Yes')

if answer==0:
    print('No')