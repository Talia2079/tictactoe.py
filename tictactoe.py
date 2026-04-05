import tkinter as tk 
from tkinter import font 
  
  
class TicTacToeBoard(tk.Tk): 
    def __init__(self):
        super().__init__() 
         
        self.title("Tic Tac Toe") 
        self.configure(bg="blue") 
         
        self.current_player = "X"
        self.cells = {} 
        
        self._create_header() 
        self._create_board()
        self._create_footer() 
         
        # Header section 
    def _create_header(self): 
            header = tk.Frame(self, bg="#E0FFFF", pady=10) 
            header.pack(fill= "x") 
             
            self.display = tk.Label( 
                text= "Player X's Turn",
                bg="#FFB6C1",
                fg="#2F4F4F", 
                font=font.Font(size=22, weight="bold"), 
            )
            self.display.pack() 
            
    def _create_board(self): 
        self._cells = {}
        board_frame = tk.Frame(self, bg="thistle", padx=20, pady=20)
        board_frame.pack()
           
        pastel_cells =["#FFD6E8", "#D6F0FF", "#E6FFE6"]
          
        for row in range(3): 
            for col in range(3):
                button = tk.Button(
                    board_frame,
                    text="", 
                    font=font.Font(size=32, weight="bold"),
                    width=4,  
                    height=2,
                    bg=pastel_cells[(row+col)% 3],
                    activebackground="#FFF2CC", 
                    relief= "ridge", 
                    bd=3, 
                    command=lambda r=row, c=col: self.play_move(r, c),
                )  
                 
                button.grid(row=row, column=col, padx=8, pady=8) 
                self._cells[(row,col)] = button 
                
    def _create_footer(self): 
        footer= tk.Frame(self, bg="#E8DAFF")
        footer.pack(fill= "x") 
        
        restart_btn = tk.Button( 
            footer,
            text="Restart Button", 
            font=("Arial",12, "bold"), 
            bg="#C7CEEA", 
            fg="Green", 
            command=self.restart_game, 
            )  
        restart_btn.pack() 
        
    def play_move(self, row,col):
        button = self._cells[(row, col)]  
          
        if button["text"] == "":
            button["text"] = self.current_player  
            button["fg"] = "#FF6B9A" if self.current_player == "X" else "#4D96FF"
            if self.check_winner(): 
                self.display["text"] = f" player{self.current_player} Wins!"
                self.display_board()
                  
            elif self.is_draw(): 
                self.display["text"] = "It's a Draw!"
            else: 
                self.switch_player() 
                
    def switch_player(self): 
        self.current_player = "o" if self.current_player == "X" else "X" 
        self.display["text"] = f"player {self.current_player}'s Turn" 
         
    def check_winner(self): 
        board=[[self._cells[(r, c)]["text"]for c in range(3)] for r in range(3)] 
        
        for row in board: 
            if row[0] == row[1] == row[2] != "":
                 return True 
              
        for col in range(3): 
            if board[0][col] == board[1][col] == board[2][col] != "": 
                  return True 
               
            if board[0][0] == board[1][1] == board[2][2] != "": 
                  return True 
              
            if board[0][2] == board[1][1] == board[2][0] != "":
                  return True 
              
            return False  
        
    def is_draw (self): 
        return all(btn["text"] != "" for btn in self._cells.values())
     
    def disable_board(self):
        for button in self._cells.values(): 
            button.configure(state= "disabled")
              
    def restart_game(self): 
        self.current_player = "X" 
        self.display["text"] = "Player x's Turn"
          
        for button in self ._cells.values(): 
            button.configure(text="", state="normal") 
             
              
if __name__ == "__main__": 
    game = TicTacToeBoard()  
    game.mainloop()
        