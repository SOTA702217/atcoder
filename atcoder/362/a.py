R,G,B=map(int,input().split())
C=input()
x=0

if C=='Red':
    if G<B:
        x=G
    else:
        x=B
    print(x)
elif C=='Green':
    if R<B:
        x=R
    else:
        x=B
    print(x)
else:
    if G<R:
        x=G
    else:
        x=R
    print(x)

