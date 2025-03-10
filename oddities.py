x = input()
list = []
for i in range(int(x)):
    d = input()
    list.append(int(d))
    
for i in range(int(x)):
    if -10 <= list[i] <=10:
        if ((list[i])%2 == 0):
            print(str(list[i])+" is even")
        else:
            print(str(list[i])+" is odd")
    