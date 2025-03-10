import sys
for line in sys.stdin:
    options = line.split()
    stone_num = int(options.pop(0))

    num_options = int(options.pop(0))
    for i in range(num_options):
        options[i] = int(options[i])
    options.sort(reverse=True)
    max_option = max(options)

    #memory to dp
    stan_w = [False]*(stone_num+1)

    #if 0 stones left then stan L, if 1 then stan W
    stan_w[0] = False
    stan_w[1] = True

    for i in range(2, stone_num+1):    
        #if there exists i - option is L, then that means i is W since i - option is played by Ollie
        #iterate through options to find an option where i - option is L
        #start with max for speed
        if i >= max_option and stan_w[i-max_option] == False:
            stan_w[i] = True
        else:
            for j in range(num_options):
                if i >= options[j] and stan_w[i-options[j]] == False:
                    stan_w[i] = True
                    break
        
    if stan_w[stone_num] == True:
        print("Stan wins")
    else:
        print("Ollie wins")

