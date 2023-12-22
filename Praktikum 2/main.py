# import matplot untuk visualisasi papan catur yang dilalui
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class KnightGraph:
    # Inisialisasi objek KnightGraph dengan ukuran papan catur (n).
    def __init__(self, n):
        self.n = n
        self.graph = {i * n + j: [] for i in range(n) for j in range(n)}
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
    # Memeriksa apakah langkah yang diinginkan oleh kuda masih berada dalam batas papan catur.
    def is_legal_move(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n
    
    # memeriksa kemungkinan gerakan kuda dan menambahkan edge pada graf jika gerakan 
    # tersebut legal, sesuai dengan aturan pergerakan kuda pada catur. 
    def generate_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                current_node = i * self.n + j
                for move in self.moves:
                    x, y = i + move[0], j + move[1]
                    if self.is_legal_move(x, y):
                        next_node = x * self.n + y
                        self.graph[current_node].append(next_node)

    # visualisasi pada board
    def print_board(self, tour):
        x = [coord % self.n + 0.5 for coord in tour]
        y = [coord // self.n + 0.5 for coord in tour]

        plt.figure(figsize=(8, 8))
        plt.title('Knight\'s Tour')

        # Gambar papan catur
        for i in range(self.n):
            for j in range(self.n):
                color = 'white' if (i + j) % 2 == 0 else 'black'
                plt.gca().add_patch(patches.Rectangle((i, j), 1, 1, linewidth=1, edgecolor='black', facecolor=color))

        plt.scatter(x, y, color='red', s=50, zorder=2)  # Titik
        plt.plot(x, y, color='yellow', linestyle='-', linewidth=2, zorder=1)  # Garis Kuning

        # Titik Awal dan Akhir, dan penentuan warnanya
        plt.scatter(x[0], y[0], color='blue', s=100, label='Start', zorder=3)  # Titik Awal
        plt.scatter(x[-1], y[-1], color='blue', s=100, label='End', zorder=3)  # Titik Akhir

        plt.legend()
        plt.show()

    # menampilkan representasi papan catur dengan langkah-langkah perjalanan kuda di terminal. 
    def print_terminal(self, tour):
        board = [[0] * self.n for _ in range(self.n)]
        i = 1
        for tile in tour:
            row, col = divmod(tile, self.n)
            board[row][col] = i
            i += 1

        for row in board:
            print(row)

    # menghasilkan dan menampilkan perjalanan kuda pada papan catur, baik dalam bentuk 
    # representasi terminal maupun visualisasi menggunakan Matplotlib.
    def generate_tour(self, start_node):
        visited = set()
        tour = []

        def dfs(node):
            nonlocal tour
            tour.append(node)
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_node)
        self.print_terminal(tour)
        self.print_board(tour)
        return tour

# Driver Code
# membuat dan mengeksekusi tur kuda pada papan catur berukuran 8x8
n = 8  # Board size
knight_graph = KnightGraph(n)
knight_graph.generate_graph()

start_x = 0
start_y = 0
start_node = start_y * n + start_x

tour = knight_graph.generate_tour(start_node)
