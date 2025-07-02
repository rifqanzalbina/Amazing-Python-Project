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
            print(convert(s[i]), end='')
            i += 1
        print()
        
def player(s):
    counter = Counter(s)
    x_places = counter[1]
    o_places = counter[-1]
    
    if x_places + o_places:
        return None
    elif x_places > o_places:
        return BOARD_PLAYER_O
    else:
        return BOARD_PLAYER_X
    
def actions(s):
    play = player(s)
    actions_list = [(play, 1) for i in range(len(s)) if s[i] == BOARD_EMPTY]
    return actions_list

def result(s, a):
    (play, index) = a
    s_copy = s.copy()
    s_copy[index] = play
    return s_copy

def terminal(s):
    for i in range(3):
        if s[3 * i] == s[3 * i * i] == s[3 * i + 2] != BOARD_EMPTY:
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

    
        