def breakingbad():
    n = int(input())
    grocery_list = []
    for i in range(n):
        grocery_list.append(input())
    i = 0

    sus = int(input())
    dic = {}
    verdict = None
    for i in range(sus):
        item = input().split()
        if item[0] in dic.keys():
            dic[item[0]]+= [item[1]]
        else:
            dic.update({item[0]: [item[1]]})
        if item[1] in dic.keys():
            dic[item[1]]+= [item[0]]
        else:
            dic.update({item[1]: [item[0]]})
    
    walter = []
    jesse = []
    for item in grocery_list:
        if item in dic.keys():
            check_w = any(thing in dic[item] for thing in walter)
            if check_w == True:
                check_j = any(thing in dic[item] for thing in jesse)
                if check_j == True:
                    return False
                else:
                    jesse.append(item)
            else:
                walter.append(item)
        else:
            walter.append(item)
    verdict = [walter, jesse]
    return verdict

l = breakingbad()
if l == False:
    print("impossible")
else:
    for things in l:
        print(" ".join(things))
                        
                    
                    
    
