#二つの四角形が重なっているかどうかを判定するプログラムを作成してください。
# ax1 ay1 bx1 by1 cx1 cy1 dx1 dy1 ax2 ay2 bx2 by2 cx2 cy2 dx2 dy2で与えられる。
# ax1 ay1 bx1 by1 cx1 cy1 dx1 dy1は1つ目の四角形の座標、ax2 ay2 bx2 by2 cx2 cy2 dx2 dy2は2つ目の四角形の座標である。

S=list(map(int,input().split()))

q1=[(S[0],S[1]),(S[2],S[3]),(S[4],S[5]),(S[6],S[7])]
q2=[(S[8],S[9]),(S[10],S[11]),(S[12],S[13]),(S[14],S[15])]
