from itertools import permutations

N,K=map(int,input().split())
S=input()

s=set(''.join(p) for p in permutations(S))

def is_palindrome(s):
    return s == s[::-1]

count=0

for string in s:
    flag=0
    for i in range(N-K+1):
        string_s=string[i:i+K]
        if is_palindrome(string_s):
            flag=1
            break
    if flag==0:
        count+=1

print(count)