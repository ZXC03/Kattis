options = input().split()
stone_num = int(options.pop(0))
num_options = int(options.pop(0))

stan_w = [None]*(stone_num+1)

stan_w[0] = False
for i in range(1, stone_num+1):
    stan_w[i] = False
    
    for j in range(num_options):
        if i >= int(options[j]) and stan_w[i-int(options[j])] == False:
            stan_w[i] = True
            break
    
if stan_w[stone_num] == True:
    print("Stan wins")
else:
    print("Ollie wins")
