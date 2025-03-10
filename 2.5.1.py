num = int(input())
friendships = int(input())
friend_group = []

for i in range(num):
    for j in range(friendships):
        friendship = input()
        list_ = friendship.split()
        if j == 0:
            friend_group.append(list_[0])
            friend_group.append(list_[1])
        else:
            if list_[0] in friend_group:
                friend_group.append(list_[1])
            elif list_[1] in friend_group:
                friend_group.append(list_[0])
        print(len(friend_group))
        
        if p1 == p2:
            return p1.size

        elif p1.size > p2.size:
            p2.main = p1
            p1.size += p2.size
            return p1.size
        else:
            p1.main = p2
            p2.size += p1.size
            return p2.size
                