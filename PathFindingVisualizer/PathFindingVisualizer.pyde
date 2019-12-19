#!/usr/bin/env python
"""

TODO:-
   1. Shuffle directions
   2. Maze generators
   3. A*
   

"""
import Globals
import Draw
from Algorithms import ALGORITHMS_MAP, DIRECTIONS, TIME_COMPLEXITY_MAP, SPACE_COMPLEXITY_MAP
import Utils

Globals.MAZE = Utils.read_maze_from_file(Globals.MAZE_FILE)
N, M = len(Globals.MAZE), len(Globals.MAZE[0])
Globals.WIDTH = Globals.CELL_WIDTH * M
Globals.HEIGHT = Globals.CELL_WIDTH * N

def setup():
    size(Globals.WIDTH, Globals.HEIGHT)
    # frameRate(60)
    Globals.VISITED = [list(r) for  r in Globals.MAZE]
    Draw.draw_maze(Globals.MAZE)
    # Draw.draw_grid(Globals.WIDTH, Globals.HEIGHT, Globals.CELL_WIDTH)
    Globals.PLAYER_POSITION = Utils.find_char_position(Globals.MAZE, Globals.PLAYER_CHAR)
    Globals.GEN = ALGORITHMS_MAP[Globals.ALGORITHM](Globals.PLAYER_POSITION, Globals.MAZE, DIRECTIONS, Globals.SPEED)

def draw():
    Draw.draw_maze(Globals.MAZE)
    # Draw.draw_grid(Globals.WIDTH, Globals.HEIGHT, Globals.CELL_WIDTH)
    
    fill(0,0,0, 110)
    rect(17, 20, 360, 80)
    textSize(20)
    fill(255)
    text("Algorithm: {}".format(Globals.ALGORITHM), 20, 40)
    text("Time complexity: {}".format(TIME_COMPLEXITY_MAP[Globals.ALGORITHM]), 20, 65)
    text("Space complexity: {}".format(SPACE_COMPLEXITY_MAP[Globals.ALGORITHM]), 20, 90)
    
    if Globals.STOP or Globals.PAUSE:
        return

    # saveFrame("pics/"+ALGORITHM.upper()+"/"+ALGORITHM.upper()+"-######.png")
    Globals.GEN.next()

def change_algorithm(algorithm):
    Globals.ALGORITHM = algorithm
    Globals.VISITED = [list(r) for  r in Globals.MAZE]
    Globals.GEN = ALGORITHMS_MAP[Globals.ALGORITHM](Globals.PLAYER_POSITION, Globals.MAZE, DIRECTIONS, Globals.SPEED)
    Draw.draw_maze(Globals.MAZE)
    Globals.STOP = False

def keyPressed():
    if (key == " "):
        Globals.PAUSE = not Globals.PAUSE

    elif (key == 'b'):
        change_algorithm("Breadth-First Search(BFS)")
    
    elif (key == 'd'):
        change_algorithm("Depth-First Search(DFS)")
    
    elif (key == 'k'):
        change_algorithm("Dijkstra")
    
    elif (key == '+'):
        Globals.SPEED += 1
        print("Speed: " + str(Globals.SPEED))
    
    elif (key == '-'):
        Globals.SPEED = max(1, Globals.SPEED-1)
        print("Speed: " + str(Globals.SPEED))
    
    elif (key == 's'):
        saveFrame(Globals.ALGORITHM.upper()+"-######.png")
        
