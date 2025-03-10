x = input().split()
num_socks = int(x[0])
capacity = int(x[1])
max_diff = int(x[2])
socks = input().split()
for i in range(num_socks):
    socks[i] = int(socks[i])

socks.sort()
i = 1
num_washers = 1
socks_in_washer = 1
lowest_sock = socks[0]

while i < num_socks:
    if abs(socks[i] - lowest_sock) > max_diff or socks_in_washer >= capacity:
        socks_in_washer = 0
        num_washers += 1
        lowest_sock = socks[i]
        
    socks_in_washer += 1
    i += 1

print(num_washers)