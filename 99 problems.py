num = int(input())
if num < 149:
    num_99 = 99
else:
    num_99 = (round((num+1.01)/100)*100)-1

print(num_99)