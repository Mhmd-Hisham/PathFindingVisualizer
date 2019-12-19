#!/usr/bin/env python3

import Globals
import random

def read_maze_from_file(filename):
    with open(filename, "r") as maze_file:
        maze = maze_file.readlines()

    return [list(r.strip()) for r in maze]

def get_cell(i, j, step=Globals.CELL_WIDTH):
    return PVector(j * step, i * step), step, step

def generate_maze(n, m):
    return [[random.randrange(2) for _ in range(n)] for _ in range(m)]

def find_char_position(maze, character):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == character:
                return i, j

def pprint_maze(maze):
    print("//////////////////////////////////////")
    print(len(maze), len(maze[0]))
    for r in maze:
        print(''.join(r))
    print("//////////////////////////////////////")

def extract_weights_from_maze(maze):
    
    n = len(maze)
    m = len(maze[0])
    weights = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            
            if (maze[i][j] == '.'):
                weights[i][j] = 1
            
            elif (maze[i][j] == ' '):
                weights[i][j] = 3
            
            elif (maze[i][j] == '-'):
                weights[i][j] = 4
            
            else:
                weights[i][j] = 0
    
    return weights
