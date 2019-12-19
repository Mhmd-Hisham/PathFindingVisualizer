#!/usr/bin/env python

import Globals
import Utils
import Draw
import Queue
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    @property
    def size(self):
        return len(self.elements)
    
    def empty(self):
        return self.size == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def dfs(start, maze, directions, speed, draw_map=Draw.DRAW_MAP, color_map=Draw.COLOR_MAP):
    s = [start]
    
    graph = list(list(r) for r in maze) # copy the graph
    visited = [[0] * len(graph[i]) for i in range(len(graph))]
    valid_index = lambda i, j: (0 <= i < len(graph)) and (0 <= j < len(graph[0]))
    
    spanning_tree = {}
    target = None
    while len(s) != 0:
        for _ in range(speed):
            i, j = s.pop(-1)
            p, w, h = Utils.get_cell(i, j)

            if (graph[i][j] == 'G'):
                print("GOT IT :)")
                target = (i, j)
                Globals.GEN = Draw.draw_path(start, target, graph, spanning_tree, speed)
                break
            
            Globals.VISITED[i][j] = 'V'
            # draw_map['V'](p, w, h, color_map['V'])
            # if Draw.LAYER_MAP['V'] < Draw.LAYER_MAP[graph[i][j]]:
            #     draw_map[graph[i][j]](p, w, h, color_map[graph[i][j]])

            for x, y in directions:
                if (valid_index(i + x, j + y) and graph[i + x][j + y] != '%' and (not visited[i + x][j + y])):
                    spanning_tree[(i+x, j+y)] = (i, j)
                    visited[i][j] = True
                    s.append((i + x, j + y))
        yield
            
def bfs(start, maze, directions, speed, draw_map=Draw.DRAW_MAP, color_map=Draw.COLOR_MAP):
    q = Queue.Queue()
    q.put(start)
    
    graph = list(list(r) for r in maze) # copy the graph
    visited = [[0] * len(graph[i]) for i in range(len(graph))]
    valid_index = lambda i, j: (0 <= i < len(graph)) and (0 <= j < len(graph[0]))
    
    spanning_tree = {}
    target = None

    while q.empty() != True:
        for _ in range(speed):
            i, j = q.get()
            p, w, h = Utils.get_cell(i, j)

            # if ((i == target[0]) and (j == target[1])):
            if (graph[i][j] == 'G'):
                print("GOT IT :)")
                target = (i, j)
                Globals.GEN = Draw.draw_path(start, target, graph, spanning_tree, speed)
                break

            Globals.VISITED[i][j] = 'V'
            # draw_map['V'](p, w, h, color_map['V'])
            # if Draw.LAYER_MAP['V'] < Draw.LAYER_MAP[graph[i][j]]:
            #     draw_map[graph[i][j]](p, w, h, color_map[graph[i][j]])

            for x, y in directions:
                if (valid_index(i + x, j + y) and graph[i + x][j + y] != '%' and (not visited[i + x][j + y])):
                    spanning_tree[(i+x,j+y)] = (i, j)
                    q.put((i + x, j + y))
                    visited[i + x][j + y] = True
        yield

def Dijkstra(start, maze, directions, speed, draw_map=Draw.DRAW_MAP, color_map=Draw.COLOR_MAP):
    q = PriorityQueue()
    q.put(start, 0)
    
    # graph = list(list(r) for r in maze) # copy the graph
    graph = maze
    visited = [[0] * len(graph[i]) for i in range(len(graph))]
    weights = Utils.extract_weights_from_maze(graph)
    
    valid_index = lambda i, j: (0 <= i < len(graph)) and (0 <= j < len(graph[0]))
    
    spanning_tree = {start:None}
    cost_so_far = {start:0}
    visited[start[0]][start[1]] = True

    target = None
    while q.empty() != True:
        for _ in range(speed):
            i, j = q.get()
            current = (i, j)
            p, w, h = Utils.get_cell(i, j)

            if (graph[i][j] == 'G'):
                target = current
                Globals.GEN = Draw.draw_path(start, target, graph, spanning_tree, speed)
                break

            Globals.VISITED[i][j] = 'V'
            # draw_map['V'](p, w, h, color_map['V'])
            # if Draw.LAYER_MAP['V'] < Draw.LAYER_MAP[graph[i][j]]:
            #     draw_map[graph[i][j]](p, w, h, color_map[graph[i][j]])
    
            for x, y in directions:
                next = (i+x, j+y)
                if (graph[next[0]][next[1]] == '%') or (visited[next[0]][next[1]]):
                    continue
                
                new_cost = cost_so_far[current] + weights[next[0]][next[1]]
                if ((next not in cost_so_far) or new_cost <= cost_so_far[next]):
                    cost_so_far[next] = new_cost
                    visited[next[0]][next[1]] = True
                    q.put(next, new_cost)
                    # print("Cost: %s"%new_cost)
                    
                    spanning_tree[next] = current
        yield

#       (0,-1)
# (-1,0)(0,0)(1, 0)
#       (0,1)

DIRECTIONS = [
    (0, -1),  # UP
    (0, 1),  # DOWN
    (-1, 0),  # LEFT
    (1, 0),  # RIGHT
]

ALGORITHMS_MAP = {"Breadth-First Search(BFS)": bfs,
                  "Depth-First Search(DFS)": dfs,
                  "Dijkstra": Dijkstra}

TIME_COMPLEXITY_MAP = {"Depth-First Search(DFS)": "O(V + E)",
                       "Breadth-First Search(BFS)": "O(V)",
                       "Dijkstra": "O((V + E) log V)",
                       }

SPACE_COMPLEXITY_MAP = {"Depth-First Search(DFS)": "O(V + E)",
                        "Breadth-First Search(BFS)": "O(V)",
                        "Dijkstra": "O(V)",
                       }

                    
