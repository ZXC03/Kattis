x = input()
list = []
y = input()
list_y = y.split()
length = len(list_y)
count = 0

for i in range(length):
    if int(list_y[i]) < 0:
        count = count+1
        
print(count)