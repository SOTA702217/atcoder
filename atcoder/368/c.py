N = int(input())
H = list(map(int, input().split()))

T = 0  

for health in H:

    cycle_position = (T % 3)
    
    full_cycles = max((health - (3 - cycle_position) % 3 * 1 - (cycle_position == 0) * 2) // 5, 0)

    damage = full_cycles * 5
    
    T += full_cycles * 3
    
    remaining_health = health - damage
    while remaining_health > 0:
        T += 1
        if T % 3 == 0:
            remaining_health -= 3
        else:
            remaining_health -= 1

print(T)

