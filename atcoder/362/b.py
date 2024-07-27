xa,ya=map(int,input().split())
xb,yb=map(int,input().split())
xc,yc=map(int,input().split())

ab=(xa-xb)**2+(ya-yb)**2
ac=(xa-xc)**2+(ya-yc)**2
cb=(xc-xb)**2+(yc-yb)**2

if ab+ac==cb or cb+ac==ab or ab+cb==ac:
    print('Yes')
else:
    print('No')
    