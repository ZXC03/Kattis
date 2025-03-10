import sys

num_lines = 0
possibilities = ["queue", "priority queue", "stack"]
lines = []
add = []
remove = []
trav =  []
num = 1

for char in sys.stdin:
    if char == "/n":
        break
    char = char[:-1]
    if len(char) != 1:
        char = char.split()
        if int(char[0]) == 1:
            add.append(char[1])
        elif int(char[0]) == 2:
            remove.append(char[1])
    else:
        if remove == []:
            ans = "impossible"
        else:
            for i in range(len(remove)):
                if add == [] or remove[i] not in add:
                    ans = "impossible"
                    break
                elif i > 0 and remove[i] > remove[i-1] and "priority queue" in possibilities:
                    possibilities.remove("priority queue")
                trav.append(add.index(remove[i]))
            for i in range(len(trav)):
                if i > 0 and trav[i]-trav[i-1]==1 and "stack" in possibilities:
                    possibilities.remove("stack")
                elif i > 0 and trav[i]-trav[i-1]==-1 and "queue" in possibilities:
                    possibilities.remove("queue")

            if len(possibilities) == 1:
                ans = possibilities[0]
            elif len(possibilities) > 1:
                ans = "not sure"
            elif len(possibilities) == 0:
                ans = "impossible"
            
        num = int(char)
print(ans)

