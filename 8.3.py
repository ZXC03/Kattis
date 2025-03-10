s = list(input())

count = [0]*len(s)
for i in range(0, len(s)):
    pattern = s[0:i+1]
    ispattern = True
    #for each set of i numbers after i
    if i != 0:
        for j in range(i+1, len(s), i+1):
            prov = pattern.copy()
            for letter in s[j:j+len(pattern)]:
                if letter not in prov:
                    ispattern = False
                    break
                else:
                    prov.remove(letter)
            if ispattern == False:
                break
    if ispattern == True and i+1 <= len(s)//2:
        count[i] = len(pattern)

print(len(s)//max(count))
    