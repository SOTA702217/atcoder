n,t=map(int,input().split())
l=[]
r=[]
for i in range(n):
    l_i,r_i=map(int,input().split())
    l.append(l_i)
    r.append(r_i)

L=int(input())
ans=L
v_min=sum(r)+1
print(v_min)
