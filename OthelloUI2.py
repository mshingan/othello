#Manasi Shingane 1238221
import OthelloGameLogic2


def invalid_row_input(row):
    if row not in [4,6,8,10,12,14,16]:
        raise InvailidRowInput()
    else:
        return row
    
def translate_board(boardLine: str)->str:
    '''translates numbers to corresponding values
    '''
    trans = str.maketrans('01239', '.BW!?')
    return boardLine.translate(trans)

def print_board(board:list) -> None:
    '''prints board so user can see it in readable format
    '''
    for col in range(len(board)):
        new_str = ''
        for row in range(len(board[col])):
            new_str += str(board[col][row]) + ' '
        print(new_str)
    print()
def print_if_move_valid( x:'GameState'):
    if x._turn == 'B':
        if x._is_valid_black == True:
            print('VALID')
            return
        elif x._is_valid_black == False:
            while True:
                print('INVALID')
                x._turn = 'B'
                move= input("Enter desired location: ")
                move_list = move.split()
                row  = int(move_list[0])-1
                col = int(move_list[1])-1
                if (row,col) in x._valid_black_moves:
                    print('VALID')
                    x.reassign(row,col)
                    break
            return
    elif x._turn == 'W':
        if x._is_valid_white == True:
            print('VALID')
            return 
        elif x._is_valid_white == False:
            while True:
                print('INVALID')
                x._turn = 'W'
                move= input("Enter desired location: ")
                move_list = move.split()
                row  = int(move_list[0])-1
                col = int(move_list[1])-1
                if (row,col) in x._valid_white_moves:
                    print('VALID')
                    x.reassign(row,col)
                    break
            return
    
        
def board_input( rows:int, cols:int):
    input_list = []
    board = [] 
    for i in range(rows):
        input_list.append(input().strip())

    for i in input_list:
        board.append(i.split())
    return board

def initial_row():
    '''input for rows'''
    while True:
        try:
            rows =int(input())
            if rows not in [4,6,8,10,12,14,16]:
                raise ValueError
        except ValueError:
            print('invalid')
        else:
            return rows
            break
        
        
def initial_cols():
    '''input for columns'''
    while True:
        try:
            cols =int(input())
            if cols not in [4,6,8,10,12,14,16]:
                raise ValueError
        except ValueError:
            print('invalid')
        else:
            return cols
            break
                  
def initial_first_player():
    '''input for first player '''
    while True:
        try:
            first_player = input().upper()
            if first_player =='B':
                first_player = 'B'
            elif first_player == 'W':
                first_player = 'W'
            else:
                raise Exception 
        except:
            print('invalid')
        else:
            return first_player
        
def initial_who_wins():
    '''input for who wins'''
    while True:
        try:
            who_wins = input().strip()
            if who_wins.strip() =='>':
                who_wins = '>'
            elif who_wins.strip() == '<':
                who_wins = '<'
            else:
                raise Exception
        except:
           print('invalid')
        else:
            return who_wins
            

if __name__ == '__main__':
    print('FULL')
    rows = initial_row()
    cols = initial_cols()
    first_player = initial_first_player()
    who_wins = initial_who_wins()
    board= board_input(rows,cols)
    x =OthelloGameLogic2.GameState(rows,cols,board,first_player, who_wins)
    x.check_validity()
    x.one_filled()
    x.everything_filled()
    x.count_black()
    x.count_white()
    x.no_pos()
    if x.no_places():
        print('WINNER: ', x._winner)
    elif x.everything_filled():
        print('WINNER: ', x._winner)
    elif x.both_filled():
        print('WINNER: ', x._winner)
    else:
            print('B: ', x.count_black(), 'W: ', x.count_white())
            print_board(board)
            print('TURN: ', x._turn)
            move= input()
            move_list = move.split()
            row  = int(move_list[0])-1
            col = int(move_list[1])-1
            x.check_validity()
            x.reassign(row,col)
            x.one_filled()
            if x._turn == 'B':
                if (row,col) in x._valid_black_moves:
                    x._is_valid_black = True
                else:
                    x._is_valid_black = False
            elif x._turn == 'W':
                if (row,col) in x._valid_white_moves:
                    x._is_valid_white = True
                else:
                    x._is_valid_white = False
            print_if_move_valid(x)
            x.reset_white()
            x.reset_black()
            r = x.reassign(row,col)
            x._opposite_turn()
            x.check_validity()
    
            while True:
                print('B: ', x.count_black(), 'W: ', x.count_white())
                print_board(r)
                x.no_pos()
                if x.everything_filled() == True:
                    print('WINNER: ', x._winner)
                    break
                elif x.both_filled() == True:
                    print('WINNER: ', x._winner)
                    break
                x._is_valid_black = bool
                x._is_valid_white = bool
                print('TURN: ', x._turn)
                move= input()
                move_list = move.split()
                row  = int(move_list[0])-1
                col = int(move_list[1])-1
                x.check_board_spaces()
                x.one_filled()
##                if x.both_filled() == True:
##                    print('WINNER: ', x._winner)
##                    break
                if x._turn == 'B':
                    if (row,col) in x._valid_black_moves:
                        x._is_valid_black = True
                    else:
                        x._is_valid_black = False
                elif x._turn == 'W':
                    if (row,col) in x._valid_white_moves:
                        x._is_valid_white = True
                    else:
                        x._is_valid_white = False
                print_if_move_valid(x)
                
                r = x.reassign(row,col)
                x._opposite_turn()
 #               x.no_pos()
                print(x._valid_black_moves, ' ', x._valid_white_moves)
                
        
