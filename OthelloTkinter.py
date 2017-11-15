#Manasi Shingane 12382221
import tkinter
import OthelloGameLogic2

class First:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._button_pressed  = False
        game_type = tkinter.Label(
            master = self._root_window, text ="FULL VERSION" , font = ('Times', '24', 'bold'))
        game_type.grid(row = 0, column = 0, padx = 20, pady= 20, sticky = tkinter.S)
        end_button = tkinter.Button(master = self._root_window, text = "Start Game", font = ("Times", '24'),
                      command= self._on_button_pressed )
        end_button.grid(row = 1, column = 0, padx= 20, pady= 20, sticky = tkinter.N)

        self._root_window.rowconfigure(0,weight =1)
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def _on_button_pressed(self):
        self._button_pressed = True
        self._root_window.destroy()

    def run(self):
        self._root_window.grab_set()
        self._root_window.wait_window()
        
class Options:
    def __init__(self):
        self.rows= 0
        self.cols= 0
        self.player = ''
        self.win = ''
        self._ok_clicked = False 
        
        self._option_menu = tkinter.Tk()
        self.var1 = tkinter.IntVar()
        self.var2 = tkinter.IntVar()
        self.var3 = tkinter.IntVar()
        self.var4 = tkinter.IntVar()
        
        self._canvas = tkinter.Canvas(master = self._option_menu, width = 100, height = 100,
                                      background = '#ffffff')
        self._canvas.grid(row = 0, column= 0)

        self._option_menu.rowconfigure(0,weight =1)
        self._option_menu.columnconfigure(0,weight =1 )

        self._rows = tkinter.Scale( master = self._canvas, from_ = 4, to = 16, tickinterval = 2,
                         orient  = 'horizontal', length = 500, resolution = 2,
                                    activebackground= '#00ffff',
                                    label = '                                                         Rows',
                                    variable = self.var3, command = self._on_rows_selected  )
        self._rows.grid(row=0, column= 0, padx = 0, pady = 0 ,
                        sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

        self._cols = tkinter.Scale( master = self._canvas, from_ = 4, to = 16, tickinterval = 2,
                         orient  = 'horizontal', length = 500, resolution = 2,
                                    activebackground= '#00ffff',
                                    label = '                                                     Columns',
                                    variable = self.var4, command = self._on_cols_selected)

        self._cols.grid(row =2, column = 0, pady =20)
        self._option_menu.rowconfigure(2,weight =1)
        self._option_menu.columnconfigure(0,weight =1 )
        
        self._player_label = tkinter.Label(master = self._canvas, text= 'Choose first player:')
        self._player_label.grid(row = 3, column = 0, pady = 0)
        self._player_label.rowconfigure(3,weight =1)
        self._player_label.columnconfigure(0,weight =1 )

        self._B = tkinter.Radiobutton(master= self._canvas, text = 'Black', variable = self.var1,
                                      value = 1, command = self._on_player_selected) 
        self._B.grid(row = 4, column = 0)
        self._B.rowconfigure(4,weight =1)
        self._B.columnconfigure(0,weight =1 )

        self._W = tkinter.Radiobutton(master = self._canvas, text = 'White', variable = self.var1,
                                      value = 2, command = self._on_player_selected) 
        self._W.grid(row= 5, column =0, pady = 20)
        self._W.rowconfigure(5,weight =1)
        self._W.columnconfigure(0,weight =1 )

        self._win_label = tkinter.Label(master= self._canvas, text= 'Choose which way to win:')
        self._win_label.grid(row = 6, column= 0, pady=0)
        self._win_label.rowconfigure(6,weight =1)
        self._win_label.columnconfigure(0,weight =1 )

        self._more = tkinter.Radiobutton(master = self._canvas, text='> (More pieces wins)',
                                         variable = self.var2, value = 1, command = self._on_way_to_win) # add command
        self._more.grid(row=7,column=0)
        self._more.rowconfigure(7,weight =1)
        self._more.columnconfigure(0,weight =1 )

        self._less = tkinter.Radiobutton(master = self._canvas, text= '< (Less pieces wins)',
                                         variable = self.var2, value = 2, command = self._on_way_to_win ) # add command
        self._less.grid(row = 8, column = 0)
        self._less.rowconfigure(8,weight =1)
        self._less.columnconfigure(0,weight =1 )

        self.ok_button = tkinter.Button(master = self._canvas, text = 'ok') 
        self.ok_button.grid(row = 9 ,column = 0)
        self.ok_button.rowconfigure(9,weight =1)
        self.ok_button.columnconfigure(0,weight =1 )
        
        self._rows.set(4)
        self._cols.set(4)

        self.ok_button.bind('<ButtonRelease>', self._on_button_pressed)

    def _on_player_selected(self) -> None:
            if self.var1.get() == 1:
                self.player = 'B'
            elif self.var1.get() ==2:
                self.player = 'W'
                
    def get_player(self) -> str:
        '''returns first player'''
        return self.player 
                

    def _on_way_to_win(self) -> None:
            if self.var2.get() == 1:
                self.win = '>'
            elif self.var2.get() == 2:
                self.win = '<'
                
    def get_way2win(self) -> str:
        '''returns how the game will be won'''
        return self.win

    def _on_button_pressed(self,event: tkinter.Event) -> None:
            '''closes window and starts game once button is pressed'''
            self._ok_clicked = True
            self._option_menu.destroy()
            
    def _on_rows_selected(self, new_val: int) -> None:
        self.rows = new_val

    def get_rows(self) -> int:
        ''' returns desired amount of rows'''
        return self.rows

    def _on_cols_selected(self, new_val) -> None:
        self.cols = new_val

    def get_cols(self) -> int:
        '''gets cols'''
        return self.cols


    def run(self):
        self._option_menu.grab_set()
        self._option_menu.wait_window()

class Othello:
    def __init__(self):
        f = First()
        f.run()
        if f._button_pressed:
            op = Options()
            op.run()
            self._rows = int(op.get_rows())
            self._cols = int(op.get_cols())
            self._player = op.get_player()
            self._amount = op.get_way2win()
            self._same_turn = bool
            if op._ok_clicked:
                self._done_pressed = False
                self._done2_pressed = False
                self._x = OthelloGameLogic2.GameState(self._rows,self._cols, self._player, self._amount)
                self.game_window = tkinter.Tk()
                self._canvas = tkinter.Canvas(master= self.game_window, width = 600, height = 600, background = '#00ffff')
                self._canvas.grid(row = 1, columnspan = 3, sticky = tkinter.N + tkinter.S+ tkinter.W + tkinter.E)
                
                self._point_label_B =tkinter.Label(master = self.game_window, text = 'Black:' + str(self._x.count_black()), font = ('Times', '24', 'bold'))
                self._point_label_B.grid(row = 0, column =0, sticky = tkinter.W)

                self._point_label_W =tkinter.Label(master = self.game_window, text = 'White:' + str(self._x.count_white()), font = ('Times', '24', 'bold'))
                self._point_label_W.grid(row = 0, column =2, sticky = tkinter.E)

                if self._player == 'B':
                    self._turn_label =tkinter.Label(master = self.game_window, text = 'Turn: Black', font = ('Times', '24', 'bold'))
                    self._turn_label.grid(row = 0, column = 1, sticky = tkinter.N + tkinter.S+tkinter.W + tkinter.E)

                elif self._player == 'W':
                    self._turn_label =tkinter.Label(master = self.game_window, text = 'Turn: White', font = ('Times', '24', 'bold'))
                    self._turn_label.grid(row = 0, column = 1,  sticky = tkinter.N + tkinter.S+tkinter.W + tkinter.E)

                self.winner_label = tkinter.Label(master = self.game_window, text = 'Winner: ' + self._x._winner, font = ('Times','24', 'bold'))
                self.winner_label.grid(row = 2, column= 1, sticky= tkinter.N + tkinter.S+tkinter.W + tkinter.E)
                                                  

                self.done_button = tkinter.Button(master = self.game_window, text = 'Done', command = self._on_done_pressed)
                self.done_button.grid(row = 3, column = 2, sticky = tkinter.S + tkinter.E)
                

                
                self.game_window.rowconfigure(0,weight =1 )
                self.game_window.columnconfigure(0, weight = 1)
                self.game_window.rowconfigure(1,weight =1 )
                self.game_window.columnconfigure(1,weight =1)
                self.game_window.columnconfigure(2,weight =1)
                self.game_window.rowconfigure(2,weight =1)
                self.game_window.rowconfigure(3, weight = 0)
                self.game_window.columnconfigure(3,weight =0)
                
                
                self._canvas.bind('<Configure>', self._on_canvas_resized)
                self._canvas.bind('<Button-1>', self._on_initial_canvas_clicked)

    def _on_done_pressed(self):
        if self._done2_pressed:
            self.done_button.destroy()
            self._canvas.bind('<Button-1>', self._on_canvas_clicked)
        self._done_pressed = True
        self._x._opposite_turn()
        self._change_turn_labels()

        
    def _on_initial_canvas_clicked(self, event:tkinter.Event):
        '''for initial canvas'''

        if self._done_pressed == True:

            self._done2_pressed = True



            self._done_pressed = False

        desired_row = self.get_square(event.x, event.y)[0]
        desired_col = self.get_square(event.x,event.y)[1]
        self._x._board[desired_row][desired_col] = self._x._turn



        self._redraw_all()
    def _on_canvas_resized(self, event: tkinter.Event):
        '''resizes'''
        self._canvas.delete(tkinter.ALL)

        self._redraw_all()

    def _redraw_all(self) ->  None:
        '''draws canvas'''
        self._change_point_labels()
        canvas_height = self._canvas.winfo_height()
        canvas_width = self._canvas.winfo_width()
        height = canvas_height / self._rows
        wid = canvas_width / self._cols
        for k in range(self._cols):
            self._canvas.create_line(k*wid,0, k*wid, canvas_height, fill = 'black')
        for i in range(self._rows):
            self._canvas.create_line( 0, i*height, canvas_width ,i*height,  fill = 'black')
            for i in range(len(self._x._board)):
                for k in range(len(self._x._board[i])):
                    if self._x._board[k][i] =='W':
                        self._canvas.create_oval(
                            i*wid +5, k*height+5,
                            (i+1)*wid-5,(k+1)*height-5, fill = 'white', outline = 'black')
            for i in range(len(self._x._board)):
                for k in range(len(self._x._board[i])):
                    if self._x._board[k][i] == 'B':
                        self._canvas.create_oval(
                            i*wid +5, k*height+5,
                            (i+1)*wid-5,(k+1)*height-5, fill = 'black', outline = 'black')            
            

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''runs when canvas is clicked'''
        count = 0 
        canvas_height = self._canvas.winfo_height()
        canvas_width = self._canvas.winfo_width()
        height = canvas_height / self._rows
        wid = canvas_width / self._cols

        desired_row = self.get_square(event.x, event.y)[0]

        desired_col = self.get_square(event.x,event.y)[1] 
        if self._x.everything_filled() == True or self._x.one_only():
            self.winner_label.config(text = "Winner: "+ self._x._winner)
            return
        else:
            self._x.check_board_spaces()
            self._x.reassign(desired_row,desired_col)
            if self._x._turn == 'B':
                if (desired_row,desired_col) in self._x._valid_black_moves:
                    self._x._is_valid_black = True
                    self._x._board[desired_row][desired_col] = 'B'                
                else:
                    self._x._is_valid_black = False
            elif self._x._turn == 'W':
                if (desired_row,desired_col) in self._x._valid_white_moves:
                    self._x._is_valid_white = True
                    self._x._board[desired_row][desired_col] = 'W'
                else:
                    self._x._is_valid_white = False

            if count>0 :
                if self._x.one_filled():
                    self._x.no_pos()
            count +=1

            self._redraw_all()

            if self._x._turn == 'B' and  self._x._is_valid_black == False:
                    return

            if self._x._turn == 'W':
                if self._x._is_valid_white == False:
                    return
            self._x._opposite_turn()
            self.print_if_move_valid(event.x,event.y)
            if count>0 :
                if self._x.one_filled():
                    self._x.no_pos()
            if self._x.everything_filled() == True or self._x.no_pos()or self._x.both_filled() or self._x.one_only():
                self.winner_label.config(text = "Winner: "+ self._x._winner)
                self._turn_label.config(text = 'GAME OVER')
                return

            self._change_turn_labels()
            self._change_point_labels()
            print('tkinter black ',self._x._valid_black_moves, '\n' , 'tkinter white ',self._x._valid_white_moves)


        


    def get_square(self,click_x, click_y) -> (int,int):
        '''gets the corresponding square'''
        canvas_height = self._canvas.winfo_height()
        canvas_width = self._canvas.winfo_width()
        row_dist = canvas_height/self._rows
        col_dist = canvas_width/self._cols

        for row in range(self._rows):
            if row*row_dist <= click_y < (row+1)*row_dist:
                click_row = row

        for col in range(self._cols):
            if col*col_dist <= click_x < (col+1)*col_dist:
                click_col = col

        return click_row, click_col

    def _change_point_labels(self):
        '''changes point labels'''
        self._point_label_B.config(text = 'Black:' + str(self._x.count_black()))

        self._point_label_W.config(text = 'White:' + str(self._x.count_white()))

    def _change_turn_labels(self):
        '''changes turn labels'''
        if self._x._turn == 'B':
            self._turn_label.config(text = 'Turn: Black')
        elif self._x._turn == 'W':
            self._turn_label.config(text = 'Turn: White')

 

    def print_if_move_valid( self, x_coor: int, y_coor: int):
        '''Keeps turn if it's invalid'''
        if self._x._turn == 'B':
            if self._x._is_valid_black == True:
                return
            elif self._x._is_valid_black == False:

                    self._x._turn = 'B'
                    desired_row = self.get_square(x_coor, y_coor)[0]
                    desired_col = self.get_square(x_coor,y_coor)[1]
                    

        elif self._x._turn == 'W':
            if self._x._is_valid_white == True:
                return 
            elif self._x._is_valid_white == False:
                    self._x._turn = 'W'
                    desired_row = self.get_square(x_coor, y_coor)[0]
                    desired_col = self.get_square(x_coor,y_coor)[1]                  

                    
        

    def run(self) -> None:
        ''' runs the code'''
        self.game_window.mainloop()


if __name__ == '__main__':
    x = Othello()
    x.run()

