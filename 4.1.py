break_num, cost = input().split()
breaks = input().split()

current_max = 0
max_max = 0

j = 0
while j < int(break_num):
    breaks[j] = int(breaks[j])
    current_max = current_max + int(breaks[j]) - int(cost)
    if int(breaks[j])- int(cost) > current_max:
        current_max = int(breaks[j]) - int(cost)
    if current_max > max_max:
        max_max = current_max
    j += 1

print(max_max)
    
