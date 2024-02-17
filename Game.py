from Board import *
from Minmax import *
import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = np.zeros((3,3)).astype(int)
        self.active = True
        self.winner = None
  
    def map_to_xo(self,val):
        if val == 0:
            return 0
        elif val == 1:
            return 1
        elif val == -1:
            return -1
    
    def CheckVictory(self, check):
        for row in self.board:  # markers: 1 -> X, -1 -> O
            if (sum(row)) == 3:
                self.winner = 1
                
            elif sum(row) == -3:
                self.winner = -1

        if self.winner != 1 and self.winner != -1:
            for i in range(0,3):
                if (sum(self.board[:,i])) == 3:
                    self.winner = 1
                    
                elif (sum(self.board[:,i])) == -3:
                    self.winner = -1
        
        if self.winner != 1 and self.winner != -1:
            if (sum(self.board.diagonal())) == 3:
                self.winner = 1
            elif(sum(self.board.diagonal())) == -3:
                self.winner = -1
            elif (sum(np.fliplr(self.board).diagonal())) == 3:
                self.winner = 1
            elif (sum(np.fliplr(self.board).diagonal())) == -3:
                self.winner = -1

        if not np.any(self.board == 0):
            self.active = False
        
        if self.winner == 1 or self.winner == -1:
            if check == True:
                self.active = False
        else:
            self.winner = 0
        
    def place(self, marker, row, col): # place la valeur du joueur dans la matrice
        self.board[row, col] = marker
        self.CheckVictory(True)

    def empty(self, row, col): # annule un mouvement
        self.board[row,col] = 0

    def checkDoubles(self, currentPlayer): # check pour IA s'il y a possibilitÃ© de gagner 
        numOfDoubles = 0
        if currentPlayer == 1:
            for row in self.board:
                if (sum(row)) == 2:
                    numOfDoubles += 1

        for i in range(0, 3):
            if (sum(self.board[:, i])) == 2:
                numOfDoubles += 1

        if (sum(self.board.diagonal())) == 2:
            numOfDoubles += 1

        if (sum(np.fliplr(self.board).diagonal())) == 2:
            numOfDoubles += 1

        elif currentPlayer == -1:
            for row in self.board:
                if (sum(row)) == -2:
                    numOfDoubles += 1

        for i in range(0, 3):
            if (sum(self.board[:, i])) == -2:
                numOfDoubles += 1

        if (sum(self.board.diagonal())) == -2:
            numOfDoubles += 1

        if (sum(np.fliplr(self.board).diagonal())) == -2:
            numOfDoubles += 1
        return numOfDoubles



class Ultimate:

# boards and squares are interpreted with the following NUMPAD system:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |


    def __init__(self, mark):
        self.mainboard = Board()
        self.player = Player(mark)
        self.board = [[TicTacToe(),TicTacToe(),TicTacToe()],[TicTacToe(),TicTacToe(),TicTacToe()],[TicTacToe(),TicTacToe(),TicTacToe()]]
        self.active = True
        self.winner = None
        self.last_move = None
        self.minmaxAgent = minmax(5)
        self.minmaxAgent2 = None
        

        self.g1 = [[0 for x in range(3)] for y in range(3)]
        self.g2 = [[0 for x in range(3)] for y in range(3)]
        self.g3 = [[0 for x in range(3)] for y in range(3)]
        self.g4 = [[0 for x in range(3)] for y in range(3)]
        self.g5 = [[0 for x in range(3)] for y in range(3)]
        self.g6 = [[0 for x in range(3)] for y in range(3)]
        self.g7 = [[0 for x in range(3)] for y in range(3)]
        self.g8 = [[0 for x in range(3)] for y in range(3)]
        self.g9 = [[0 for x in range(3)] for y in range(3)]


        self.squares = [[self.g1,self.g2,self.g3],[self.g4,self.g5,self.g6],[self.g7,self.g8,self.g9]]

    def mark_sqr(self, outer_row, outer_col, inner_row, inner_col, marker):
        if self.squares[outer_row][outer_col][inner_row][inner_col] == 0 and self.isValid(outer_row, outer_col, inner_row, inner_col):
            self.squares[outer_row][outer_col][inner_row][inner_col] = marker
            self.board[outer_row][outer_col].place(marker,inner_row,inner_col)
        else:
            print("Your move is not valid.")
        


    def checkVictory(self, marker):  # checks if the game has ended
        # Check Rows
        if (marker == self.board[0][0].winner == self.board[0][1].winner == self.board[0][2].winner):
            self.active = False
            self.winner = marker
            return True
        elif (marker == self.board[1][0].winner == self.board[1][1].winner == self.board[1][2].winner):
            self.active = False
            self.winner = marker
            return True
        elif (marker == self.board[2][0].winner == self.board[2][1].winner == self.board[2][2].winner):
            self.active = False
            self.winner = marker
            return True

        # Check Columns
        elif (marker == self.board[0][0].winner == self.board[1][0].winner == self.board[2][0].winner):
            self.active = False
            self.winner = marker
            return True
        elif (marker == self.board[0][1].winner == self.board[1][1].winner == self.board[2][1].winner):
            self.active = False
            self.winner = marker
            return True
        elif (marker == self.board[0][2].winner == self.board[1][2].winner == self.board[2][2].winner):
            self.active = False
            self.winner = marker
            return True

        # Check Diagonals
        elif (marker == self.board[0][0].winner == self.board[1][1].winner == self.board[2][2].winner):
            self.active = False
            self.winner = marker
            print("win")
            return True
        elif (marker == self.board[0][2].winner == self.board[1][1].winner == self.board[2][0].winner):
            self.active = False
            self.winner = marker
            print("win")
            return True
        
        return False

   
    def conversion(self, outer_row, outer_col, inner_row, inner_col):
        outer_res = outer_row * 3 + outer_col + 1
        inner_res = inner_row * 3 + inner_col + 1
        pos = str(outer_res) + str(inner_res)
        int_pos = int(pos)
        return int_pos
    
    def deconvert(self, res):
        row = (res - 1) // 3
        col = (res - 1) % 3
        
        return row, col

    def getPossibleActions(self):  # self-explanatory, returns an array of possible tiles to play
        if self.last_move is None:
            return [x for x in range(11,100)]
        
        elif self.board[self.last_move[2]][self.last_move[3]].active:
            last_outer_row ,last_outer_col , last_inner_row, last_inner_col = self.last_move
            possible_actions = []
            if self.active:
                for i in range(3):
                    for j in range(3):
                        if self.squares[last_inner_row][last_inner_col][i][j] == 0:
                            possible_actions.append(self.conversion(last_inner_row, last_inner_col, i, j))
        
            return possible_actions
       
        else:
            possible_actions = []
            if self.active:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j].active:
                            for row in range(3):
                                for col in range(3):
                                    if self.squares[i][j][row][col] == 0:
                                        possible_actions.append(self.conversion(i, j, row, col))
            

            return possible_actions
        


    def emptyTile(self, move):  # called to remove a marker from a tile during minmax lookahead iterations
        pos = int(move % 10)  # e.g. 9
        game = int((move - pos) / 10)  # e.g. 3
        row, col = self.deconvert(game - 1)
        row_ttt, col_ttt = self.deconvert(pos)
        self.board[row][col].empty(row_ttt, col_ttt)
        self.board[row][col].active = True


    def isValid(self, outer_row, outer_col, inner_row, inner_col):
        
        if self.active:
            if self.squares[outer_row][outer_col][inner_row][inner_col] == 0:
                if self.last_move is not None:
                    last_outer_row, last_outer_col, last_inner_row, last_inner_col = self.last_move

                    if self.board[last_inner_row][last_inner_col].active:
                        if (outer_row, outer_col) == (last_inner_row, last_inner_col):
                            return True
                        return False
                    elif self.board[outer_row][outer_col].active:
                        return True
                    else:
                        return False
                    
                else:
                    return True

        return False


    def play(self, outer_row, outer_col, inner_row, inner_col):            
        symb = ""
        if self.player.marker == 1:
            symb = "O"
        else:
            symb = "X"

        print("Your turn " + symb + " !")

        self.mark_sqr(outer_row, outer_col, inner_row, inner_col, self.player.marker)
        pos = [outer_row, outer_col, inner_row, inner_col]
        game = [outer_row, outer_col]
        self.last_move = [outer_row, outer_col, inner_row, inner_col]
        
        if self.checkVictory(self.player):
            print("Player {} has won the game!".format(self.player.marker))
            self.active = False

        self.player.next_turn() 

       
    def heuristics(self, currentPlayer):
        center_spots = [51, 52, 53, 54, 55, 56, 57, 58, 59, 15, 25, 35, 45, 65, 75, 85, 95]  # high value tile locations
        corner_boards = [0, 2, 6, 8]  # small tic tac toe boards
        score = 0
        positions = self.allTilesbyPlayer(currentPlayer)
        # print("Currently looking at player " + str(currentPlayer) + " with positions " + str(positions))
        for int in range(1,10):  # to iterate through the boards
            row, col = self.deconvert(int-1)
            #self.board[row][col].CheckVictory(False)
            if self.board[row][col].winner == currentPlayer:
                score += 10  # points for winning a small board
                if int-1 in corner_boards:  # if the small game is a corner game, extra points
                    score += 4
                elif int-1 == 4:  # if small game is the center game, even more points
                    score += 11
            numberOfDoubles = self.board[row][col].checkDoubles(currentPlayer)  # points for having two out of three tiles for a small board win
            score += numberOfDoubles*2
        for play in positions:
            if play in center_spots:  # just if the spot itself is valuable
                score += 3
                if play == 55:
                    score += 3

        return score
    
    def allTilesbyPlayer(self, player):
        temp = [game for game in self.board]
        ans = []
        for temp2 in temp:
            for i, game in enumerate(temp2):
                temp2 = game.board.flatten()
                temp2 = np.argwhere(temp == player).flatten() + ((i+1)* 10) + 1
                ans.extend(temp)
        return ans   
    
