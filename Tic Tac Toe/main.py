from collections import Counter


BOARD_EMPTY = 0
BOARD_PLAYER_X = 1
BOARD_PLAYER_O = -1

def print_board(s):
  def convert(num):
    if num == BOARD_PLAYER_X:
      return 'X'
    if num == BOARD_PLAYER_O:
      return 'O'
    return '_'

  i = 0
  for _ in range(3):
    for _ in range(3):
      print(convert(s[i]), end=' ')
      i += 1
    print()
    

def player(s):
  counter = Counter(s)
  x_places = counter[1]
  o_places = counter[-1]

  if x_places + o_places == 9:
    return None
  elif x_places > o_places:
    return BOARD_PLAYER_O 
  else:
    return BOARD_PLAYER_X

def actions(s):
  play = player(s)
  actions_list = [(play, i) for i in range(len(s)) if s[i] == BOARD_EMPTY]
  return actions_list

def result(s, a):
  (play, index) = a
  s_copy = s.copy()
  s_copy[index] = play
  return s_copy

def terminal(s):
  for i in range(3):
    if s[3 * i] == s[3 * i + 1] == s[3 * i + 2] != BOARD_EMPTY:
      return s[3 * i]
    if s[i] == s[i + 3] == s[i + 6] != BOARD_EMPTY:
      return s[i]

  if s[0] == s[4] == s[8] != BOARD_EMPTY:
    return s[0]
  if s[2] == s[4] == s[6] != BOARD_EMPTY:
    return s[2]

  if player(s) is None:
    return 0
    
  return None

def utility(s):
  term = terminal(s)
  if term is not None:
    return term
    
  action_list = actions(s)
  utils = []
  for action in action_list:
    new_s = result(s, action)
    utils.append(utility(new_s))

  score = utils[0]
  play = player(s)
  if play == BOARD_PLAYER_X:
    for i in range(len(utils)):
      if utils[i] > score:
        score = utils[i]
  else:
    for i in range(len(utils)):
      if utils[i] < score:
        score = utils[i]
  return score


def utility(s, cost):
  term = terminal(s)
  if term is not None:
    return (term, cost)
    
  action_list = actions(s)
  utils = []
  for action in action_list:
    new_s = result(s, action)
    utils.append(utility(new_s, cost + 1))

  score = utils[0][0]
  idx_cost = utils[0][1]
  play = player(s)
  if play == BOARD_PLAYER_X:
    for i in range(len(utils)):
     if utils[i][0] > score:
       score = utils[i][0]
       idx_cost = utils[i][1]
  else:
    for i in range(len(utils)):
      if utils[i][0] < score:
        score = utils[i][0]
        idx_cost = utils[i][1]

  return (score, idx_cost) 

def minimax(s):
  action_list = actions(s)
  utils = []
  for action in action_list:
    new_s = result(s, action)
    utils.append((action, utility(new_s, 1)))

  if len(utils) == 0:
    return ((0, 0), (0, 0))

  sorted_list = sorted(utils, key=lambda l : l[0][1])
  action = min(sorted_list, key = lambda l : l[1])
  return action

if __name__ == '__main__':
  s = [BOARD_EMPTY for _ in range(9)]
  print('|------- WELCOME TO TIC TAC TOE -----------|')
  print('You are X while the Computer is O')

  while terminal(s) is None:
    play = player(s)
    if play == BOARD_PLAYER_X:
      print('\n\nIt is your turn', end='\n\n')
      x = int(input('Enter the x-coordinate [0-2]: '))
      y = int(input('Enter the y-coordinate [0-2]: '))
      index = 3 * x + y
    
      if not s[index] == BOARD_EMPTY: 
        print('That coordinate is already taken. Please try again.')
        continue
      
      s = result(s, (BOARD_PLAYER_X, index))
      print_board(s)
    else:
      print('\n\nThe is computer is playing its turn')
      action = minimax(s)
      s = result(s, action[0])
      print_board(s)

  winner = terminal(s)
  if winner == BOARD_PLAYER_X:
    print("You have won!")
  elif winner == BOARD_PLAYER_O:
    print("You have lost!")
  else:
    print("It's a tie.")