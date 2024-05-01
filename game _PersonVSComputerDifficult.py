import math 
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner = None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
        #primero: for i in range(3) genera numeros para i. i=0 ,i=1 ,i=2 en cada iteracion. En total 3.
        #segundo: [i*3:(i+1)*3] esta diciendo que dentro de la propiedad self.board apuntemos a sus 
        #posiciones [0*3 : (0+1)*3] --> [0:3] iteracion 1;;; [1*3 : (1+1)*3] --> [3:6]; [2*3 : (2+1)*3]-->[6:9]
        #Tablero
        #[ 0 1 2 ]
        #[ 3 4 5 ]
        #[ 6 7 8 ]
        #tercero: dentro del for row in .... estamos diciendo en la iteracion 1: row = [0 1 2] del tablero self.board
            print('| '+' | '.join(row)+' |')
            
    @staticmethod
    def print_board_nums():
        #| 0 | 1 | 2 |
        number_board= [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        #j for j in range(3)  => [0, 1, 2]
        #(j+3, (j+1)*3)] for j in range(3)  => [(3, 3), (4, 6), (5, 9)]
        #[str(i) for i in range(j+3, (j+1)*3)] for j in range(3)  => [[], [4, 5], [5, 6, 7, 8]]
        #for j in range(3):
        #   for i in range(j+3, (j+1)*3)):
        #       str(i)  (genera ==> j=0 : (3,3) --> range(3,3) --> no llega a generar nada da una lsita vacia)
        #               (j=1 : range(4,6) --> genera la sgte lista: [4,5]) .. y asi con el j=2
        for row in number_board:
            print('| '+' | '.join(row)+' |')
            
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot==' ']
        #moves = []
        #for (i,spot) in enumerate(self.board):
            #['x','x','o'] --> [(0,'x'), (1,'x'), (2,'o')]
        #    if spot==' ':
        #        moves.append(i)
        #return moves
        
    def empty_squares(self):
        return ' ' in self.board #this returns a boolean
    
    def num_empty_sqares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move, then make the move(assign square to a letter)
        #then return true. if invalid, return false.
        if self.board[square]==' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #winner if 3 in a row anwhere.. we have to check all of these!
        #first let's check the row
        row_ind = square //3 #the // is seying how manuy time that 3 is going into square
        row=self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
        #for every spot in the row we are checking 
        #whether or not that spot equals the letter
            return True
        
        #check column
        col_ind = square %3
        column= [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            #if everysignle spot equals a letter in the column then...           
            return True
        
        #check diagonals
        #but only if the square is an even number (0,2,4,6,8)
        #these are the only moves possible to win a diagonal
        if square %2 == 0:
            diagonal1=[self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
            #if everysignle spot equals a letter in the diagonal1 then...           
                return True
            diagonal2=[self.board[i] for i in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
            #if everysignle spot equals a letter in the diagonal2 then...           
                return True
        
        #if all of these fail
        return False
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X' #starting letter
    #iterate while the game still has empty squres
    #we don't have to worry about winner because we'll just
    #return that, which breaks the loop
    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        #let's define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #print an empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!')
                    return letter
        #after we made our move, we need to alternate letters
        letter = 'O' if letter =='X' else 'X'
        
        #tiny break
        time.sleep(1)
        
    if print_game:
        print('it\'s a tie!' )
             
        #BUT WAIT WHAT IF WE WON?

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
            
            
            
            