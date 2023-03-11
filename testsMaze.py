from Maze import *

laby = Maze.gen_fusion(4, 4)
solution = laby.solve_rhr((0, 0), (3, 3))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(3, 3)] = 'A'
print(laby.overlay(str_solution))