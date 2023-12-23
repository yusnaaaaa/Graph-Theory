# Graph-Theory

## Group Member

| NRP        | Name                        |
| ---------- | --------------------------- |
| 5025211050 | Rule Lulu Damara            |
| 5025211057 | Salsabila Fatma Aripa       |
| 5025211254 | Yusna Millaturrosyidah      |

## Pre

```bash
(1, 2, 2)
#1: Menunjukkan langkah ke berapa
#(2,2) menunjukkan koordinat
```
![image](https://github.com/yusnaaaaa/Graph-Theory/assets/105763198/d44f954c-de41-4c9d-8820-b4a252a45020)


## Praktikum 2 LIS
class SegmentTree
```bash
class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def update_value(self, index, value):
        index += self.size
        self.tree[index] = value

        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0

        while left < right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1

            if right % 2 == 1:
                right -= 1
                result = max(result, self.tree[right])

            left //= 2
            right //= 2

        return result
```

Kelas ini bertanggung jawab mengelola pohon segmen, yang memungkinkan kita mencari nilai maksimum di dalam suatu rentang di dalam sebuah array.
__init__(self, size): Ketika kita membuat objek SegmentTree, kita perlu memberikan ukuran array yang akan dikelola oleh pohon segmen ini. Awalnya, pohon segmen diinisialisasi dengan semua nilai 0.
update_value(self, index, value): Jika kita ingin mengubah nilai pada indeks tertentu dalam array, kita bisa menggunakan metode ini. Metode ini secara otomatis memperbarui pohon segmen agar tetap konsisten dengan perubahan kita.
query(self, left, right): Ketika kita ingin mengetahui nilai maksimum di dalam suatu rentang (dari indeks left hingga right) dalam array, kita dapat menggunakan metode ini.

longest_increasing_subsequence_length(nums)
```bash
def longest_increasing_subsequence_length(nums):
    n = len(nums)
    index_mapping = {num: i for i, num in enumerate(sorted(set(nums)))}
    segment_tree = SegmentTree(len(index_mapping))
    lis_lengths = [0] * n

    for i, num in enumerate(nums):
        index = index_mapping[num]
        lis_lengths[i] = segment_tree.query(0, index) + 1
        segment_tree.update_value(index, lis_lengths[i])

        # Visualization
        visualize_lis_lengths(lis_lengths)
        visualize_segment_tree(segment_tree)

    return max(lis_lengths)
```
Fungsi ini bertujuan untuk menghitung panjang dari Subsequence Meningkat Terpanjang (LIS) dari array nums.
Fungsi ini menggunakan pohon segmen untuk melakukan perhitungan ini dengan efisien.
Selama proses perhitungan, kita juga mencetak langkah-langkah visualisasi untuk membantu pemahaman.
Dalam contoh yang diberikan, array nums adalah [4, 1, 13, 7, 0, 2, 8, 11, 3].
Fungsi longest_increasing_subsequence_length dipanggil untuk menghitung panjang LIS dari array tersebut.
Hasilnya dicetak, dan selama eksekusi, langkah-langkah visualisasi panjang LIS dan pohon segmen juga dicetak.
OUTPUT
```bash
LIS Lengths: [1, 0, 0, 0, 0, 0, 0, 0, 0]

Segment Tree:
[0, 0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0]
[0, 0]
[0]

LIS Lengths: [1, 1, 0, 0, 0, 0, 0, 0, 0]

Segment Tree:
[0, 1, 0, 0, 1, 0, 0, 0, 0]
[1, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0]
[1, 0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0]
[0, 0]
[0]

LIS Lengths: [1, 1, 2, 0, 0, 0, 0, 0, 0]

Segment Tree:
[0, 1, 0, 0, 1, 0, 0, 0, 2]
[1, 0, 0, 1, 0, 0, 0, 2]
[0, 0, 1, 0, 0, 0, 2]
[0, 1, 0, 0, 0, 2]
[1, 0, 0, 0, 2]
[0, 0, 0, 2]
[0, 0, 2]
[0, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 0, 0, 0, 0, 0]

Segment Tree:
[0, 1, 0, 0, 1, 2, 0, 0, 2]
[1, 0, 0, 1, 2, 0, 0, 2]
[0, 0, 1, 2, 0, 0, 2]
[0, 1, 2, 0, 0, 2]
[1, 2, 0, 0, 2]
[2, 0, 0, 2]
[0, 0, 2]
[0, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 1, 0, 0, 0, 0]

Segment Tree:
[1, 1, 0, 0, 1, 2, 0, 0, 2]
[1, 0, 0, 1, 2, 0, 0, 2]
[0, 0, 1, 2, 0, 0, 2]
[0, 1, 2, 0, 0, 2]
[1, 2, 0, 0, 2]
[2, 0, 0, 2]
[0, 0, 2]
[0, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 1, 2, 0, 0, 0]

Segment Tree:
[1, 1, 2, 0, 1, 2, 0, 0, 2]
[1, 2, 0, 1, 2, 0, 0, 2]
[2, 0, 1, 2, 0, 0, 2]
[0, 1, 2, 0, 0, 2]
[1, 2, 0, 0, 2]
[2, 0, 0, 2]
[0, 0, 2]
[0, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 1, 2, 3, 0, 0]

Segment Tree:
[1, 1, 2, 0, 1, 2, 3, 0, 2]
[1, 2, 0, 1, 2, 3, 0, 2]
[2, 0, 1, 2, 3, 0, 2]
[0, 1, 2, 3, 0, 2]
[1, 2, 3, 0, 2]
[2, 3, 0, 2]
[3, 0, 2]
[0, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 1, 2, 3, 4, 0]

Segment Tree:
[1, 1, 2, 0, 1, 2, 3, 4, 2]
[1, 2, 0, 1, 2, 3, 4, 2]
[2, 0, 1, 2, 3, 4, 2]
[0, 1, 2, 3, 4, 2]
[1, 2, 3, 4, 2]
[2, 3, 4, 2]
[3, 4, 2]
[4, 2]
[2]

LIS Lengths: [1, 1, 2, 2, 1, 2, 3, 4, 3]

Segment Tree:
[1, 1, 2, 3, 1, 2, 3, 4, 2]
[1, 2, 3, 1, 2, 3, 4, 2]
[2, 3, 1, 2, 3, 4, 2]
[3, 1, 2, 3, 4, 2]
[1, 2, 3, 4, 2]
[2, 3, 4, 2]
[3, 4, 2]
[4, 2]
[2]

Panjang Largest Monotonically Increasing Subsequence: 4
```

## Praktikum 3 Knight Cycle
### Open Tour
```bash
class KnightGraph:
    # Inisialisasi objek KnightGraph dengan ukuran papan catur (n).
    def __init__(self, n):
        self.n = n
        self.graph = {i * n + j: [] for i in range(n) for j in range(n)}
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
```
Inisialisasi objek KnightGraph dengan ukuran papan catur (n).


def is_legal_move(self, x, y):
```bash
    # Memeriksa apakah langkah yang diinginkan oleh kuda masih berada dalam batas papan catur.
    def is_legal_move(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n
    # memeriksa kemungkinan gerakan kuda dan menambahkan edge pada graf jika gerakan
    # tersebut legal, sesuai dengan aturan pergerakan kuda pada catur.
```

def generate_graph(self):
```bash
    def generate_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                current_node = i * self.n + j
                for move in self.moves:
                    x, y = i + move[0], j + move[1]
                    if self.is_legal_move(x, y):
                        next_node = x * self.n + y
                        self.graph[current_node].append(next_node)
```
Membangun graf yang merepresentasikan kemungkinan gerakan kuda di papan catur. Setiap petak pada papan adalah node, dan setiap kemungkinan gerakan kuda dari satu petak ke petak lainnya adalah edge.

print_board(self, tour)
```bash
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
```
Menampilkan visualisasi papan catur dengan langkah-langkah perjalanan kuda.
Digunakan modul Matplotlib untuk menggambar papan catur dan menunjukkan perjalanan kuda dengan warna dan label yang berbeda.

Menampilkan representasi papan catur dengan langkah-langkah perjalanan kuda di terminal. Setiap langkah diberi nomor urut.

generate_tour(self, start_node)
```bash
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
```
Membangkitkan perjalanan kuda pada papan catur dengan menggunakan Depth-First Search (DFS).
DFS dimulai dari posisi awal kuda (start_node) dan menelusuri semua kemungkinan langkah kuda hingga papan terisi penuh.

```bash
# Driver Code
# membuat dan mengeksekusi tur kuda pada papan catur berukuran 8x8
n = 8  # Board size
knight_graph = KnightGraph(n)
knight_graph.generate_graph()

start_x = 0
start_y = 0
start_node = start_y * n + start_x

tour = knight_graph.generate_tour(start_node)
```

Output
```bash
[1, 47, 62, 34, 31, 18, 9, 36]
[61, 54, 32, 46, 10, 35, 30, 17]
[48, 2, 44, 37, 33, 28, 19, 8]
[53, 60, 39, 27, 45, 11, 16, 29]
[59, 49, 3, 43, 38, 24, 7, 20]
[63, 52, 56, 40, 26, 21, 12, 15]
[50, 58, 42, 4, 23, 14, 25, 6]
[55, 64, 51, 57, 41, 5, 22, 13]
```
![image](https://github.com/yusnaaaaa/Graph-Theory/assets/105763198/19d757ae-8d6e-421d-bf15-d4256c24acc6)


### Close Tour
Function print_tour
```bash
def print_tour(tour):
    for i in range(N):
        for j in range(N):
            print("(%d, %d, %d)\t" % (tour[j * N + i], i, j), end="")
        print()
```
Fungsi ini mengambil input berupa list tour, di mana tour merepresentasikan urutan langkah yang dilakukan oleh kuda di papan catur.
Fungsi ini mencetak Knights tour dalam bentuk grid, di mana setiap sel berisi tiga nilai: nomor langkah, indeks baris, dan indeks kolom.

Function findClosedTour(start_x, start_y)
```bash
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

    tour[start_y * N + start_x] = tour[(current_tile.y) * N + (current_tile.x)] + 1
    print_tour(tour)

    return True
```
Fungsi ini berusaha menemukan tour closed (tour di mana kuda kembali ke posisi awalnya) di papan catur, dimulai dari posisi yang ditentukan (start_x, start_y).
Fungsi ini menginisialisasi list tour, yang merepresentasikan langkah-langkah kuda, dan menetapkan posisi awal ke nomor langkah 1.
Selanjutnya, fungsi secara iteratif memanggil fungsi nextMove untuk membuat langkah-langkah berikutnya sampai tour closed ditemukan atau semua kemungkinan telah dijelajahi.
Jika tour closed ditemukan, fungsi mencetak tour tersebut menggunakan fungsi print_tour dan mengembalikan True; sebaliknya, mengembalikan False.

```bash
start_x = 7
start_y = 7

while not findClosedTour(start_x, start_y):
    continue
```
Ini untuk initial state

OUTPUT
```bash
(49, 0, 0)	(10, 0, 1)	(29, 0, 2)	(26, 0, 3)	(59, 0, 4)	(12, 0, 5)	(31, 0, 6)	(16, 0, 7)	
(28, 1, 0)	(25, 1, 1)	(50, 1, 2)	(11, 1, 3)	(30, 1, 4)	(15, 1, 5)	(62, 1, 6)	(13, 1, 7)	
(9, 2, 0)	(48, 2, 1)	(27, 2, 2)	(60, 2, 3)	(53, 2, 4)	(58, 2, 5)	(17, 2, 6)	(32, 2, 7)	
(24, 3, 0)	(55, 3, 1)	(38, 3, 2)	(51, 3, 3)	(36, 3, 4)	(61, 3, 5)	(14, 3, 6)	(63, 3, 7)	
(39, 4, 0)	(8, 4, 1)	(47, 4, 2)	(54, 4, 3)	(57, 4, 4)	(52, 4, 5)	(33, 4, 6)	(18, 4, 7)	
(46, 5, 0)	(23, 5, 1)	(56, 5, 2)	(37, 5, 3)	(42, 5, 4)	(35, 5, 5)	(64, 5, 6)	(3, 5, 7)	
(7, 6, 0)	(40, 6, 1)	(21, 6, 2)	(44, 6, 3)	(5, 6, 4)	(2, 6, 5)	(19, 6, 6)	(34, 6, 7)	
(22, 7, 0)	(45, 7, 1)	(6, 7, 2)	(41, 7, 3)	(20, 7, 4)	(43, 7, 5)	(4, 7, 6)	(65, 7, 7)
```
