import keyboard

from Game import *
from keyboard import *
import os, time

stop = False

while not stop:
    print(  "   _     __  __   _    _______   _                  _   _",
            "  /_\   |  \/  | /_\  |_  / __| (_)_ _    _ __ _  _| |_| |_  ___ _ _",
            " / _ \  | |\/| |/ _ \  / /| _|  | | ' \  | '_ \ || |  _| ' \/ _ \ ' \ ",
            "/_/ \_\ |_|  |_/_/ \_\/___|___| |_|_||_| | .__/\_, |\__|_||_\___/_||_|",
            "                                         |_|   |__/", sep='\n')

    print("Veuillez choisir votre algorithme de génération de labyrinthe :",
          "1 - Arbre binaire",
          "2 - Sidewinder",
          "3 - Fusion de chemins",
          "4 - Exploration",
          "5 - Wilson", sep='\n')

    algo = int(input("Votre choix : ")[-1])
    if algo < 1 or algo > 5:
        raise ValueError("Choix invalide")

    print("Veuillez choisir votre taille de labyrinthe :",
          "1 - 5x5",
          "2 - 10x10",
          "3 - 15x15",
          "4 - 20x20", sep='\n')

    choice = int(input("Votre choix : "))
    if choice == 1:
        size = 5
    elif choice == 2:
        size = 10
    elif choice == 3:
        size = 15
    elif choice == 4:
        size = 20
    else:
        raise ValueError("Choix invalide")

    game = Game(size, size, algo)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(game.maze.overlay({game.player_position: 'P', game.end: 'A'}))

    won = False
    while not won and not stop:
        print('Appuyez sur les touches Z, Q, S, D pour vous déplacer')
        print('Appuyez sur la touche X pour quitter')

        direction = read_key()

        if direction == 'x':
            stop = True

        won = game.move_player(direction)

        os.system('cls' if os.name == 'nt' else 'clear')

        display_cells = {game.player_position: 'P', game.end: 'A'}

        print(game.maze.overlay(display_cells))


        while is_pressed('z') or is_pressed('q') or is_pressed('s') or is_pressed('d'):
            time.sleep(0.06)

    if won:
        print("Vous avez gagné !")
        time.sleep(1)
        print("Retour au menu dans 5 secondes...")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')

