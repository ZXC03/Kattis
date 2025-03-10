import sys

num_lines = 0
add = []
remove = []
possibilities = ["queue", "priority queue", "stack"]
structure = None

for line in sys.stdin:
#for line in sys.stdin.read():
    if line == "" or line == "\n" or len(line) == 0:
        break
    line = line[:-1]

    if len(line) == 1:
        num_lines = int(line)
        if num_lines == 1:
            structure = "impossible"

    else:
        ioo, num = line.split()
        if int(ioo) == 1:
            add.append(num)
        elif int(ioo) == 2:
            remove.append(num)    
        num_lines -= 1

    if num_lines == 0:
        if add == [] or remove == []:
            structure = "impossible"
        else:
            priority_test = add.copy()
            for i in range(len(remove)):
                if remove[i] not in add:
                    structure = "impossible"
                #priority test
                if len(priority_test) != 0 and max(priority_test) == remove[i]:
                    priority_test.remove(max(priority_test))
                elif "priority queue" in possibilities:
                    possibilities.remove("priority queue")
                #queue test
                if "queue" in possibilities and add[i] != remove[i]:
                    possibilities.remove("queue")
                #stack test
                if "stack" in possibilities and add[-(i+1)] != remove[i]:
                    possibilities.remove("stack")

        if len(possibilities) == 0 or structure == "impossible":
            print("impossible")
        elif len(possibilities) == 1:
            print(possibilities[0])
        elif len(possibilities) > 1:
            print("not sure")

        add = []
        remove = []
        possibilities = ["queue", "priority queue", "stack"]
        structure = None
