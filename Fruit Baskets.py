import itertools
import math

total_weight = 0
num_fruits = int(input())
weights = input().split()
for i in range(len(weights)):
    weights[i] = int(weights[i])

r = 1 #need at least one fruit in basket
temp = weights.copy()
large = 0
for i in range(len(temp)):
    largest = max(temp) + large
    if largest >= 200:
        break
    else:
        large += temp.pop(temp.index(max(temp)))
        r += 1

while r < 4 and r < len(weights) + 1: #4+ fruits are necessarily >= 200g
    for comb in itertools.combinations(weights, r):
        if sum(comb) >= 200:
            total_weight += sum(comb)
    r += 1

n = num_fruits
while r < len(weights) + 1:
    num_combs = math.comb(n-1, r-1) #n-1 and r-1 because a given fruit is guaranteed when iterating through the fruits
    for weight in weights:
        total_weight += int(weight*num_combs)
    r += 1
    
print(total_weight)