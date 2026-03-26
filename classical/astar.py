import numpy as np
import heapq

GRID_SIZE = 15
START = (0, 0)
GOAL = (GRID_SIZE-1, GRID_SIZE-1)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node, grid):
    x, y = node
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if grid[nx, ny] == 0:
                yield (nx, ny)

def a_star(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for n in neighbors(current, grid):
            temp_g = g[current] + 1
            if n not in g or temp_g < g[n]:
                g[n] = temp_g
                f = temp_g + heuristic(n, goal)
                heapq.heappush(open_set, (f, n))
                came_from[n] = current

    path = []
    if goal in came_from:
        node = goal
        while node != start:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()

    return path
