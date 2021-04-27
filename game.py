import board
import player

def setup():
    player_1 = player.create()
    player_2 = player.create()

    player.assign_names(player_1, player_2)
    player.assign_symbols(player_1, player_2)


    game_board = board.create()
    board.print_instructions(game_board)

    current_player = player_1
    next_player = player_2

    print(f"{player.get_name(current_player)} starts first!")
    return game_board,current_player,next_player

def loop(game_board,current_player, next_player):
    while True:
        existing_moves=board.get_existing_moves(game_board)
        move=player.pick_move(current_player,existing_moves)
        # ask p1 about move


        board.add_move_to_board(game_board, move, player.get_symbol(current_player))

        board.print_board(game_board)

        if board.has_won(game_board, player.get_symbol(current_player)):
            print(f"{player.get_name(current_player)} has won!")
            break

        # switch players
        current_player, next_player = next_player, current_player