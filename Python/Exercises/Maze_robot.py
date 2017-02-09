import numpy as np


def get_path(maze):
    if maze.any():
        path = []
        if _get_path(maze, 0, 0, path):
            return path
    return None


def _get_path(maze, i, j, path):
    if (i >= maze.shape[0] or j >= maze.shape[1] or not maze[i, j]):
        return False
    end = ((i, j) == (maze.shape[0] - 1, maze.shape[1] - 1))
    print ' current cell is {}, {}'.format(i, j)
    print end
    if end or _get_path(maze, i + 1, j, path) or _get_path(maze, i, j + 1, path):
        path.append((i, j))
        return True

    return False


def print_path(maze, path):
    maze = maze.copy()
    for coord in path:
        maze[coord[0], coord[1]] = 5
    return maze
