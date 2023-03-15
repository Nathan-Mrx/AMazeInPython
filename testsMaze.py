from Maze import *

laby = Maze.gen_wilson(8, 8)
solution = laby.solve_dfs((0, 0), (7, 7))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(7, 7)] = 'A'
print(laby.overlay(str_solution))
print(laby.distance_geo((0, 0), (7, 7)))
print(laby.distance_man((0, 0), (7, 7)))
