a, b = input().split()
num_clients = int(a)
time_until_close = int(b)
money = [None]*num_clients
time = [None]*num_clients
for j in range(num_clients):
    a, b = input().split()
    money[j] = int(a)
    time[j] = int(b)

time = [x for _, x in sorted(zip(money, time))]
time.reverse()
money.sort(reverse=True)
arr = [None]*time_until_close
best_arr = [None]*time_until_close
for k in range(num_clients):
    l = time[k]
    if arr[time[k]] == None:
        best_arr[time[k]] = money[k]
        arr[time[k]] = time[k]
    else:
        while l >= 0:
            if arr[l] == None:
                best_arr[l] = money[k]
                arr[l] = time[k]
                break
            else:
                l -= 1

sum_money = 0
for m in range(len(best_arr)):
    if best_arr[m] != None:
        sum_money += best_arr[m]
        
print(sum_money)