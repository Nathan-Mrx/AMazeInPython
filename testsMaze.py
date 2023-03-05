from Maze import *


laby = Maze(5, 5, empty = True)
print(laby)
print(laby.get_walls())
laby.add_wall((0,0), (0,1))
laby.add_wall((0,1), (0,2))
print(laby.get_walls())

#laby.fill()
#print(laby)
