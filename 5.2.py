num_cases = int(input())
for i in range(num_cases):
    num_coor = int(input())
    v1 = input().split()
    v2 = input().split()
    for j in range(num_coor):
        v1[j] = int(v1[j])
        v2[j] = int(v2[j])
    v1.sort()
    v2.sort(reverse=True)
    scalar = [None]*num_coor
    for j in range(num_coor):
        scalar[j] = v1.pop()*v2.pop()
    print("Case #"+str(i+1)+": "+str(sum(scalar)))
        