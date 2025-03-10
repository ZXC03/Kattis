n = int(input())
strings = []
for i in range(n):
    strings.append(input())

for s in strings:
    seen = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j] in s[0:j] or s[i:j] in s[i:len(s)]:
                seen.add(s[i:j])
    print(len(seen))
