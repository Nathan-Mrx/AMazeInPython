from Maze import *

class Game:
    def __init__(self, width:int, height:int, algo:int):
        self.width = width
        self.height = height
        if algo == 1:
            self.maze = Maze.gen_btree(width, height)
        elif algo == 2:
            self.maze = Maze.gen_sidewinder(width, height)
        elif algo == 3:
            self.maze = Maze.gen_fusion(width, height)
        elif algo == 4:
            self.maze = Maze.gen_exploration(width, height)
        # elif algo == 5:
        #     self.maze = Maze.gen_wilson(width, height)
        else:
            raise ValueError("Algorithme invalide")
        self.algo = algo
        self.start = (0, 0)
        self.end = (width - 1, height - 1)
        self.player_position = (0, 0)



    def move_player(self, direction):
        """
        Déplaces le joueur dans la direction donnée

        :param direction: La direction dans laquelle le joueur doit se déplacer
        :return: True si le joueur se trouve sur la case d'arrivée, False sinon
        """
        if direction == 'q' and self.maze.is_in_maze( (self.player_position[0], self.player_position[1] - 1) ) and \
                (self.player_position[0], self.player_position[1] - 1) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0], self.player_position[1] - 1)

        elif direction == 'd' and self.maze.is_in_maze( (self.player_position[0], self.player_position[1] + 1) ) and \
                (self.player_position[0], self.player_position[1] + 1) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0], self.player_position[1] + 1)

        elif direction == 's' and self.maze.is_in_maze( (self.player_position[0] + 1, self.player_position[1]) ) and \
                (self.player_position[0] + 1, self.player_position[1]) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0] + 1, self.player_position[1])

        elif direction == 'z' and self.maze.is_in_maze( (self.player_position[0] - 1, self.player_position[1]) ) and \
                (self.player_position[0] - 1, self.player_position[1]) in self.maze.neighbors[self.player_position]:
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        return self.player_position == self.end
