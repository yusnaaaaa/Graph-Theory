def print_tour(tour):
    for i in range(N):
        for j in range(N):
            print("(%d, %d, %d)\t" % (tour[j * N + i], i, j), end="")
        print()


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


start_x = 7
start_y = 7

while not findClosedTour(start_x, start_y):
    continue
