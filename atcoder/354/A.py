H=int(input())
count=0
hi=0
s=1
for i in range(100):
    count+=1
    s=2**(count-1)
    hi+=s
    if H<hi:
        break
print(count)