num = int(input())
dic = {}
for person in range(num):
    name, like, bd = input().split()
    if bd in dic:
        if int(like) > int(dic[bd][1]):
            dic[bd] = (name, like)
    else:
        dic[bd] = (name, like)

arr = []  
for key in dic:
    arr.append(dic[key][0])

arr.sort()
print(len(arr))
for r in range(len(arr)):
    print(arr[r])
    

