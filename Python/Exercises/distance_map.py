# Complete the function below.
from collections import deque

# Return the two list of neighbors(as tuples of coordinates)
# the close for the close one (cost=1)
# the far for the far one (cost=3)


def compute_neighbors(x, y, grid):
    N, M = grid.shape
    neighbors_close = []
    neighbors_far = []
    if x == 0:
        neighbors_close.append((x+1, y))
        if y == 0:
            neighbors_close.append((x, y+1))
            neighbors_far.append((x+1, y+1))
        else:
            neighbors_close.append((x, y-1))
            neighbors_far.append((x+1, y-1))
            if y == M-1:
                return neighbors_close, neighbors_far
            neighbors_close.append((x, y+1))
            neighbors_far.append((x+1, y+1))
    elif y == 0:
        neighbors_close.append((x, y+1))
        neighbors_close.append((x-1, y))
        neighbors_far.append((x-1, y-1))
        if x == N-1:
            return neighbors_close, neighbors_far
        neighbors_close.append((x+1, y))
        neighbors_far.append((x+1, y+1))
    elif x == N-1:
        neighbors_close.append((x-1, y))
        neighbors_close.append((x, y-1))
        neighbors_far.append((x-1, y-1))
        if y == M-1:
            return neighbors_close, neighbors_far
        neighbors_close.append((x, y+1))
        neighbors_far.append((x-1, y+1))
    else:
        neighbors_close.append((x-1, y))
        neighbors_close.append((x, y-1))
        neighbors_close.append((x+1, y))
        neighbors_far.append((x-1, y-1))
        neighbors_far.append((x+1, y-1))
        if y == M-1:
            return neighbors_close, neighbors_far
        neighbors_close.append((x, y+1))
        neighbors_far.append((x+1, y+1))
        neighbors_far.append((x-1, y+1))

    return neighbors_close, neighbors_far

# Version 1: brute force


def visite_neighbors(neighbors, queue, visited, grid, parent_cost, fee):
    for n in neighbors:
        nx, ny = n
        # Checking n not obstacle or landmark
        if grid[nx, ny] >= 0:
            newcost = parent_cost + fee
            # Need to compare the cost because of the close/far distinction
            if not visited[nx, ny] or newcost < grid[nx, ny]:
                # Visit node n
                visited[nx, ny] = 1
                grid[nx, ny] = newcost
                queue.append(n)
    return queue, grid, visited

# Version 2: Change the source landmark when a new landmark is met and
# start from it


def visite_neighbors_2(neighbors, queue, visited, grid, parent_cost, fee):
    for n in neighbors:
        nx, ny = n
        # Case n is a landmark
        if grid[nx, ny] == -2 and not visited[nx, ny]:
            # Start over from this landmark
            visited[nx, ny] = 1
            new_parent_cost = 0
            # Computing neighbors
            new_neighbors_close, new_neighbors_far = compute_neighbors(
                nx, ny, grid)
            # Visiting close neighbors
            queue, grid, visited = visite_neighbors_2(
                new_neighbors_close, queue, visited, grid, new_parent_cost, 1)
            # Visiting far neighbors
            queue, grid, visited = visite_neighbors_2(
                new_neighbors_close, queue, visited, grid, new_parent_cost, 3)
        elif grid[nx, ny] >= 0:
            newcost = parent_cost + fee
            # Need to compare the cost because of the close/far distinction
            if not visited[nx, ny] or newcost < grid[nx, ny]:
                # Visit node n
                visited[nx, ny] = 1
                grid[nx, ny] = newcost
                queue.append(n)
    return queue, grid, visited

# Inplace computation of the distance map


def compute_distance_map(grid):
    # Pre process the grid
    # Find the landmark
    found = np.where(grid == 2)
    Ls = [(x, y) for x, y in zip(found[0], found[1])]
    # Fill landmark with -2
    grid[found] = -2
    # Fill obstacle with -1
    grid[grid == 1] = -1

    # Compute distance from each landmark
    # Boolean array to check if node visited
    visited = np.zeros_like(grid)
    for land in Ls:
        lx, ly = land
        if not visited[lx, ly]:
            # Queue of pending nodes to visit
            queue = deque([land])
            visited[lx, ly] = 1
            while queue:
                x, y = queue.popleft()
                # Case landmark
                if grid[x, y] < 0:
                    parent_cost = 0
                else:
                    parent_cost = grid[x, y]
                # Computing neighbors
                neighbors_close, neighbors_far = compute_neighbors(x, y, grid)
                # Visiting close neighbors
                queue, grid, visited = visite_neighbors_2(
                    neighbors_close, queue, visited, grid, parent_cost, 1)
                # Visiting far neighbors
                queue, grid, visited = visite_neighbors_2(
                    neighbors_far, queue, visited, grid, parent_cost, 3)

    # Filling the unvisited node with -1 (because not accessible)
    grid[grid == 0] = -1
    # Filling the landmark node with 0 (to format the output)
    grid[grid == -2] = 0

    return grid


def read_grid():
    n = int(sys.stdin.readline())
    return np.array([map(int, sys.stdin.readline().split()) for _ in xrange(n)])


def write_distance_map(d):
    for row in d:
        print " ".join(map(str, row))

grid = read_grid()
distance_map = compute_distance_map(grid)
write_distance_map(distance_map)
