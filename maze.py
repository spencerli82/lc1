#!/usr/bin/env python
# -*- coding: utf-8 -*-
def walk(maze, x, y):
    passed = False
    if (x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 1):
        maze[x][y] = 2
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            passed = True
        else:
            passed = walk(maze, x, y + 1)
            if not passed:
                passed = walk(maze, x + 1, y)
            if not passed:
                passed = walk(maze, x, y - 1)
            if not passed:
                passed = walk(maze, x - 1, y)
        if passed:
            maze[x][y] = 3
    return passed



maze =[[1,1,1,1,1,1,1,1],
       [1,0,0,1,0,0,1,0],
       [1,0,0,0,1,1,1,0],
       [0,1,1,0,1,0,0,1],
       [0,0,1,0,1,1,1,1],
       [1,0,1,1,1,0,1,0],
       [1,1,1,0,0,0,0,1],
       [0,0,1,1,1,1,1,1]]
print walk(maze, 0, 0)