def findlps(subs, subs_l, lps):
    i,l = 1,0
    while i < subs_l and l < subs_l:
        if subs[i] == subs[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def findsubstring(subs, s):
    subs_l,s_l = len(subs),len(s)
    array = [0]*subs_l
    lps = findlps(subs, subs_l, array)
 
    i,j = 0,0 
    while (s_l - i) >= (subs_l - j):
        if subs[j] == s[i]:
            i += 1
            j += 1
        if j == subs_l:
            print(i-j)
            j = lps[j-1]
        elif subs[j] != s[i] and i < s_l:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
#findsubstring("peek a boo", "you speek a bootiful language")
         
while True:
    try:
        subs = input()
        s = input()
        findsubstring(subs, s)
    except:
        break
    
