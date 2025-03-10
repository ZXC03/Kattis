import sys


try:
    num_lines = 0
    queue = []
    stack = []
    priority = []
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
                queue.append(num)
                stack.append(num)
                priority.append(num)   
            elif int(ioo) == 2:
                if queue == [] or stack == [] or priority == []:
                    structure = "impossible"
                else:
                    if num not in queue and num not in priority and num not in stack:
                        structure = "impossible"
                    #priority test
                    if "priority queue" in possibilities and max(priority) != num:
                        possibilities.remove("priority queue")
                    priority.remove(max(priority))
                    #queue test
                    q_value = queue.pop(0)
                    if "queue" in possibilities and q_value!= num:
                        possibilities.remove("queue")
                    #stack test
                    s_value = stack.pop()
                    if "stack" in possibilities and s_value != num:
                        possibilities.remove("stack")
            num_lines -= 1

        if num_lines == 0:
            if len(possibilities) == 0 or structure == "impossible":
                print("impossible")
            elif len(possibilities) == 1:
                print(possibilities[0])
            elif len(possibilities) > 1:
                print("not sure")

            queue = []
            stack = []
            priority = []
            possibilities = ["queue", "priority queue", "stack"]
            structure = None
except:
    pass
