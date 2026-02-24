"""
Game of Life - Implementasi menggunakan ADT Array
Berdasarkan definisi ADT Array dari dokumen
"""

import time
import os

# ============== ADT ARRAY ==============
class Array:
    """Implementasi ADT Array satu dimensi"""
    
    def __init__(self, size):
        """
        Membuat array dengan ukuran tertentu
        Pra-kondisi: size > 0
        """
        if size <= 0:
            raise ValueError("Ukuran array harus lebih besar dari 0")
        
        self._size = size
        self._data = [None] * size
    
    def length(self):
        """Mengembalikan panjang array"""
        return self._size
    
    def getitem(self, index):
        """
        Mengembalikan nilai pada indeks tertentu
        Pra-kondisi: index dalam rentang 0..size-1
        """
        if index < 0 or index >= self._size:
            raise IndexError("Indeks di luar rentang array")
        return self._data[index]
    
    def setitem(self, index, value):
        """
        Mengubah nilai pada indeks tertentu
        Pra-kondisi: index dalam rentang 0..size-1
        """
        if index < 0 or index >= self._size:
            raise IndexError("Indeks di luar rentang array")
        self._data[index] = value
    
    def clearing(self, value):
        """Mengosongkan array dengan nilai tertentu"""
        for i in range(self._size):
            self._data[i] = value
    
    def __iter__(self):
        """Membuat iterator untuk array"""
        return iter(self._data)
    
    def __str__(self):
        """Representasi string dari array"""
        return str(self._data)


# ============== GRID 2D MENGGUNAKAN ARRAY ==============
class Grid:
    """Implementasi grid 2D menggunakan Array"""
    
    def __init__(self, rows, cols):
        """
        Membuat grid dengan ukuran rows x cols
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensi grid harus lebih besar dari 0")
        
        self._rows = rows
        self._cols = cols
        self._grid = Array(rows)
        
        for i in range(rows):
            self._grid.setitem(i, Array(cols))
    
    def rows(self):
        """Mengembalikan jumlah baris"""
        return self._rows
    
    def cols(self):
        """Mengembalikan jumlah kolom"""
        return self._cols
    
    def get_cell(self, row, col):
        """
        Mengembalikan nilai sel pada posisi (row, col)
        """
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError("Posisi sel di luar rentang grid")
        
        row_array = self._grid.getitem(row)
        return row_array.getitem(col)
    
    def set_cell(self, row, col, value):
        """
        Mengubah nilai sel pada posisi (row, col)
        """
        if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
            raise IndexError("Posisi sel di luar rentang grid")
        
        row_array = self._grid.getitem(row)
        row_array.setitem(col, value)
    
    def clear_grid(self, value):
        """
        Mengosongkan seluruh grid dengan nilai tertentu
        """
        for i in range(self._rows):
            row_array = self._grid.getitem(i)
            row_array.clearing(value)
    
    def __str__(self):
        """Representasi string dari grid"""
        result = ""
        for i in range(self._rows):
            row_array = self._grid.getitem(i)
            for j in range(self._cols):
                cell = row_array.getitem(j)
                if cell == 1:
                    result += "■ "  # Sel hidup
                else:
                    result += "□ "  # Sel mati
            result += "\n"
        return result


# ============== GAME OF LIFE ==============
class GameOfLife:
    """Implementasi Game of Life menggunakan ADT Array"""
    
    def __init__(self, rows, cols):
        """
        Inisialisasi game dengan grid berukuran rows x cols
        """
        self._rows = rows
        self._cols = cols
        self._grid = Grid(rows, cols)
        self._generation = 0
        
        # Inisialisasi semua sel mati
        self._grid.clear_grid(0)
    
    def set_initial_pattern(self, pattern):
        """
        Mengatur pola awal permainan
        pattern: list of tuples (row, col) untuk sel hidup
        """
        for row, col in pattern:
            if 0 <= row < self._rows and 0 <= col < self._cols:
                self._grid.set_cell(row, col, 1)
    
    def count_neighbors(self, row, col):
        """
        Menghitung jumlah tetangga hidup untuk sel pada posisi (row, col)
        Tetangga mencakup 8 sel di sekitar: vertikal, horizontal, diagonal
        """
        count = 0
        for i in range(-1, 2):  # -1, 0, 1
            for j in range(-1, 2):  # -1, 0, 1
                # Abaikan sel itu sendiri
                if i == 0 and j == 0:
                    continue
                
                # Hitung posisi tetangga
                neighbor_row = row + i
                neighbor_col = col + j
                
                # Periksa apakah posisi tetangga valid
                if 0 <= neighbor_row < self._rows and 0 <= neighbor_col < self._cols:
                    if self._grid.get_cell(neighbor_row, neighbor_col) == 1:
                        count += 1
        return count
    
    def next_generation(self):
        """
        Menghitung generasi berikutnya berdasarkan aturan Game of Life
        """
        # Buat grid baru untuk generasi berikutnya
        next_grid = Grid(self._rows, self._cols)
        next_grid.clear_grid(0)
        
        # Terapkan aturan untuk setiap sel
        for i in range(self._rows):
            for j in range(self._cols):
                current_cell = self._grid.get_cell(i, j)
                neighbors = self.count_neighbors(i, j)
                
                # Aturan Game of Life
                if current_cell == 1:  # Sel hidup
                    if neighbors in [2, 3]:
                        # Aturan 1: Tetap hidup jika memiliki 2 atau 3 tetangga
                        next_grid.set_cell(i, j, 1)
                    else:
                        # Aturan 2 & 3: Mati jika <2 atau >3 tetangga
                        next_grid.set_cell(i, j, 0)
                else:  # Sel mati
                    if neighbors == 3:
                        # Aturan 4: Lahir jika tepat 3 tetangga
                        next_grid.set_cell(i, j, 1)
        
        # Update grid
        self._grid = next_grid
        self._generation += 1
    
    def run(self, generations=10, delay=0.5):
        """
        Menjalankan simulasi Game of Life
        generations: jumlah generasi yang akan dijalankan
        delay: waktu delay antar generasi (detik)
        """
        print(f"Game of Life - Generasi ke-{self._generation}")
        print(self._grid)
        
        for gen in range(1, generations + 1):
            time.sleep(delay)
            os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
            
            self.next_generation()
            print(f"Game of Life - Generasi ke-{self._generation}")
            print(self._grid)
    
    def get_statistics(self):
        """Mengembalikan statistik permainan"""
        total_cells = self._rows * self._cols
        live_cells = 0
        
        for i in range(self._rows):
            for j in range(self._cols):
                if self._grid.get_cell(i, j) == 1:
                    live_cells += 1
        
        return {
            'generation': self._generation,
            'live_cells': live_cells,
            'dead_cells': total_cells - live_cells,
            'total_cells': total_cells
        }


# ============== FUNGSI UTAMA ==============
def main():
    """Program utama untuk mendemonstrasikan Game of Life"""
    
    print("=" * 60)
    print("               GAME OF LIFE - John H. Conway")
    print("=" * 60)
    print("\nGame of Life adalah cellular automata yang diciptakan oleh")
    print("matematikawan Inggris John H. Conway pada tahun 1970.")
    print("\nAturan Permainan:")
    print("1. Sel hidup dengan 2 atau 3 tetangga hidup -> tetap hidup")
    print("2. Sel hidup dengan <2 tetangga hidup -> mati (terisolasi)")
    print("3. Sel hidup dengan >3 tetangga hidup -> mati (overpopulasi)")
    print("4. Sel mati dengan tepat 3 tetangga hidup -> hidup (kelahiran)")
    print("=" * 60)
    
    # Buat game dengan grid 20x20
    game = GameOfLife(20, 20)
    
    # Pola-pola menarik yang bisa dicoba
    patterns = {
        "1": {
            "name": "Blinker (Oscillator 2 fase)",
            "description": "Pola berkedip yang bergantian antara horizontal dan vertikal",
            "pattern": [(10, 9), (10, 10), (10, 11)]
        },
        "2": {
            "name": "Glider (bergerak diagonal)",
            "description": "Pola yang bergerak secara diagonal melintasi grid",
            "pattern": [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        },
        "3": {
            "name": "Block (Stabil)",
            "description": "Pola statis yang tidak berubah antar generasi",
            "pattern": [(10, 10), (10, 11), (11, 10), (11, 11)]
        },
        "4": {
            "name": "Beehive (Stabil)",
            "description": "Pola statis berbentuk sarang lebah",
            "pattern": [(10, 10), (10, 11), (11, 9), (11, 12), (12, 10), (12, 11)]
        },
        "5": {
            "name": "Toad (Oscillator 2 fase)",
            "description": "Pola yang berosilasi antara dua bentuk",
            "pattern": [(10, 10), (10, 11), (10, 12), (11, 9), (11, 10), (11, 11)]
        },
        "6": {
            "name": "Lightweight Spaceship (LWSS)",
            "description": "Pola yang bergerak horizontal melintasi grid",
            "pattern": [
                (5, 5), (5, 8),
                (6, 9),
                (7, 4), (7, 9),
                (8, 5), (8, 6), (8, 7), (8, 8)
            ]
        },
        "7": {
            "name": "Pola Acak",
            "description": "Menghasilkan pola acak untuk observasi",
            "pattern": "random"
        }
    }
    
    # Tampilkan pilihan pola
    print("\n" + "=" * 60)
    print("PILIH POLA AWAL:")
    print("=" * 60)
    for key, pattern in patterns.items():
        print(f"{key}. {pattern['name']}")
        print(f"   {pattern['description']}")
    
    # Minta input dari user
    choice = input("\nMasukkan pilihan (1-7): ").strip()
    
    if choice in patterns and choice != "7":
        print(f"\nMemulai dengan pola: {patterns[choice]['name']}")
        game.set_initial_pattern(patterns[choice]["pattern"])
    elif choice == "7":
        print("\nMemulai dengan pola acak...")
        # Generate pola acak (sekitar 30% sel hidup)
        import random
        random_pattern = []
        for i in range(20):
            for j in range(20):
                if random.random() < 0.3:  # 30% kemungkinan hidup
                    random_pattern.append((i, j))
        game.set_initial_pattern(random_pattern)
    else:
        print("\nPilihan tidak valid. Menggunakan pola default (Blinker)")
        game.set_initial_pattern(patterns["1"]["pattern"])
    
    # Tampilkan statistik awal
    stats = game.get_statistics()
    print(f"\nSTATISTIK AWAL:")
    print(f"├─ Generasi ke-: {stats['generation']}")
    print(f"├─ Sel Hidup   : {stats['live_cells']}")
    print(f"├─ Sel Mati    : {stats['dead_cells']}")
    print(f"└─ Total Sel   : {stats['total_cells']}")
    
    # Tampilkan grid awal
    print("\nKONFIGURASI AWAL:")
    print(game._grid)
    
    # Minta jumlah generasi
    try:
        gen_input = input("\nMasukkan jumlah generasi yang akan dijalankan (default: 20): ").strip()
        generations = int(gen_input) if gen_input else 20
        
        delay_input = input("Masukkan delay antar generasi dalam detik (default: 0.3): ").strip()
        delay = float(delay_input) if delay_input else 0.3
        
        input("\nTekan Enter untuk memulai simulasi...")
        
        # Jalankan simulasi
        game.run(generations=generations, delay=delay)
        
    except KeyboardInterrupt:
        print("\n\nSimulasi dihentikan oleh user")
    except ValueError:
        print("\nInput tidak valid. Menggunakan nilai default.")
        game.run(generations=20, delay=0.3)
    
    # Tampilkan statistik akhir
    stats = game.get_statistics()
    print(f"\nSTATISTIK AKHIR:")
    print(f"├─ Generasi ke-: {stats['generation']}")
    print(f"├─ Sel Hidup   : {stats['live_cells']}")
    print(f"├─ Sel Mati    : {stats['dead_cells']}")
    print(f"└─ Total Sel   : {stats['total_cells']}")
    
    if stats['live_cells'] == 0:
        print("\n⚠️  Semua organisme telah punah!")
    elif stats['live_cells'] == stats['total_cells']:
        print("\n⚠️  Grid penuh! Populasi mencapai maksimum.")
    
    print("\n" + "=" * 60)
    print("Terima kasih telah mencoba Game of Life!")
    print("=" * 60)


# ============== FUNGSI DEMO CEPAT ==============
def demo_quick():
    """Fungsi untuk demonstrasi cepat pola-pola terkenal"""
    
    print("\n" + "=" * 60)
    print("DEMONSTRASI CEPAT POLA-POLA GAME OF LIFE")
    print("=" * 60)
    
    # Demo pola sederhana
    demo_patterns = [
        ("Blinker (Oscillator)", [(10, 9), (10, 10), (10, 11)], 6),
        ("Block (Stabil)", [(10, 10), (10, 11), (11, 10), (11, 11)], 3),
        ("Glider (Bergerak)", [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)], 10)
    ]
    
    for name, pattern, gens in demo_patterns:
        print(f"\n\n>>> DEMO: {name} <<<")
        game = GameOfLife(15, 15)
        game.set_initial_pattern(pattern)
        
        for _ in range(gens):
            print(f"\nGenerasi {game.get_statistics()['generation']}:")
            print(game._grid)
            game.next_generation()
            time.sleep(0.5)
        
        input("\nTekan Enter untuk lanjut ke demo berikutnya...")


# ============== PROGRAM UTAMA ==============
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 60)
        print("GAME OF LIFE - MENU UTAMA")
        print("=" * 60)
        print("1. Jalankan simulasi interaktif")
        print("2. Demo cepat pola-pola terkenal")
        print("3. Keluar")
        
        choice = input("\nPilih menu (1-3): ").strip()
        
        if choice == "1":
            main()
        elif choice == "2":
            demo_quick()
        elif choice == "3":
            print("\nTerima kasih! Sampai jumpa.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")