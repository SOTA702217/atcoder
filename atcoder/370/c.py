# 問題文
# 英小文字からなる文字列 
# S,T が与えられます。ここで、
# S と 
# T の長さは等しいです。

# X を空の配列とし、以下の操作を 
# S と 
# T が等しくなるまで繰り返します。

# S の文字を 
# 1 文字書き換え、
# X の末尾に 
# S を追加する。
# こうして得られる文字列の配列 
# X のうち要素数最小のものを求めてください。要素数最小のものが複数考えられる場合は、そのうち辞書順最小のものを求めてください。

# 文字列の配列の辞書順とは
# 制約
# S,T は英小文字からなる長さ 
# 1 以上 
# 100 以下の文字列
# S と 
# T の長さは等しい
# 入力
# 入力は以下の形式で標準入力から与えられる。

# S
# T
# 出力
# 答えの要素数を 
# M として 
# M+1 行出力せよ。

# 1 行目には 
# M の値を出力せよ。

# i+1(1≤i≤M) 行目には答えの 
# i 番目の要素を出力せよ。

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


