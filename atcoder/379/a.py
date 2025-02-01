N=input()
A=[]
B=[]

A.append(N[1])
A.append(N[2])
A.append(N[0])

B.append(N[2])
B.append(N[0])
B.append(N[1])

print(''.join(A),''.join(B))