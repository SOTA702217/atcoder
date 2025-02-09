n,k=map(int,input().split())
s=list(input())

def max_dod(n,k,s):
    def process(s,k):
        s=s[:]
        ans=s.count('.')

        for i in range(n-2):
            if k==0:
                break

            if s[i:i+3]==['S','S','S']:
                s[i]=s[i+1]=s[i+2]='.'
                ans+=3
                k-=1

        for i in range(n-2):
            if k==0:
                break

            if s[i:i+3] in [['S','S','.'],['S','.','S'],['.','S','S']]:
                s[i]=s[i+1]=s[i+2]='.'
                ans+=2
                k-=1

        for i in range(n-2):
            if k==0:
                break

            if s[i:i+3] in [['S','.','.'],['.','S','.'],['.','.','S']]:
                s[i]=s[i+1]=s[i+2]='.'
                ans+=1
                k-=1

        for i in range(n):
            if k==0:
                break

            if s[i]=='S':
                s[i]='.'
                ans+=1
                k-=1
        
        return ans
    
    fwd=process(s,k)
    s.reverse()
    bwd=process(s,k)
    return max(fwd,bwd)

ans=max_dod(n,k,s)

print(ans)
