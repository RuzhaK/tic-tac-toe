
import game


def start_game():
    game_board, current_player, next_player = game.setup()
    game.loop(game_board,current_player,next_player)

start_game()