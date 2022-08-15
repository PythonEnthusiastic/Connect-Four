from termcolor import colored
import sys

def board(p_board):
  print(' ',' '.join(str(i) for i in choices))
  for i in p_board:
    print(f" |{'|'.join(i)}|")
  print('\n')

def turn_syntax_validity(p_turn):
  if not (p_turn.isnumeric() and int(p_turn) in choices):
    print('You\'ve entered an invalid anwser')
    return True
  return False

def position_validity(p_turn, p_board):
  for i in p_board[::-1]:
    if i[int(p_turn)-1] == ' ':
      return False
  print('This column is full!\n')
  return True

def replace(p_turn, p_board, p_color):
  for i in p_board[::-1]:
    if i[int(p_turn)-1] == ' ':
      i[int(p_turn)-1] = colored('●', p_color)
      break

def check_win(p_color, p_board):
  for val in p_board:
    if colored('●', p_color)*4 in ''.join(val):
      winner(p_color)
  for i in range(7):
    if colored('●', p_color)*4 in ''.join([p_board[index][i] for index,_ in enumerate(p_board)]):
      winner(p_color)
  for i in range(6):
    for x in range(7):
      if i <= 2:
        check_across_top_part(i,x)
      else:
        check_across_bottom_part(i,x)
        
def check_across_top_part(column,row):
  if row < 3:
    if colored('●', color)*4 in ''.join([game_board[column+shift][row+shift] for shift in range(4)]):
      winner(color)
  elif row > 3:
    if colored('●', color)*4 in ''.join([game_board[column+shift][row-shift] for shift in range(4)]):
      winner(color)
  else:
    if colored('●', color)*4 in ''.join([game_board[column+shift][row+shift] for shift in range(4)]):
      winner(color)
    elif colored('●', color)*4 in ''.join([game_board[column+shift][row-shift] for shift in range(4)]):
      winner(color)

def check_across_bottom_part(column,row):
  if row < 3:
    if colored('●', color)*4 in ''.join([game_board[column-shift][row+shift] for shift in range(4)]):
      winner(color)
  elif row > 3:
    if colored('●', color)*4 in ''.join([game_board[column-shift][row-shift] for shift in range(4)]):
      winner(color)
  else:
    if colored('●', color)*4 in ''.join([game_board[column-shift][row+shift] for shift in range(4)]):
      winner(color)
    elif colored('●', color)*4 in ''.join([game_board[column-shift][row-shift] for shift in range(4)]):
      winner(color)

def winner(p_color):
  print(f'Player {p_color} has won!')
  sys.exit()
  
game_board = [[' ' for i in range(7)] for i in range(6)]
choices = [1,2,3,4,5,6,7]
color = 'red'
counter = 0

print('You can place the place the piece in any of the following columns:\n')
board(game_board)

while True:
  turn = input(f'Player {color}\'s turn, which column do you want to place in? ')

# runs if variable 'turn' is not a number and is not a valid number
  if turn_syntax_validity(turn) or position_validity(turn, game_board): 
    continue

  replace(turn, game_board, color)
  counter += 1
  
  print('\n')
  board(game_board)

  check_win(color, game_board)

  if counter >= 42:
    print('It\'s a tie!')
    sys.exit()
  
  color = 'yellow' if color == 'red' else 'red'
