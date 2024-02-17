from Board import *
from Game import *
from art import *
from Minmax import *

minmaxAgent = minmax(1)

def afficher_menu():
    print("=== Menu ===")
    print("1. Jouer à 2 joueurs")
    print("2. Jouer contre l'IA")
    print("3. Regarder l'IA jouer")
    print("4. Quitter")
    print("============")

def afficher_sous_menu():
    print("=== Options ===")
    print("1. Joueur commence")
    print("2. IA commence")
    print("===============")

def jouer_a_deux_joueurs():
    # Création de la grille de jeu
    board = Board()
    ultimate = Ultimate(1)


    while ultimate.active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                outer_row = pos[1] // (3 * sqsize)
                outer_col = pos[0] // (3 * sqsize)
                inner_row = (pos[1] % (3 * sqsize)) // sqsize
                inner_col = (pos[0] % (3 * sqsize)) // sqsize

                if not ultimate.isValid(outer_row, outer_col, inner_row, inner_col):
                    print("Your move is not valid.")

                else:

                    print(ultimate.squares)

                    board.draw_fig(inner_row, inner_col, outer_row, outer_col, ultimate.player.marker)

                    # Change de tour
                    ultimate.play(outer_row, outer_col, inner_row, inner_col)

        pygame.display.update()

def jouer_contre_ia():
    afficher_sous_menu()
    choix = input("Veuillez choisir qui commence (1-2) : ")

    first = 0

    if choix == "1":
        first = 1
    elif choix == "2":
        first = -1
    else:
        print("Option invalide. Retour au menu principal.")
        return

    # Création de la grille de jeu
    board = Board()
    ultimate = Ultimate(1)


    while ultimate.active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ultimate.player.marker == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    outer_row = pos[1] // (3 * sqsize)
                    outer_col = pos[0] // (3 * sqsize)
                    inner_row = (pos[1] % (3 * sqsize)) // sqsize
                    inner_col = (pos[0] % (3 * sqsize)) // sqsize

                    if not ultimate.isValid(outer_row, outer_col, inner_row, inner_col):
                        print("Your move is not valid.")
                    else:

                        print(ultimate.squares)

                        board.draw_fig(inner_row, inner_col, outer_row, outer_col, ultimate.player.marker)

                        # Change de tour
                        ultimate.play(outer_row, outer_col, inner_row, inner_col)
            else:
                chosenTile = 0
                if ultimate.last_move == None:
                    chosenTile = random.randint(11,99)
                else:
                    chosenTile = minmaxAgent.algorithm(ultimate, ultimate.player.marker*-1, ultimate.getPossibleActions())
                
                if not chosenTile is None:
                    outer_row, outer_col, inner_row, inner_col = deconversion(chosenTile)

                    print(ultimate.squares)

                    board.draw_fig(inner_row, inner_col, outer_row, outer_col, ultimate.player.marker)

                    # Change de tour
                    ultimate.play(outer_row, outer_col, inner_row, inner_col)
                else:
                    print("Plus de coup possible...")

        pygame.display.update()

def regarder_ia_jouer():
    # Création de la grille de jeu
    board = Board()
    ultimate = Ultimate(1)

    while ultimate.active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            chosenTile = 0
            if ultimate.last_move == None:
                chosenTile = random.randint(11,99)
            else:
                chosenTile = minmaxAgent.algorithm(ultimate, ultimate.player.marker*-1, ultimate.getPossibleActions())
            
            ultimate.checkVictory(ultimate.player.marker)

            if not chosenTile is None:
                outer_row, outer_col, inner_row, inner_col = deconversion(chosenTile)

                print(ultimate.squares)

                board.draw_fig(inner_row, inner_col, outer_row, outer_col, ultimate.player.marker)

                # Change de tour
                ultimate.play(outer_row, outer_col, inner_row, inner_col)
            else:
                print("Plus de coup possible...")


        pygame.display.update()

def deconversion(int_pos):
    pos = str(int_pos)
    outer_res = int(pos[0]) - 1
    inner_res = int(pos[1]) - 1

    outer_row = outer_res // 3
    outer_col = outer_res % 3
    inner_row = inner_res // 3
    inner_col = inner_res % 3

    return outer_row, outer_col, inner_row, inner_col

print(text2art("TicTacToe", "rand"))

# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Veuillez choisir une option (1-4) : ")

    if choix == "1":
        jouer_a_deux_joueurs()
    elif choix == "2":
        jouer_contre_ia()
    elif choix == "3":
        regarder_ia_jouer()
    elif choix == "4":
        print("Merci d'avoir joué ! Au revoir.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
