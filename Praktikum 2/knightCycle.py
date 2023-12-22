import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# class untuk current_tile
class KnightTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ukuran board
BoardSize = 8

# gerakan knight
x_moves = [1, 1, 2, 2, -1, -1, -2, -2]
y_moves = [2, -2, 1, -1, 2, -2, 1, -1]

# cek apakah tile masih ada dalam knight_tile (gerakan yang diperbolehkan)
def isLegal(x, y):
    return ((x >= 0 and y >= 0) and (x < BoardSize and y < BoardSize))

# Checks apakah tiles berada dalam knight_tile dan kosong
def isEmpty(tour, x, y):
    return (isLegal(x, y)) and (tour[y * BoardSize + x] < 0)

# Cari jumlah tiles kosong yang berdekatan (derajat dari graf knight)
def getDegreeGraph(tour, x, y):
    count = 0
    for i in range(BoardSize):
        if isEmpty(tour, (x + x_moves[i]), (y + y_moves[i])):
            count += 1
    return count

# pilih next move berdasarkan heuristik Warnsdorff
# return false jika tidak bisa memilih
def nextMoveGraph(tour, currentTile):
    min_degree_index = -1 # untuk menyimpan index dengan derajat minimum
    degree = 0
    min_degree = (BoardSize + 1)  # derajat minimum
    next_moves_x = 0
    next_moves_y = 0

    # acak gerakan
    # cari derajat next moves hasil acak
    # lakukan 8 kali dan dapatkan next moves dengan derajat minimum
    start = random.randint(0, 1000) % BoardSize
    for count in range(0, BoardSize):
        i = (start + count) % BoardSize
        next_moves_x = currentTile.x + x_moves[i]
        next_moves_y = currentTile.y + y_moves[i]
        degree = getDegreeGraph(tour, next_moves_x, next_moves_y)
        if ((isEmpty(tour, next_moves_x, next_moves_y)) and degree < min_degree):
            min_degree_index = i
            min_degree = degree

    # Jika tidak ditemukan next moves
    if (min_degree_index == -1):
        return None

    # tiles next_moves
    next_moves_x = currentTile.x + x_moves[min_degree_index]
    next_moves_y = currentTile.y + y_moves[min_degree_index]

    # Masukkan next moves ke tiles
    tour[next_moves_y * BoardSize + next_moves_x] = tour[(currentTile.y) * BoardSize + (currentTile.x)] + 1

    # Update currentTile
    currentTile.x = next_moves_x
    currentTile.y = next_moves_y

    return currentTile

# menampilkan papan catur dengan semua gerakan knight yang diperbolehkan
def print_tour(tour):
    for i in range(BoardSize):
        for j in range(BoardSize):
            print("%d\t" % tour[j * BoardSize + i], end="")
        print()

# cek apakah node tetangganya adalah starting_node
def isNeighbor(x, y, start_x, start_y):
    for i in range(BoardSize):
        if ((x + x_moves[i]) == start_x) and ((y + y_moves[i]) == start_y):
            return True
    return False

# Generates gerakan yang diperbolehkan menggunakan heuristik Warnsdorff. Return false jika tidak mungkin
def findClosedTour(start_x, start_y):
    # Tour array
    tour = [-1] * BoardSize * BoardSize

    # buat currentTile
    currentTile = KnightTile(start_x, start_y)

    tour[currentTile.y * BoardSize + currentTile.x] = 1 # First move

    # Cari next move dengan menggunakan heuristik Warnsdorff
    nextTile = None
    for i in range(BoardSize * BoardSize - 1):
        nextTile = nextMoveGraph(tour, currentTile)
        if nextTile == None:
            return False

    # cek apakah tour closed (node tetangga dari next-tile adalah starting node)
    if not isNeighbor(nextTile.x, nextTile.y, start_x, start_y):
        return False

    # Visualisasi
    x = [coord % BoardSize + 0.5 for coord in tour]
    y = [coord // BoardSize + 0.5 for coord in tour]

    plt.figure(figsize=(8, 8))
    plt.title('Knight\'s Tour')

    # Gambar papan catur
    for i in range(BoardSize):
        for j in range(BoardSize):
            color = 'white' if (i + j) % 2 == 0 else 'black'
            plt.gca().add_patch(patches.Rectangle((i, j), 1, 1, linewidth=1, edgecolor='black', facecolor=color))

    plt.scatter(x, y, color='red', s=50, zorder=2)  # Titik
    plt.plot(x, y, color='yellow', linestyle='-', linewidth=2, zorder=1)  # Garis Kuning

    # Titik Awal dan Akhir, dan penentuan warnanya
    plt.scatter(x[0], y[0], color='blue', s=100, label='Start', zorder=3)  # Titik Awal
    plt.scatter(x[-1], y[-1], color='blue', s=100, label='End', zorder=3)  # Titik Akhir

    plt.legend()
    plt.show()

    return True

# Driver Code

# posisi awal
start_x = 7
start_y = 7

## Hamiltonian Cycle
# loop sampai ketemu solusi
while not findClosedTour(start_x, start_y):
    continue
