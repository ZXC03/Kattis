num_trees = int(input())
growth_speeds = input().split()
for i in range(num_trees):
    growth_speeds[i] = int(growth_speeds[i])

day_count = []
growth_speeds.sort()
i = 1
while i <= num_trees:
    tree = growth_speeds.pop()
    day_count.append(tree+i)
    i += 1

print(max(day_count)+1)