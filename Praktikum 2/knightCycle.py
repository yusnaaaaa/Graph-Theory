import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class CurrentTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


N = 8

moves_x = [1, 1, 2, 2, -1, -1, -2, -2]
moves_y = [2, -2, 1, -1, 2, -2, 1, -1]


def isLegal(x, y):
    return ((x >= 0 and y >= 0) and (x < N and y < N))


def isempty(tour, x, y):
    return (isLegal(x, y)) and (tour[y * N + x] < 0)


def getDegree(tour, x, y):
    count = 0
    for i in range(N):
        if isempty(tour, (x + moves_x[i]), (y + moves_y[i])):
            count += 1
    return count


def nextMove(tour, CurrentTile):
    min_degree_index = -1
    degree = 0
    min_degree = (N + 1)
    next_moves_x = 0
    next_moves_y = 0

    start = random.randint(0, 1000) % N
    for count in range(0, N):
        i = (start + count) % N
        next_moves_x = CurrentTile.x + moves_x[i]
        next_moves_y = CurrentTile.y + moves_y[i]
        degree = getDegree(tour, next_moves_x, next_moves_y)
        if ((isempty(tour, next_moves_x, next_moves_y)) and degree < min_degree):
            min_degree_index = i
            min_degree = degree

    if (min_degree_index == -1):
        return None

    next_moves_x = CurrentTile.x + moves_x[min_degree_index]
    next_moves_y = CurrentTile.y + moves_y[min_degree_index]

    tour[next_moves_y * N +
         next_moves_x] = tour[(CurrentTile.y) * N + (CurrentTile.x)] + 1

    CurrentTile.x = next_moves_x
    CurrentTile.y = next_moves_y

    return CurrentTile


def print_tour(tour):
    for i in range(N):
        for j in range(N):
            print("%d\t" % tour[j * N + i], end="")
        print()


def neighbour(x, y, start_x, start_y):
    for i in range(N):
        if ((x + moves_x[i]) == start_x) and ((y + moves_y[i]) == start_y):
            return True
    return False


def findClosedTour(start_x, start_y):
    tour = [-1] * N * N
    current_tile = CurrentTile(start_x, start_y)
    tour[current_tile.y * N + current_tile.x] = 1

    next_tile = None
    for i in range(N * N - 1):
        next_tile = nextMove(tour, current_tile)
        if next_tile is None:
            return False

    if not neighbour(next_tile.x, next_tile.y, start_x, start_y):
        return False

    tour[start_y * N +
         start_x] = tour[(current_tile.y) * N + (current_tile.x)] + 1
    print_tour(tour)
    return True


# Driver Code
start_x = 1
start_y = 1

while not findClosedTour(start_x, start_y):
    continue
