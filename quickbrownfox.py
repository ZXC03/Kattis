x = input()
if 1 <= int(x) <= 50:
    list_ = []
    for i in range(int(x)):
        d = input()
        if 1 <= len(d) <= 100:
            list_.append(d)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list2 = [[] for i in range(int(x))]

for j in range(len(list_)):
    for i in range(len(alphabet)):
        if alphabet[i] not in list_[j] and alphabet[i].upper() not in list_[j]:
            list2[j].append(alphabet[i])
    if len(list2[j]) > 0:
        print("missing "+"".join(list2[j]))
    else:
        print("pangram")
        