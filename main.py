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
    print('3 - Random Arcade')
    print('4 - Random Endless')
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
        print("5 - Quitter")

        difficulty = int(input("Votre choix : "))

        size = 0
        if difficulty == 5:
            stop = True
        size = 8*difficulty


        max_game_count = 0
        game_count = 0
        if mode == 1 or mode == 3:
            max_game_count = 5
        else:
            max_game_count = inf

        score = 0

        game = Game()

        while not restart and not stop:
            state = game.play_game(size, mode, 1, score, game_count, max_game_count)
            stop = state[0]
            restart = state[1]

os.system('cls' if os.name == 'nt' else 'clear')
