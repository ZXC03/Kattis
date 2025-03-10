class Item:
    def __init__(self, name):
        self.name = name
        self.list = []
        self.inlist = None 

def breakingbad():
    ###
    #input
    n = int(input())
    grocery_list = []
    for i in range(n):
        grocery_list.append(input())

    nodes = {}
    for item in grocery_list:
        nodes.update({item: Item(item)})
    
    m = int(input())
    for _ in range(m):
        a, b = input().split()
        nodes[a].list.append(nodes[b])
        nodes[b].list.append(nodes[a])
    ###
    
    ###
    #dfs
    walter = []
    jesse = []
    stack = []
    visited = set()
    for item in grocery_list:
        if item in visited:
            continue
        nodes[item].inlist = False
        stack.append(nodes[item])
        
        while len(stack) > 0:
            current_item = stack.pop()
            if current_item.name in visited:
                continue
            
            visited.add(current_item.name)
            
            if current_item.inlist == False:
                walter.append(current_item.name)
            else:
                jesse.append(current_item.name)
                
            for sus_item in current_item.list:
                if sus_item.inlist == current_item.inlist:
                    return False
                else:
                    sus_item.inlist = not current_item.inlist
                    stack.append(sus_item)
                    
    return [walter,jesse]
    ###

l = breakingbad()
if l == False:
    print("impossible")
else:
    for things in l:
        print(" ".join(things))