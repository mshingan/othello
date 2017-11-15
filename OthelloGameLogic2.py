#Manasi Shingane 12382221

class GameState:
    def __init__(self, rows,cols,first_player, who_wins ):
        self._rows = rows
        self._cols = cols
        board  = []
        for i in range(self._rows):
            board.append([])
            for k in range(self._cols):
                board[i].append('.')
        self._board = board
        self._turn = first_player
        self._directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        self._valid_white_moves = set()
        self._valid_black_moves = set()
        self._blackPos = []
        self._whitePos = []
        self._flip_list = set()
        self._flip_list_white = set()
        self._flipper = []
        self._flippy = []
        self._how_winner = who_wins
        self._blckCount = 0
        self._whiteCount = 0
        self._winner = ''
        self._is_valid_white = bool
        self._is_valid_black = bool 


    def get_rows(self) -> int:
        '''returns rows'''
        return self._rows

    def get_cols(self) -> int:
        '''returns columns'''
        return self._cols

    def is_valid_column_num(self, colNum:int) ->bool:
        '''checks to see if column number is within range'''
        return 0 <= colNum < self.get_cols()

    def is_valid_row_num(self, rowNum: int) -> bool:
        '''checks to see if row number is within range'''
        return 0<= rowNum < self.get_rows()

    def _opposite_turn(self):
        if self._turn == 'W':
            self._turn = 'B'
        else:
            self._turn =  'W'
        return self._turn
    
    def black_positions(self)->list:
        '''returns list of positions in board where there are B'''
        for rows in range(len(self._board)):
            for col in range(len(self._board[rows])):
                if self._board[rows][col] == 'B':
                      self._blackPos.append((rows,col))
        return self._blackPos

    def white_positions(self)->list:
        '''returns list of positions in board where there are W'''
        for rows in range(len(self._board)):
            for col in range(len(self._board[rows])):
                if self._board[rows][col] == 'W':
                    self._whitePos.append((rows,col))
        return self._whitePos

    def check_valid_black(self, new_row:int, new_col:int, rowDelta:int, colDelta:int) -> list:
        '''checks to see which spaces are valid for the black player'''

        black_moves = []
    
        if self.is_valid_column_num(new_col) and self.is_valid_row_num(new_row):
            if self._board[new_row][new_col] == 'B':
                pass
            elif self._board[new_row][new_col] == '.':
                pass
            elif self._board[new_row][new_col] == 'W':
                   if self.is_valid_column_num(new_col+colDelta) and self.is_valid_row_num(new_row +rowDelta):
                            new_row = new_row + rowDelta
                            new_col = new_col + colDelta
                            if self._board[new_row][new_col] == '.':
                                black_moves.append((new_row,new_col))
                            else:
                                self.check_valid_black(new_row,new_col,rowDelta,colDelta)
        self._valid_black_moves.update(black_moves)
        return self._valid_black_moves 




    def check_valid_white(self, new_row:int, new_col:int, rowDelta:int, colDelta:int) -> list:
        '''checks to see which spaces are valid for the white player'''
        white_moves = []
        if self.is_valid_column_num(new_col) and self.is_valid_row_num(new_row):
            if self._board[new_row][new_col]== 'W':
                pass
            elif self._board[new_row][new_col] == '.':
                pass
            elif self._board[new_row][new_col] == 'B':
                    if self.is_valid_column_num(new_col+colDelta) and self.is_valid_row_num(new_row +rowDelta):
                            new_row = new_row + rowDelta
                            new_col = new_col + colDelta
                            if self._board[new_row][new_col] == '.':
                                white_moves.append((new_row,new_col))
                            else:
                                self.check_valid_white(new_row,new_col,rowDelta,colDelta)
                                pass

        self._valid_white_moves.update(white_moves)
        return self._valid_white_moves

    def make_flip_list_black(self,row:int,col:int, rowDelta:int, colDelta:int):
        '''makes black flip list'''
        flipper = []
        if self._turn == 'B':
            while self.is_valid_column_num(col) and self.is_valid_row_num(row) and self._board[row][col]!= 'B':
                if self._board[row][col] == 'W':
                    flipper.append((row,col))
                    row = row - rowDelta
                    col = col - colDelta
                elif self._board[row][col] == '.':
                    break               
            if self.is_valid_column_num(col) == False or self.is_valid_row_num(row) == False:
                pass
            elif self._board[row][col] == 'B':
                self._flip_list.update( flipper )

                
    def make_flip_list_white(self,row:int,col:int, rowDelta:int, colDelta:int):
        '''makes white flip_list'''
        flippy = [] 
        while self.is_valid_column_num(col) and self.is_valid_row_num(row) and self._board[row][col] != 'W':
            if self._board[row][col] == 'B':
                flippy.append((row,col))
                row = row - rowDelta
                col = col - colDelta
            elif self._board[row][col] == '.':
                break
            
        if self.is_valid_column_num(col) == False or self.is_valid_row_num(row) == False:
            pass
        elif self._board[row][col] == 'W':
            self._flip_list_white.update( flippy )
            
    def check_validity(self):
        '''checks validitiy'''
        print('function ',self._valid_black_moves, '\n' , self._valid_white_moves)

        for row,col in self.black_positions():
            for i in self._directions:
                new_row  = row + i[0]
                new_col = col +  i[1]
                self.check_valid_black(new_row, new_col, i[0], i[1])
        for row,col in self.white_positions():
            for i in self._directions:
                
                new_row = row + i[0]
                new_col = col + i[1]
                self.check_valid_white(new_row, new_col, i[0], i[1])

    def check_board_spaces(self):
        if self._turn == 'B':
            for row,col in self.black_positions():
                for i in self._directions:
                    self.reset_white()
                    new_row  = row + i[0]
                    new_col = col +  i[1]
                    self.check_valid_black(new_row, new_col, i[0], i[1])
        elif self._turn == 'W':
            for row,col in self.white_positions():
                for i in self._directions:
                    self.reset_black()
                    new_row = row + i[0]
                    new_col = col + i[1]
                    self.check_valid_white(new_row, new_col, i[0], i[1])

    def reassign_board_black(self,desired_row:int, desired_col:int):
            '''reassigns black'''
            if self.is_valid_column_num(desired_col) and self.is_valid_row_num(desired_row):
                if (desired_row, desired_col) in self._valid_black_moves and self._board[desired_row][desired_col] == '.':
                    self._board[desired_row][desired_col] = 'B'
                    for i in self._directions:
                        prev_row = desired_row - i[0]
                        prev_col = desired_col - i[1]
                        self.make_flip_list_black(prev_row,prev_col, i[0], i[1])
                        for i in self._flip_list:
                            row =i[0]
                            col = i[1]
                            self._board[row][col]= 'B'
                            
    def reassign_board_white(self, desired_row:int, desired_col:int):
            '''reassigns white'''
            if self.is_valid_column_num(desired_col) and self.is_valid_row_num(desired_row):
                if (desired_row, desired_col) in self._valid_white_moves and self._board[desired_row][desired_col] == '.':
                    self._board[desired_row][desired_col] = 'W'
                    for i in self._directions:
                        prev_row = desired_row - i[0]
                        prev_col = desired_col - i[1]
                        self.make_flip_list_white(prev_row,prev_col, i[0], i[1])
                        for i in self._flip_list_white:
                            row =i[0]
                            col = i[1]
                            self._board[row][col]= 'W'

            
                        
    def reassign(self, desired_row:int, desired_col:int):
        '''reassigns values'''
        if self._turn == 'W':
            self.reassign_board_white(desired_row,desired_col)
        elif self._turn == 'B':
            self.reassign_board_black(desired_row,desired_col)
        
        return self._board
                        
                    

    
    def count_black(self):
        '''counts the black'''
        black_count  = 0
        for rows in self._board:
            for i in rows:
                if i == 'B':
                    black_count += 1
        self._blckCount  = black_count
        return self._blckCount

    def count_white(self):
        '''counts the white'''
        white_count = 0
        for rows in self._board:
            for i in rows:
                if i == 'W':
                    white_count += 1
        self._whiteCount = white_count
        return self._whiteCount
                

    def winner(self):
        '''assigning the winner'''
        if self._how_winner == '>':
            if self._blckCount > self._whiteCount:
                self._winner = 'B'
            elif self._whiteCount > self._blckCount:
                self._winner = 'W'
            else:
                self._winner = 'NONE'
        elif self._how_winner == ',':
            if self._blckCount < self._whiteCount:
                self._winner = 'B'
            elif self._whiteCount < self._blckCount:
                self._winner = 'W'
            else:
                self._winner = 'NONE'
                
    def everything_filled(self):
        '''if there are no more empty spaces'''
        num =0
        for rows in self._board:
            for cols in rows:
                if cols == '.':
                    num +=1
        if num == 0:
            self.winner()
            return True
        else:
            return False


    def one_filled(self) -> bool:
        '''if one set is filled, but turn has no valid moves'''
        count =0
        if self._turn == 'B':
            if self._valid_black_moves == set():
                self.check_board_spaces()
                if self._valid_black_moves != set():
                    pass
                else:
                    self.reset_black()
                    self._turn = 'W'
                    self.check_board_spaces()
                    if self._valid_white_moves != set():
                        count +=1
                        if count > 0:
                            self.reset_white()
                            self.check_board_spaces()
                        return True
                        
                    else:
                        self._turn = 'B'
                        self.check_board_spaces()
                        self.winner()
                        return False
            else:
                pass
        elif self._turn == 'W':
            if self._valid_white_moves == set():
                    self.check_board_spaces()
                    if self._valid_white_moves != set():
                        pass
                    else:
                        self.reset_white()
                        self._turn = 'B'
                        self.check_board_spaces()
     #                   self.reset_black()
                        if self._valid_black_moves != set():
                            count +=1
                            if count >0:
                                self.reset_black()
                                self.check_board_spaces()

                            return True
                        
                        else:
                            self._turn = 'W'
                            print('turn is white')
                            self.check_board_spaces()
                            self.winner()
                            return False
            else:
                pass
    def both_filled(self):
        '''if no sets are filled'''
        print('black frm both ', self._valid_black_moves)
        print('white ', self._valid_white_moves)
        if self._valid_black_moves == set() and self._valid_white_moves == set() and not self.one_filled():
            self.winner()
            return True
        else:
            return False 
    def reset_black(self):
        '''resets_black'''
        self._valid_black_moves = set()
        self._flip_list = set()
        

    def reset_white(self):
        self._valid_white_moves = set()
        self._flip_list_white = set()

    def no_pos(self):
        '''if there are no positions'''
        if self._blckCount !=0 and self._whiteCount == 0:
            self.winner()
            self.reset_black()
            self.both_filled()
        elif self._whiteCount !=0 and self._blckCount ==0:
            self.reset_white()
            self.both_filled()
        else:
            pass
    def no_places(self):
        if self._blckCount == 0 and self._whiteCount == 0:
            self.winner()
            return True
        else:
            return False

    def one_only(self):
        if self.count_black() !=0 and self.count_white() == 0:
            self.winner()
            return True
        elif self._whiteCount !=0 and self._blckCount == 0:
            self.winner()
            return True
        else:
            return False
            
        
        
    
    
                
        
