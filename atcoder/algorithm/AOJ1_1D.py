n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
maxi=a[1]-a[0]
mini=a[0]
for i in range(1,n):
    if mini>a[i-1]:
        mini=a[i-1]
    profit=a[i]
    if maxi<profit-mini:
        maxi=profit-mini
print(maxi)