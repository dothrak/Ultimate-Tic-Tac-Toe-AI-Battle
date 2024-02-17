import sys 
import pygame
import numpy as np



rows = 9
cols = 9
sqsize = 900 // cols
line_c = (23,145,135)
line_w = 8
bg_c = (28,170,156)

width = 900
height = 900

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('TIC TAC TOE - IA BATTLE')
screen.fill(bg_c)

class Player:
    def __init__(self, mark = 1):
        self.marker = mark

    def configureMarker(self, val):
        self.marker = val
    
    def next_turn(self):
        self.marker = self.marker * (-1)



class Board: 

    def __init__(self):
        self.squares = np.array([
            np.array([' ', ' ', ' ']),
            np.array([' ', ' ', ' ']),
            np.array([' ', ' ', ' ']),
        ])
        self.show_lines()
        self.player = Player()

    def show_lines(self): # affichage des lignes
        #vertical
            for i in range(1, cols):
                x = i * sqsize
                line_w = 8 if i != 3 and i != 6 else 12 # donner une épaisseur de 8 aux lignes à l'intérieur des carrés sinon 12 pour délimiter
                pygame.draw.line(screen, line_c, (x, 0), (x, height), line_w)

            #horizontal
            for j in range(1, rows):
                y = j * sqsize
                line_w = 8 if j != 3 and j != 6 else 12 # idem 
                pygame.draw.line(screen, line_c, (0, y), (width, y), line_w)


    def draw_fig(self, inner_row, inner_col, outer_row, outer_col, marker ):
            
            if marker == 1:
                cross_c = (66,66,66)
                cross_w = 12
                # ligne descendante
                init_1 = (outer_col * 3 * sqsize + inner_col * sqsize + 27, outer_row * 3 * sqsize + inner_row * sqsize + 27)
                end_1 = (outer_col * 3 * sqsize + inner_col * sqsize + sqsize - 27, outer_row * 3 * sqsize + inner_row * sqsize + sqsize - 27)

                # ligne ascendante
                init_2 = (outer_col * 3 * sqsize + inner_col * sqsize + 27, outer_row * 3 * sqsize + inner_row * sqsize + sqsize - 27)
                end_2 = (outer_col * 3 * sqsize + inner_col * sqsize + sqsize - 27, outer_row * 3 * sqsize + inner_row * sqsize + 27)

                pygame.draw.line(screen, cross_c, init_1, end_1, cross_w)
                pygame.draw.line(screen, cross_c, init_2, end_2, cross_w)


            elif marker == -1: # cercle
                center = (outer_col * 3 * sqsize + inner_col * sqsize + sqsize // 2, outer_row * 3 * sqsize + inner_row * sqsize + sqsize // 2)
                circle_c = (239,231,200)
                circle_w = 8
                rad = sqsize // 4

                pygame.draw.circle(screen, circle_c, center, rad, circle_w)
