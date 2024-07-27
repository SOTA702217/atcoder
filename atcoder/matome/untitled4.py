N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

ants = [(X[i], S[i]) for i in range(N)]

ants.sort()

right_positions = []

meetings = 0

for position, direction in ants:
    if direction == '1': 
        right_positions.append(position)
    else:  
       
        for right_position in right_positions:
            if position - right_position <= 2 * T:
                meetings += 1

print(meetings)
