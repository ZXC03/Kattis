x = input().split()
l = int(x[0])-12
dist = int(x[1])
bird_num = int(x[2])

birds = []
for i in range(bird_num):
    birds.append(int(input())-6)
initial = len(birds)

birds.sort()
counter = 0
j = 0
if bird_num == 0:
    counter = l//dist + 1
else:
    for position in birds:
        while not (position-dist < j):
            j += dist
            counter += 1
        j = position + dist
    counter += (l-position)//dist

print(counter)