import config
import math
def create():
   return [[" "] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]

def print_instructions(board):
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")

def add_move_to_board(board,move,symbol):
    i=math.ceil(move/3)-1
    j=(move-1)%config.BOARD_SIZE
    board[i][j]=symbol


def print_board(board):
    print("")
    for row in board:
        print(''.join(f'| {x} ' for x in row),end='')
        print("|")


def all_values_same_in_list(row,symbol):
    return all(map(lambda x:x==symbol, row))


def has_won(game_board,symbol):
    rows=[all_values_same_in_list(row,symbol)
          for row in game_board]
    cols=[[game_board[j][i] for j in range(config.BOARD_SIZE)]
          for i in range(config.BOARD_SIZE)]
    cols = [all_values_same_in_list(col, symbol)
            for col in cols]

    primary_diag=[game_board[i][j]
                  for i in range(config.BOARD_SIZE)
                  for j in range(config.BOARD_SIZE)
                  if i==j ]
    primary_diag=all_values_same_in_list(primary_diag,symbol)

    secondary_diag = [game_board[i][j]
                      for i in range(config.BOARD_SIZE)
                      for j in range(config.BOARD_SIZE)
                      if j == config.BOARD_SIZE-i-1]
    secondary_diag=all_values_same_in_list(secondary_diag,symbol)

    return any([*rows,*cols,primary_diag,secondary_diag])

def get_existing_moves(game_board):
    existing_moves=[(i,j) for i in range(config.BOARD_SIZE) for j in range(config.BOARD_SIZE) if game_board[i][j]!=" "]
    return list(map(lambda x:(x[0]*config.BOARD_SIZE)+(x[1]%config.BOARD_SIZE)+1,existing_moves))
