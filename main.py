import os
import time

from keyboard import *

from Game import *

stop = False

os.system('cls' if os.name == 'nt' else 'clear')

while not stop:
    restart = False
    print("   _     __  __   _    _______   _                  _   _",
          "  /_\   |  \/  | /_\  |_  / __| (_)_ _    _ __ _  _| |_| |_  ___ _ _",
          " / _ \  | |\/| |/ _ \  / /| _|  | | ' \  | '_ \ || |  _| ' \/ _ \ ' \ ",
          "/_/ \_\ |_|  |_/_/ \_\/___|___| |_|_||_| | .__/\_, |\__|_||_\___/_||_|",
          "                                         |_|   |__/", sep='\n')

    print("Choisissez une difficulté :")
    print("1 - Facile")
    print("2 - Moyen")
    print("3 - Difficile")
    print("4 - Expert")
    print("5 - Impossible")
    print("6 - Quitter")

    difficulty = int(input("Votre choix : ")[-1])

    size = 0
    if difficulty == 6:
        stop = True
    elif difficulty == 1:
        size = 5
    elif difficulty == 2:
        size = 10
    elif difficulty == 3:
        size = 15
    elif difficulty == 4:
        size = 20
    elif difficulty == 5:
        size = 25
    else:
        raise ValueError("Difficulté invalide")

    os.system('cls' if os.name == 'nt' else 'clear')

    game_count = 0
    score = 0
    while game_count < 5 and not stop:

        print("   _     __  __   _    _______   _                  _   _",
              "  /_\   |  \/  | /_\  |_  / __| (_)_ _    _ __ _  _| |_| |_  ___ _ _",
              " / _ \  | |\/| |/ _ \  / /| _|  | | ' \  | '_ \ || |  _| ' \/ _ \ ' \ ",
              "/_/ \_\ |_|  |_/_/ \_\/___|___| |_|_||_| | .__/\_, |\__|_||_\___/_||_|",
              "                                         |_|   |__/", sep='\n')

        if game_count == 0:
            algo = 1
            msg = 'de génération par arbre binaire'
        elif game_count == 1:
            algo = 2
            msg = 'sidewinder'
        elif game_count == 2:
            algo = 3
            msg = 'de fusion de chemins'
        elif game_count == 3:
            algo = 4
            msg = 'd\'exploration exhausitve'
        elif game_count == 4:
            algo = 4
            # TODO: algo = 5 # A décommenter pour tester l'algorithme de Wilson
            msg = 'de Wilson'
        else:
            raise ValueError("Algorithme invalide")

        print("Partie n°" + str(game_count + 1) + " sur 5")
        print("Algorithme " + msg)

        time.sleep(3)

        game = Game(size, size, algo)

        os.system('cls' if os.name == 'nt' else 'clear')

        print(game.maze.overlay({game.player_position: 'P', game.end: 'A'}))
        move_count = 0
        min_distance = game.maze.distance_geo(game.start, game.end)
        won = False
        while not won and not stop:
            print('Appuyez sur les touches Z, Q, S, D pour vous déplacer')
            print('Appuyez sur la touche X pour quitter')
            print('Nombre de déplacements : ' + str(move_count))
            print('Nombre de déplacements minimal: ' + str(min_distance))

            direction = read_key()

            if direction == 'x':
                stop = True

            old_position = game.player_position
            won = game.move_player(direction)

            if game.player_position == old_position:
                move_count -= 1

            os.system('cls' if os.name == 'nt' else 'clear')

            display_cells = {game.player_position: 'P', game.end: 'A'}

            print(game.maze.overlay(display_cells))

            while is_pressed('z') or is_pressed('q') or is_pressed('s') or is_pressed('d'):
                time.sleep(0.06)
            move_count += 1

        score += min_distance * 1000 / move_count

        if won:
            print("Vous avez gagné ! En " + str(move_count) + " déplacements !")
            print('Votre score est de ', round(score), '/', 1000 * (game_count + 1), sep='')
            time.sleep(1)
            if game_count == 4:
                print("Partie terminée !")
                print("Appuyez sur x pour quitter")
                while not restart:
                    if is_pressed('x'):
                        restart = True
            else:
                print("Prochaine partie dans 5 secondes...")
                time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

        game_count += 1

os.system('cls' if os.name == 'nt' else 'clear')
