import itertools

total_weight = 0
num_fruits = int(input())
weights = input().split()
for i in range(len(weights)):
    weights[i] = int(weights[i])
#for r in range(len(weights)+1):
r = 0
while r < len(weights) + 1:
    for comb in itertools.combinations(weights, r):
        if sum(comb) >= 200:
            total_weight += sum(comb)
    r += 1

print(total_weight)


            