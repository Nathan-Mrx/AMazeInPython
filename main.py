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

    print('Sélectionnez un mode de jeu :')
    print('1 - Arcade')
    print('2 - Endless')
    print('3 - Random position Arcade')
    print('4 - Random position Endless')
    print('5 - Quitter')

    mode = int(input("Votre choix : ")[-1])

    if mode == 5:
        stop = True

    if not stop:
        print("Choisissez une difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")
        print("4 - Expert")
        print("5 - Impossible")
        print("6 - Quitter")

        difficulty = int(input("Votre choix : "))

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

        max_game_count = 0
        random_position = False
        game_count = 0
        if mode == 1:
            max_game_count = 5
            random_position = False

        elif mode == 2:
            max_game_count = inf
            random_position = False

        elif mode == 3:
            max_game_count = 5
            random_position = True

        elif mode == 4:
            max_game_count = inf
            random_position = True

        score = 0

        game = Game()
        while not stop:
            stop = game.play_game(size, mode, 1, score, game_count, max_game_count, random_position)

os.system('cls' if os.name == 'nt' else 'clear')
