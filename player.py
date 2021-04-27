import config


def create():
    return {}

def get_name(player):
    return player["name"]

def get_symbol(player):
    return player["symbol"]

def assign_names(*players):
    for i in range(len(players)):
        msg="Player "
        if i==0:
            msg+="one"
        else:
            msg+="two"
        msg+=" name:"
        players[i]['name'] = input(msg)

def pick_valid_symbol(player_name):

    while True:
        current_symbol = input(f"{player_name} would like to play with X or 0?")
        if current_symbol in ["X", "0"]:
            return current_symbol
        else:
            print("Please select X or 0")

def assign_symbols(*players):
    player_1,player_2=players

    player_1["symbol"] = pick_valid_symbol(get_name(player_1))
    player_2["symbol"] = '0' if player_1["symbol"] == 'X' else 'X'

def pick_move(player, existing_moves=[]):
    while True:
        current_move=int(input(f"{get_name(player)} choose a free position [1-9]: "))
        if current_move in existing_moves:
            print("This move is already made.")
        elif 1<=current_move<=config.BOARD_SIZE*config.BOARD_SIZE:

            return current_move
        print(f"Pick a valid move from 1 to {config.BOARD_SIZE**2}")