#!/usr/bin/env python

import Globals
import Utils

# draw_wall = draw_food = draw_player = draw_empty = None

LAYER_MAP = {
             'P':4, 'G':4, '.':4, '-':4,
             'S':3,
             'V':2,
             ' ':1,
            }

COLOR_MAP = {
             '%': color(12, 53, 71),
             '-': color(255, 0, 0),
             '.': color(0, 255, 0),
             'P': color(66, 8, 99),
             'V': color(64, 206, 227),
             ' ': Globals.BACKGROUND_COLOR,
             'G': color(255, 0, 255),
             'S': color(255,254,106),
             # 'A': color(155, 205, 0),
             }


C0LOR_MAP = {
             '%': color(199, 0, 36),
             '%': color(5, 10, 35),
             '-': color(255, 59, 59),
             '-': color(251, 30, 15),
             '.': color(74, 22, 8),
             '.': color(0, 85, 205),
             'P': color(66, 8, 99),
             'V': color(216, 24, 84),
             'V': color(216, 24, 124),
             'V': color(255, 60, 108),
             # 'V': color(204, 153, 139),
             ' ': Globals.BACKGROUND_COLOR,
             'G': color(255, 0, 255),
             'S': color(255, 180, 115),
             # 'S': color(5, 90, 130),
             # 'A': color(155, 205, 0),
             }

def draw_grid(width, height, cell_length, stroke_weight=0.5):
    p1 = p2 = cell_length

    stroke(Globals.GRID_COLOR)
    strokeWeight(stroke_weight)
    while (p1 <= width):
        line(p1, 0, p1, height)
        p1 += cell_length

    while (p2 <= height):
        line(0, p2, width, p2)
        p2 += cell_length

def draw_wall(p, w, h, c):
    # (p.x, p.y)........(p.x+w, p.y)
    #     .       Space       .
    #     .        To         .
    #     .     Draw  In      .
    # (p.x, p.y+h)......(p.x+w, p.y+h)
    # c ---> color
    # sc ---> tuple(bool, color) -> stroke(sc[0])/noStroke()

    noStroke()
    fill(c)
    rect(p.x, p.y, w, h)

def draw_food(p, w, h, c):
    noStroke()
    fill(c)
    ellipse(p.x + 0.5 * Globals.CELL_WIDTH, p.y + 0.5 * Globals.CELL_WIDTH, w-5, h-5)

def draw_player(p, w, h, c):
    noStroke()
    fill(c)
    l = h / 2.0
    triangle(p.x, p.y, p.x, p.y + h, p.x + w, p.y + l)

def draw_empty(p, w, h, c):
    stroke(Globals.GRID_COLOR)
    strokeWeight(0.5)
    fill(c)
    rect(p.x, p.y, w, h)
    # noStroke()


DRAW_MAP = {'%': draw_wall,
            'V': draw_wall,
            'S': draw_wall,
            '.': draw_food,
            'G': draw_food,
            '-': draw_food,
            'P': draw_player,
            ' ': draw_empty,
            # 'A': draw_wall,
            }

def draw_maze(maze, draw_map=DRAW_MAP, color_map=COLOR_MAP, default_color=color(0, 0, 0)):
    # noStroke()
    background(Globals.BACKGROUND_COLOR)
    n = len(maze)
    m = len(maze[0])
    
    for i in range(n):
        for j in range(m):
            p, w, h = Utils.get_cell(i, j)
            
            if (Globals.VISITED[i][j] in 'SV'):
                draw_map[Globals.VISITED[i][j]](p, w, h, color_map[Globals.VISITED[i][j]])
                if LAYER_MAP[Globals.VISITED[i][j]] < LAYER_MAP[maze[i][j]]:
                    draw_map[maze[i][j]](p, w, h, color_map[maze[i][j]])
            else:
                draw_map[maze[i][j]](p, w, h, color_map[maze[i][j]])
            # draw_map[maze[i][j]](p, w, h, color_map.get(maze[i][j], default_color))

def draw_path(start, target, graph, spanning_tree, speed, draw_map=DRAW_MAP, color_map=COLOR_MAP):
    
    node = target
    while node != start:
        for _ in range(speed):
            if (node == start):
                Globals.STOP = True
                yield
                break

            i, j = node
            p, w, h = Utils.get_cell(i, j)
            
            Globals.VISITED[i][j] = 'S'
            # draw_map['S'](p, w, h, color_map['S'])
            # if LAYER_MAP['S'] < LAYER_MAP[graph[i][j]]:
            #     draw_map[graph[i][j]](p, w, h, color_map[graph[i][j]])

            node = spanning_tree[node]
            
        yield
    
    Globals.STOP = True
    yield
