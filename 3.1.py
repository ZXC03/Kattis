num_lines = int(input())
def move_left(i):
    game[i] = "-"
    game[i-1] = "-"
    game[i-2] = "o"
    return

def move_right(i):
    game[i] = "-"
    game[i+1] = "-"
    game[i+2] = "o"
    return

def play(game, temp, pebbles):
    i = 0
    moved = False
    while i < len(game) and moved == False:
        if game[i] == "o":
            if i > 1 and game[i-1] == "o" and game[i-2] != "o" and temp[i] != "left":
                move_left(i)
                temp[i] = "left"
                has_moved_left = True
                moved = True
            if i < len(game)-2 and game[i+1] == "o" and game[i+2] != "o" and temp[i] != "right":
                temp[i] = "right"
                move_right(i)
                has_moved_right = True
                moved = True
            elif i == len(game)-1:
                new = game.count("o")
                if pebbles > new:
                    pebbles = new
                if "left" not in temp and "right" not in temp:
                    return pebbles
                else:
                    play(game, temp, pebbles)
            else:
                i += 1
                continue
        i += 1
    if moved == True:
        play(game, temp, pebbles)

pebbles = 13
for line in range(num_lines):
    game = list(input())
    if "o" not in game:
        pebbles = 0
    elif "-" not in game:
        pebbles = 12
    elif game.count("o") == 1:
        pebbles = 1
    else:
        temp = game.copy()
        pebbles = 13
        play(game, temp, pebbles)
        if pebbles > 12:
            pebbles = game.count("o")
    print(pebbles)