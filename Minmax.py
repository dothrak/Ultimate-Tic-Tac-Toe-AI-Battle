import numpy as np
import math
import random
import copy



class minmax():
    def __init__(self, depth = 3):
        self.depth = depth
        self.blockLocation = None

    def algorithm(self, board, marker, positions):
        mustBlock = False
        bestScore = -99999  # the current best score associated with the current best play
        bestPlay = None  # the best tile that the AI should play given the current board
        global wValue
        wValue = -99999  # the value found from the current move
        for tile in positions:
            deepCopy = copy.deepcopy(board)  # deepcopy of the board to ensure we don't unintentionally tamper with the current state
            pos = int(tile % 10)  # e.g. 9
            game = int((tile - pos) / 10)  # e.g. 3
            deepCopy.last_move = self.deconversion(tile)
            row_game, col_game = self.deconvert(game - 1)
            row_pos, col_pos = self.deconvert(pos)
            deepCopy.board[row_game][col_game].place(marker, row_pos, col_pos)  # puts down a marker at each available position
            if deepCopy.checkVictory(marker):  # if this wins us the game, just put it there instantly
                return tile
            wValue = self.recursive(deepCopy, marker, marker*-1, self.depth, -20000, 20000)  # calculates the heuristic score of playing at that tile
            if wValue >= bestScore:  # is this spot better than our current best score?
                bestPlay = tile
                bestScore = wValue
        return bestPlay

    def recursive(self, board, marker, currentPlayer, depth, a, b):
        alpha = a
        beta = b
        possibleMoves = board.getPossibleActions()
        if depth != 0:
            if currentPlayer == marker: #AI seeks to maximize score on its own turn
                score = -10000  # substitute for INTEGER.MIN_VALUE
                if score != 10000:
                    for i in possibleMoves:
                        pos = int(i % 10)  #try out the move
                        game = int((i - pos) / 10)
                        board.last_move = self.deconversion(i)
                        row_game, col_game = self.deconvert(game - 1)
                        row_pos, col_pos = self.deconvert(pos)
                        board.board[row_game][col_game].place(currentPlayer, row_pos, col_pos)  # puts down a marker at each available position
                        if board.checkVictory(currentPlayer):  # we will win if we continue on this path, maximum value
                            alpha = 10000
                            score = alpha
                            return score
                        score = max(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                        if (score > alpha):
                            alpha = score
                        board.emptyTile(i)
                        if (alpha > beta):
                            break
                return alpha

            else:  #AI seeks to minimize score on opponent's turn
                score = 10000
                if score != -10000:
                    for i in possibleMoves:
                        pos = int(i % 10)  #try out the move
                        game = int((i - pos) / 10)
                        board.last_move = self.deconversion(i)
                        row_game, col_game = self.deconvert(game - 1)
                        row_pos, col_pos = self.deconvert(pos)
                        board.board[row_game][col_game].place(currentPlayer, row_pos, col_pos)  # puts down a marker at each available position
                        if board.checkVictory(currentPlayer):  # the opponent will win if they play here, so block it asap
                            beta = -10000
                            score = beta
                            return score
                        score = min(score, self.recursive(board, marker, currentPlayer*-1, depth-1, alpha, beta))
                        if (score < beta):
                            beta = score
                        board.emptyTile(i)
                        if beta < alpha:
                            break
                return beta
        else:  # depth is zero, time for heuristics
            heuristicScore = board.heuristics(marker) - board.heuristics(marker*-1)
            return heuristicScore
        
    def deconvert(self, res):
        row = (res - 1) // 3
        col = (res - 1) % 3
        
        return row, col
    
    def conversion(self, outer_row, outer_col, inner_row, inner_col):
        outer_res = outer_row * 3 + outer_col + 1
        inner_res = inner_row * 3 + inner_col + 1

        pos = str(outer_res) + str(inner_res)
        int_pos = int(pos)
        
        return int_pos

    def deconversion(self, int_pos):
        pos = str(int_pos)
        outer_res = int(pos[0]) - 1
        inner_res = int(pos[1]) - 1

        outer_row = outer_res // 3
        outer_col = outer_res % 3
        inner_row = inner_res // 3
        inner_col = inner_res % 3

        return outer_row, outer_col, inner_row, inner_col
    
