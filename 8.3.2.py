s = list(input())

count = [0]*len(s)
for i in range(0, len(s)):
    pattern = s[0:i+1]
    ispattern = True
    if i != 0 and i != len(s):
        for j in range(i+1, len(s), i+1):
            prov = pattern.copy()
            popped = prov.pop()
            prov.insert(0, popped)
            if s[j:j+len(pattern)] != prov:
                    ispattern = False
                    break
            if ispattern == False:
                break
            else:
                pattern = prov
    if ispattern == True:
        count[i] = len(pattern)
        
if len(set(s)) == 1:
    print(1)
elif len(set(s)) == len(s):
    print(len(s))
else:
    count.pop()
    print(max(count))

        
    
