#!/usr/bin/env python

import os
import random

# GLOBALS
STOP = False
PAUSE = False
SPEED = 20
GEN = None

PLAYER_POSITION = None
MAZE = None
VISITED = None
ALGORITHM = "Dijkstra"

# CONF
WIDTH = HEIGHT = 0
CELL_WIDTH = 16

PLAYER_CHAR = 'P'

MAZE_FILES = os.listdir("data/mazes/")
# MAZE_FILE = os.path.join("data/mazes", MAZE_FILES[3])
# MAZE_FILE = os.path.join("data/mazes", random.choice(MAZE_FILES))
MAZE_FILE = "data/mazes/mediumMaze.txt"
# MAZE_FILE = "data/mazes/customDots.txt"
# print(MAZE_FILE)

BACKGROUND_COLOR = color(255)
GRID_COLOR = color(175, 216, 248)
# GRID_COLOR = color(74, 22, 8)
# GRID_COLOR = color(255, 60, 108)
