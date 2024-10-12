n,k=map(int,input().split())
s=list(input())
ans=s.count('.')
c0=[]
c1=[]
c2=[]

for i in range(0,len(s),3):
    c0.append(s[i:i+3])
c0SSS=0
c0SSSidx=[]
for i in range(len(c0)):
    if c0[i]==['S','S','S']:
        c0SSS+=1
        c0SSSidx.append(i)
for i in range(k):
    if c0SSS!=0:
        s[c0SSSidx[i]*3]='.'
        s[c0SSSidx[i]*3+1]='.'
        s[c0SSSidx[i]*3+2]='.'
        c0SSS-=1
        ans+=3
        k-=1
        if c0SSS==0 or k==0:
            break

for i in range(1,len(s),3):
    c1.append(s[i:i+3])
c1SSS=0
c1SSSidx=[]
for i in range(len(c1)):
    if c1[i]==['S','S','S']:
        c1SSS+=1
        c1SSSidx.append(i)
for i in range(k):
    if c1SSS!=0:
        s[c1SSSidx[i]*3+1]='.'
        s[c1SSSidx[i]*3+2]='.'
        s[c1SSSidx[i]*3+3]='.'
        c1SSS-=1
        ans+=3
        k-=1
        if c1SSS==0 or k==0:
            break

for i in range(2,len(s),3):
    c2.append(s[i:i+3])
c2SSS=0
c2SSSidx=[]
for i in range(len(c2)):
    if c2[i]==['S','S','S']:
        c2SSS+=1
        c2SSSidx.append(i)
for i in range(k):
    if c2SSS!=0:
        s[c2SSSidx[i]*3+2]='.'
        s[c2SSSidx[i]*3+3]='.'
        s[c2SSSidx[i]*3+4]='.'
        c2SSS-=1
        ans+=3
        k-=1
        if c2SSS==0 or k==0:
            break
############################################
c0=[]
c1=[]
c2=[]
for i in range(0,len(s),3):
    c0.append(s[i:i+3])
    # print(s[i:i+3])
c0SS=0
c0SSidx=[]
for i in range(len(c0)):
    if c0[i]==['.','S','S'] or c0[i]==['S','.','S'] or c0[i]==['S','S','.'] or c0[i]==['S','S']:
        c0SS+=1
        c0SSidx.append(i)
for i in range(k):
    if c0SS!=0:
        s[c0SSidx[i]*3]='.'
        s[c0SSidx[i]*3+1]='.'
        if c0SSidx[i]*3+2<len(s):
            s[c0SSidx[i]*3+2]='.'
        c0SS-=1
        ans+=2
        k-=1
        if c0SS==0 or k==0:
            break
# print(k)
# print(ans)

for i in range(1,len(s),3):
    c1.append(s[i:i+3])
c1SS=0
c1SSidx=[]
for i in range(len(c1)):
    if c1[i]==['.','S','S'] or c1[i]==['S','.','S'] or c1[i]==['S','S','.'] or c1[i]==['S','S']:
        c1SS+=1
        c1SSidx.append(i)
for i in range(k):
    if c1SS!=0:
        s[c1SSidx[i]*3+1]='.'
        s[c1SSidx[i]*3+2]='.'
        if c1SSidx[i]*3+3<len(s):
            s[c1SSidx[i]*3+3]='.'
        c1SS-=1
        ans+=2
        k-=1
        if c1SS==0 or k==0:
            break

for i in range(2,len(s),3):
    c2.append(s[i:i+3])
c2SS=0
c2SSidx=[]
for i in range(len(c2)):
    if c2[i]==['.','S','S'] or c2[i]==['S','.','S'] or c2[i]==['S','S','.'] or c2[i]==['S','S']:
        c2SS+=1
        c2SSidx.append(i)
if s[0]=='S' and s[1]=='S' and k!=0:
    ans+=2
    s[0]='.'
    s[1]='.'
for i in range(k):
    if c2SS!=0:
        s[c2SSidx[i]*3+2]='.'
        s[c2SSidx[i]*3+3]='.'
        if c2SSidx[i]*3+4<len(s):
            s[c2SSidx[i]*3+4]='.'
        c2SS-=1
        ans+=2
        k-=1
        if c2SS==0 or k==0:
            break
############################################
c0=[]
c1=[]
c2=[]
for i in range(0,len(s),3):
    c0.append(s[i:i+3])
c0S=0
c0Sidx=[]
for i in range(len(c0)):
    if c0[i]==['.','S','.'] or c0[i]==['S','.','.'] or c0[i]==['.','.','S'] or c0[i]==['S','.'] or c0[i]==['.','S'] or c0[i]==['S']:
        c0S+=1
        c0Sidx.append(i)
for i in range(k):
    if c0S!=0:
        s[c0Sidx[i]*3]='.'
        if c0Sidx[i]*3+1<len(s):
            s[c0Sidx[i]*3+1]='.'
        if c0Sidx[i]*3+2<len(s):
            s[c0Sidx[i]*3+2]='.'
        c0S-=1
        ans+=1
        k-=1
        if c0S==0 or k==0:
            break

for i in range(1,len(s),3):
    c1.append(s[i:i+3])
c1S=0
c1Sidx=[]
for i in range(len(c1)):
    if c1[i]==['.','S','.'] or c1[i]==['S','.','.'] or c1[i]==['.','.','S'] or c1[i]==['S','.'] or c1[i]==['.','S'] or c1[i]==['S']:
        c1S+=1
        c1Sidx.append(i)
if s[0]=='S' and k!=0:
    ans+=1
    s[0]='.'
for i in range(k):
    if c1S!=0:
        s[c1Sidx[i]*3+1]='.'
        if c1Sidx[i]*3+2<len(s):
            s[c1Sidx[i]*3+2]='.'
        if c1Sidx[i]*3+3<len(s):
            s[c1Sidx[i]*3+3]='.'
        c1S-=1
        ans+=1
        k-=1
        if c1S==0 or k==0:
            break

for i in range(2,len(s),3):
    c2.append(s[i:i+3])
c2S=0
c2Sidx=[]
for i in range(len(c2)):
    if c2[i]==['.','S','.'] or c2[i]==['S','.','.'] or c2[i]==['.','.','S'] or c2[i]==['S','.'] or c2[i]==['.','S'] or c2[i]==['S']:
        c2S+=1
        c2Sidx.append(i)
if s[1]=='S' and k!=0:
    ans+=1
    s[1]='.'
for i in range(k):
    if c2S!=0:
        s[c2Sidx[i]*3+2]='.'
        if c2Sidx[i]*3+3<len(s):
            s[c2Sidx[i]*3+3]='.'
        if c2Sidx[i]*3+4<len(s):
            s[c2Sidx[i]*3+4]='.'
        c2S-=1
        ans+=1
        k-=1
        if c2S==0 or k==0:
            break
print(ans)