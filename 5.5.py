n = int(input())
balloon_heights = input().split()
for i in range(n):
    balloon_heights[i] = int(balloon_heights[i])

arrows = []
i = 0
counter = 0
while i < len(balloon_heights):
    current_arrow = balloon_heights[i]
    existing_arrow = balloon_heights[i]+1
    if existing_arrow not in arrows:
        arrows.append(current_arrow)
        counter += 1
    else:
        arrows[arrows.index(existing_arrow)] = current_arrow
    i += 1

print(len(arrows))