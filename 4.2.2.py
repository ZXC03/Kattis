options = input().split()
stone_num = int(options.pop(0))
num_options = int(options.pop(0))

stan_w = [0]

#if 1 stone left then stan W
#stan_w[0] = False
for i in range(1, stone_num+1):
    app = False
    #if stone = 1, aka stan_w[1] = True , then Stan W
    #if there exists i - option is L, then that means i is W since i - option is played by Ollie
    #iterate through options to find an option where i - option is L
    for option in options:
        if i >= int(option) and stan_w[i-int(option)] == False:
            app = True
            break
    stan_w.append(app)
    
if stan_w[stone_num] == True:
    print("Stan wins")
else:
    print("Ollie wins")
