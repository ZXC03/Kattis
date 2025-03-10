n = input()
line1 = input()
line2 = input()

x = 0
true_n = int(n)%2
if len(line1) != len(line2):
    print("Deletion failed")
    
elif true_n == 0:
    if line1 == line2:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
elif true_n == 1:
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            x = "Deletion failed"
    if x == 0:
        print("Deletion succeeded")
    else:
        print("Deletion failed")