S=list(map(int,input().split()))

q1=[(S[0],S[1]),(S[2],S[3]),(S[4],S[5]),(S[6],S[7])]
q2=[(S[8],S[9]),(S[10],S[11]),(S[12],S[13]),(S[14],S[15])]

q1_inside=True
q2_inside=True
ans=False
count=0

for px,py in q1:
    odd=False
    j=3

    for i in range(4):
        xi,yi=q2[i]
        xj,yj=q2[j]

        if (yi>py)!=(yj>py):
            x=(xj-xi)*(py-yi)/(yj-yi)+xi
            if px<x:
                odd=not odd
        j=i
    if odd:
        ans=True
        break

for px,py in q1:
    odd=False
    j=3

    for i in range(4):
        xi,yi=q2[i]
        xj,yj=q2[j]

        if (yi>py)!=(yj>py):
            x=(xj-xi)*(py-yi)/(yj-yi)+xi
            if px<x:
                odd=not odd
        j=i
    if not odd:
        q1_inside=False


if not ans:
    for px,py in q2:
        odd=False
        j=3

        for i in range(4):
            xi,yi=q1[i]
            xj,yj=q1[j]

            if (yi>py)!=(yj>py):
                x=(xj-xi)*(py-yi)/(yj-yi)+xi
                if px<x:
                    odd=not odd
            j=i
        if odd: 
            ans=True
            break

for px,py in q2:
    odd=False
    j=3

    for i in range(4):
        xi,yi=q1[i]
        xj,yj=q1[j]

        if (yi>py)!=(yj>py):
            x=(xj-xi)*(py-yi)/(yj-yi)+xi
            if px<x:
                odd=not odd
        j=i
    if not odd:
        q2_inside=False

if q1_inside or q2_inside:
    ans=False
    
if ans :
    print("TRUE")
else:
    print("FALSE")