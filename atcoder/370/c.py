S=input()
T=input()
count=0
nS=[ord(char) - ord('a') + 1 for char in S if 'a' <= char <= 'z']
nT=[ord(char) - ord('a') + 1 for char in T if 'a' <= char <= 'z']

sList=list(S)
tList=list(T)
henka1=[]
henka2=[]

for i in range(len(S)):
    if nS[i] > nT[i]:
        henka1.append(i)
    elif nS[i] < nT[i]:
        henka2.append(i)
henka2.reverse()
for i in henka2:
    henka1.append(i)
henka=henka1

print(len(henka))
for i in range(len(henka)):
    sList[henka[i]]=tList[henka[i]]
    print(''.join(sList))


