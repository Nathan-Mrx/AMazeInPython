import os
import time
from math import inf

from keyboard import *

from Maze import *


class Game:
    def __init__(self):
        self.player_position = (0, 0)
        self.end = (0, 0)
        self.maze = Maze(1,1)

    def move_player(self, direction):
        """
        Déplaces le joueur dans la direction donnée

        :param direction: La direction dans laquelle le joueur doit se déplacer
        :return: True si le joueur se trouve sur la case d'arrivée, False sinon
        """
        if direction == 'q' and self.maze.is_in_maze((self.player_position[0], self.player_position[1] - 1)) and \
                (self.player_position[0], self.player_position[1] - 1) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0], self.player_position[1] - 1)

        elif direction == 'd' and self.maze.is_in_maze((self.player_position[0], self.player_position[1] + 1)) and \
                (self.player_position[0], self.player_position[1] + 1) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0], self.player_position[1] + 1)

        elif direction == 's' and self.maze.is_in_maze((self.player_position[0] + 1, self.player_position[1])) and \
                (self.player_position[0] + 1, self.player_position[1]) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0] + 1, self.player_position[1])

        elif direction == 'z' and self.maze.is_in_maze((self.player_position[0] - 1, self.player_position[1])) and \
                (self.player_position[0] - 1, self.player_position[1]) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        return self.player_position == self.end

    def play_game(self, size, mode, algo, score=0, game_count=0, max_game_count=5):
        restart = False
        stop = False
        msg = ''

        os.system('cls' if os.name == 'nt' else 'clear')

        while game_count < max_game_count and not stop and not restart:

            if game_count % 5 == 0:
                algo = 1
            elif game_count % 5 == 1:
                algo = 2
            elif game_count % 5 == 2:
                algo = 3
            elif game_count % 5 == 3:
                algo = 4
            elif game_count % 5 == 4:
                algo = 5

            if algo == 1:
                self.maze = Maze.gen_btree(size, size)
                msg = 'de génération par arbre binaire'
            elif algo == 2:
                self.maze = Maze.gen_sidewinder(size, size)
                msg = 'sidewinder'
            elif algo == 3:
                self.maze = Maze.gen_fusion(size, size)
                msg = 'de fusion de chemins'
            elif algo == 4:
                self.maze = Maze.gen_exploration(size, size)
                msg = 'd\'exploration exhausitve'
            elif algo == 5:
                self.maze = Maze.gen_exploration(size, size)
                msg = 'de Wilson'

            if mode == 1 or mode == 2:
                self.player_position = (0, 0)
                self.end = (size - 1, size - 1)
            elif mode == 3 or mode == 4:
                cells = self.maze.get_cells()
                self.player_position = r.choice(cells)
                cells.remove(self.player_position)
                self.end = r.choice(cells)

            print("   _     __  __   _    _______   _                  _   _",
                  "  /_\   |  \/  | /_\  |_  / __| (_)_ _    _ __ _  _| |_| |_  ___ _ _",
                  " / _ \  | |\/| |/ _ \  / /| _|  | | ' \  | '_ \ || |  _| ' \/ _ \ ' \ ",
                  "/_/ \_\ |_|  |_/_/ \_\/___|___| |_|_||_| | .__/\_, |\__|_||_\___/_||_|",
                  "                                         |_|   |__/", sep='\n')

            if max_game_count != inf:
                print("Partie n°" + str(game_count + 1) + " sur 5")
            else:
                print("Partie n°" + str(game_count + 1))
            print("Algorithme " + msg)

            time.sleep(3)

            os.system('cls' if os.name == 'nt' else 'clear')

            print(self.maze.overlay({self.player_position: 'P', self.end: 'A'}))
            move_count = 0
            min_distance = self.maze.distance_geo(self.player_position, self.end)
            won = False
            while not won and not stop and not restart:
                print('Appuyez sur les touches Z, Q, S, D pour vous déplacer')
                print('Appuyez sur la touche X pour quitter')
                print('Nombre de déplacements : ' + str(move_count))
                print('Nombre de déplacements minimal: ' + str(min_distance))

                direction = read_key()

                if direction == 'x':
                    stop = True


                old_position = self.player_position
                won = self.move_player(direction)

                if self.player_position == old_position:
                    move_count -= 1

                os.system('cls' if os.name == 'nt' else 'clear')

                display_cells = {self.player_position: 'P', self.end: 'A'}

                print(self.maze.overlay(display_cells))

                while is_pressed('z') or is_pressed('q') or is_pressed('s') or is_pressed('d'):
                    time.sleep(0.01)
                move_count += 1

            if won:
                score += min_distance * 1000 / move_count

                print("Vous avez gagné ! En " + str(move_count) + " déplacements !")
                print('Votre score est de ', round(score), '/', 1000 * (game_count + 1), sep='')
                time.sleep(1)
                if game_count == max_game_count - 1:
                    print("Partie terminée !")
                    print("x pour retourner au menu")
                    while not restart:
                        if is_pressed('x'):
                            restart = True
                else:
                    print("Prochaine partie dans 5 secondes...")
                    time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')

                if mode == 3 or mode == 4:
                    size += 1

            os.system('cls' if os.name == 'nt' else 'clear')
            game_count += 1

        os.system('cls' if os.name == 'nt' else 'clear')

        return stop, restart
