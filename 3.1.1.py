num_lines = int(input())
all_games = {}

def move_left(game, i):
    game = list(game)
    game[i] = "-"
    game[i-1] = "-"
    game[i-2] = "o"
    game = "".join(game)
    return game

def move_right(game, i):
    game = list(game)
    game[i] = "-"
    game[i+1] = "-"
    game[i+2] = "o"
    game = "".join(game)
    return game

def rewind_move_left(game, i):
    game = list(game)
    game[i] = "o"
    game[i-1] = "o"
    game[i-2] = "-"
    game = "".join(game)
    return game

def rewind_move_right(game, i):
    game = list(game)
    game[i] = "o"
    game[i+1] = "o"
    game[i+2] = "-"
    game = "".join(game)
    return game

def play(game, all_games):
    min_board = game.count("o")
    if hash(game) in all_games:
        return all_games[hash(game)]
    i = 2
    while i < len(game):
        if game[i] == "o" and game[i-1] == "o" and game[i-2] == "-":
            game = move_left(game, i)
            pebble_count = play(game, all_games)
            if pebble_count < min_board:
                min_board = pebble_count
            game = rewind_move_left(game, i)
        i += 1
    i = 0
    while i < len(game)-2:
        if game[i] == "o" and game[i+1] == "o" and game[i+2] == "-":
            game = move_right(game, i)
            pebble_count = play(game, all_games)
            if pebble_count < min_board:
                min_board = pebble_count
            game = rewind_move_right(game, i)
        i += 1
    
    all_games[hash(game)] = min_board
    return min_board

for line in range(num_lines):
    game = input()
    pebble_min = play(game, all_games)
    print(pebble_min)
