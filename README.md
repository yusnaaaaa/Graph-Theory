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


##Praktikum 2 LIS
##Praktikum 3 Knight Cycle
## Open Tour
## Close Tour

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
