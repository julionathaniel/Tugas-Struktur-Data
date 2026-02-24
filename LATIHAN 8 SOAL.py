"""
LATIHAN SOAL - STRUKTUR DATA (ARRAY/LIST, SET, DICTIONARY)
"""

# ============================================================
# SOAL 1: DEDUPLIKASI
# ============================================================
def deduplikasi(lst):
    """
    Menghapus duplikat dari list dengan mempertahankan urutan kemunculan pertama
    
    Parameter:
        lst (list): List yang mungkin mengandung duplikat
    
    Return:
        list: List baru tanpa duplikat (urutan pertama dipertahankan)
    """
    seen = set()        # Untuk melacak elemen yang sudah dilihat
    result = []         # List untuk menyimpan hasil
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


# Contoh penggunaan dan testing
print("=" * 60)
print("SOAL 1: DEDUPLIKASI")
print("=" * 60)

data1 = [1, 2, 3, 2, 1, 4, 5, 4, 6]
print(f"Input  : {data1}")
print(f"Output : {deduplikasi(data1)}")

data2 = ['apel', 'jeruk', 'apel', 'mangga', 'jeruk', 'pisang']
print(f"\nInput  : {data2}")
print(f"Output : {deduplikasi(data2)}")

data3 = [True, False, True, True, False]
print(f"\nInput  : {data3}")
print(f"Output : {deduplikasi(data3)}")


# ============================================================
# SOAL 2: INTERSECTION DUA ARRAY
# ============================================================
def intersection(array1, array2):
    """
    Mencari elemen yang muncul di kedua array
    
    Parameter:
        array1 (list): Array pertama
        array2 (list): Array kedua
    
    Return:
        list: Elemen yang muncul di kedua array (tanpa duplikat)
    """
    set1 = set(array1)
    set2 = set(array2)
    
    # Intersection menggunakan operator &
    result = list(set1 & set2)
    
    # Urutkan agar rapi (opsional)
    result.sort()
    
    return result


print("\n\n" + "=" * 60)
print("SOAL 2: INTERSECTION DUA ARRAY")
print("=" * 60)

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(f"Array 1 : {arr1}")
print(f"Array 2 : {arr2}")
print(f"Irisan  : {intersection(arr1, arr2)}")

arr3 = ['a', 'b', 'c', 'd']
arr4 = ['c', 'd', 'e', 'f']
print(f"\nArray 1 : {arr3}")
print(f"Array 2 : {arr4}")
print(f"Irisan  : {intersection(arr3, arr4)}")

arr5 = [10, 20, 30, 40]
arr6 = [50, 60, 70, 80]
print(f"\nArray 1 : {arr5}")
print(f"Array 2 : {arr6}")
print(f"Irisan  : {intersection(arr5, arr6)} (kosong)")


# ============================================================
# SOAL 3: ANAGRAM CHECK
# ============================================================
def anagram_check(str1, str2):
    """
    Memeriksa apakah dua string adalah anagram
    
    Parameter:
        str1 (str): String pertama
        str2 (str): String kedua
    
    Return:
        bool: True jika anagram, False jika bukan
    """
    # Hapus spasi dan ubah ke huruf kecil (case insensitive)
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Jika panjang berbeda, pasti bukan anagram
    if len(str1) != len(str2):
        return False
    
    # Hitung frekuensi karakter menggunakan dictionary
    char_count = {}
    
    # Hitung karakter di string pertama
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Kurangi dengan karakter di string kedua
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    # Periksa apakah semua count = 0
    return all(count == 0 for count in char_count.values())


# Alternatif implementasi yang lebih sederhana
def anagram_check_simple(str1, str2):
    """Versi sederhana menggunakan sorting"""
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


print("\n\n" + "=" * 60)
print("SOAL 3: ANAGRAM CHECK")
print("=" * 60)

test_cases = [
    ("listen", "silent"),
    ("hello", "world"),
    ("anagram", "nagaram"),
    ("Dormitory", "Dirty room"),
    ("The eyes", "They see"),
    ("python", "java")
]

for s1, s2 in test_cases:
    result = anagram_check(s1, s2)
    result_symbol = "✓" if result else "✗"
    print(f"'{s1}'  vs  '{s2}' : {result_symbol} Anagram")


# ============================================================
# SOAL 4: FIRST RECURRING CHARACTER
# ============================================================
def first_recurring_char(text):
    """
    Menemukan karakter pertama yang muncul lebih dari sekali
    
    Parameter:
        text (str): String yang akan diperiksa
    
    Return:
        str or None: Karakter pertama yang berulang, atau None jika tidak ada
    """
    seen = set()
    
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    
    return None  # Tidak ada karakter yang berulang


print("\n\n" + "=" * 60)
print("SOAL 4: FIRST RECURRING CHARACTER")
print("=" * 60)

strings = [
    "ABCDA",      # A berulang
    "ABCA",       # A berulang
    "ABCC",       # C berulang
    "ABCDEF",     # Tidak ada yang berulang
    "Pemrograman", # 'r' berulang? (case sensitive)
    "123421",     # '2' berulang
    "a a b c"     # spasi juga dianggap karakter
]

for s in strings:
    result = first_recurring_char(s)
    if result:
        print(f"'{s}' -> karakter pertama yang berulang: '{result}'")
    else:
        print(f"'{s}' -> tidak ada karakter yang berulang")


# ============================================================
# SOAL 5: SIMULASI BUKU TELEPON
# ============================================================
class BukuTelepon:
    """Simulasi buku telepon sederhana"""
    
    def __init__(self):
        self.kontak = {}  # Dictionary: nama -> nomor
        self.running = True
    
    def tambah_kontak(self, nama, nomor):
        """Menambahkan kontak baru"""
        if nama in self.kontak:
            print(f"Kontak '{nama}' sudah ada. Gunakan menu ubah jika ingin memperbarui.")
        else:
            self.kontak[nama] = nomor
            print(f"✓ Kontak '{nama}' berhasil ditambahkan")
    
    def cari_kontak(self, nama):
        """Mencari kontak berdasarkan nama"""
        if nama in self.kontak:
            print(f"📞 {nama}: {self.kontak[nama]}")
        else:
            print(f"✗ Kontak '{nama}' tidak ditemukan")
    
    def tampilkan_semua(self):
        """Menampilkan semua kontak"""
        if not self.kontak:
            print("📭 Buku telepon kosong")
        else:
            print("\n" + "=" * 40)
            print("         DAFTAR KONTAK")
            print("=" * 40)
            
            # Urutkan berdasarkan nama
            for i, (nama, nomor) in enumerate(sorted(self.kontak.items()), 1):
                print(f"{i:2}. {nama:15} : {nomor}")
            
            print(f"\nTotal kontak: {len(self.kontak)}")
    
    def hapus_kontak(self, nama):
        """Menghapus kontak"""
        if nama in self.kontak:
            del self.kontak[nama]
            print(f"✓ Kontak '{nama}' berhasil dihapus")
        else:
            print(f"✗ Kontak '{nama}' tidak ditemukan")
    
    def ubah_kontak(self, nama, nomor_baru):
        """Mengubah nomor kontak"""
        if nama in self.kontak:
            self.kontak[nama] = nomor_baru
            print(f"✓ Nomor kontak '{nama}' berhasil diubah")
        else:
            print(f"✗ Kontak '{nama}' tidak ditemukan")
    
    def menu(self):
        """Menampilkan menu interaktif"""
        while self.running:
            print("\n" + "=" * 50)
            print("         SIMULASI BUKU TELEPON")
            print("=" * 50)
            print("1. 📱 Tambah kontak")
            print("2. 🔍 Cari kontak")
            print("3. 📋 Tampilkan semua kontak")
            print("4. ✏️  Ubah kontak")
            print("5. 🗑️  Hapus kontak")
            print("6. 🚪 Keluar")
            print("-" * 50)
            
            pilihan = input("Pilih menu (1-6): ").strip()
            
            if pilihan == "1":
                print("\n--- TAMBAH KONTAK ---")
                nama = input("Nama: ").strip()
                if nama:
                    nomor = input("Nomor telepon: ").strip()
                    self.tambah_kontak(nama, nomor)
                else:
                    print("Nama tidak boleh kosong!")
            
            elif pilihan == "2":
                print("\n--- CARI KONTAK ---")
                nama = input("Masukkan nama yang dicari: ").strip()
                self.cari_kontak(nama)
            
            elif pilihan == "3":
                self.tampilkan_semua()
            
            elif pilihan == "4":
                print("\n--- UBAH KONTAK ---")
                nama = input("Nama kontak yang akan diubah: ").strip()
                if nama in self.kontak:
                    nomor_baru = input("Nomor baru: ").strip()
                    self.ubah_kontak(nama, nomor_baru)
                else:
                    print(f"✗ Kontak '{nama}' tidak ditemukan")
            
            elif pilihan == "5":
                print("\n--- HAPUS KONTAK ---")
                nama = input("Nama kontak yang akan dihapus: ").strip()
                self.hapus_kontak(nama)
            
            elif pilihan == "6":
                print("\nTerima kasih telah menggunakan Buku Telepon!")
                self.running = False
            
            else:
                print("\nPilihan tidak valid! Silakan pilih 1-6.")
            
            if pilihan != "6":
                input("\nTekan Enter untuk melanjutkan...")


def demo_buku_telepon():
    """Fungsi untuk mendemonstrasikan buku telepon dengan data contoh"""
    buku = BukuTelepon()
    
    # Tambah data contoh
    buku.kontak = {
        "Andi Pratama": "081234567890",
        "Budi Santoso": "082345678901",
        "Citra Dewi": "083456789012",
        "Dian Kurniawan": "084567890123",
        "Eka Putri": "085678901234"
    }
    
    print("\n📚 BUKU TELEPON - MODE DEMO")
    print("Data contoh telah ditambahkan!")
    buku.menu()


# ============================================================
# PROGRAM UTAMA
# ============================================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("       LATIHAN SOAL STRUKTUR DATA (ARRAY/SET/DICT)")
    print("=" * 60)
    
    while True:
        print("\nPilih soal yang ingin dijalankan:")
        print("1. Soal 1 - Deduplikasi")
        print("2. Soal 2 - Intersection Dua Array")
        print("3. Soal 3 - Anagram Check")
        print("4. Soal 4 - First Recurring Character")
        print("5. Soal 5 - Simulasi Buku Telepon (Demo dengan data contoh)")
        print("6. Soal 5 - Simulasi Buku Telepon (Mulai dari kosong)")
        print("0. Keluar")
        
        pilihan = input("\nMasukkan pilihan (0-6): ").strip()
        
        if pilihan == "1":
            # Soal 1 sudah ditampilkan di atas
            print("\n" + "=" * 60)
            print("SOAL 1: DEDUPLIKASI")
            print("=" * 60)
            data = input("Masukkan list (pisahkan dengan koma, contoh: 1,2,3,2,1): ").strip()
            if data:
                try:
                    # Konversi input ke list
                    lst = [int(x.strip()) if x.strip().isdigit() else x.strip() for x in data.split(',')]
                    print(f"Hasil: {deduplikasi(lst)}")
                except:
                    print("Input tidak valid!")
        
        elif pilihan == "2":
            print("\n" + "=" * 60)
            print("SOAL 2: INTERSECTION DUA ARRAY")
            print("=" * 60)
            arr1_input = input("Array 1 (pisahkan dengan koma): ").strip()
            arr2_input = input("Array 2 (pisahkan dengan koma): ").strip()
            
            if arr1_input and arr2_input:
                try:
                    arr1 = [int(x.strip()) if x.strip().isdigit() else x.strip() for x in arr1_input.split(',')]
                    arr2 = [int(x.strip()) if x.strip().isdigit() else x.strip() for x in arr2_input.split(',')]
                    print(f"Irisan: {intersection(arr1, arr2)}")
                except:
                    print("Input tidak valid!")
        
        elif pilihan == "3":
            print("\n" + "=" * 60)
            print("SOAL 3: ANAGRAM CHECK")
            print("=" * 60)
            str1 = input("String pertama: ").strip()
            str2 = input("String kedua: ").strip()
            
            if str1 and str2:
                if anagram_check(str1, str2):
                    print(f"✓ '{str1}' dan '{str2}' adalah ANAGRAM")
                else:
                    print(f"✗ '{str1}' dan '{str2}' BUKAN anagram")
        
        elif pilihan == "4":
            print("\n" + "=" * 60)
            print("SOAL 4: FIRST RECURRING CHARACTER")
            print("=" * 60)
            text = input("Masukkan string: ").strip()
            
            if text:
                result = first_recurring_char(text)
                if result:
                    print(f"Karakter pertama yang berulang: '{result}'")
                else:
                    print("Tidak ada karakter yang berulang")
        
        elif pilihan == "5":
            demo_buku_telepon()
        
        elif pilihan == "6":
            print("\n" + "=" * 60)
            print("SOAL 5: SIMULASI BUKU TELEPON (MULAI KOSONG)")
            print("=" * 60)
            buku = BukuTelepon()
            buku.menu()
        
        elif pilihan == "0":
            print("\nTerima kasih! Program selesai.")
            break
        
        else:
            print("\nPilihan tidak valid!")
        
        if pilihan not in ["5", "6", "0"]:
            input("\nTekan Enter untuk kembali ke menu...")