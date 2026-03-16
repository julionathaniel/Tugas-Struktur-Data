import random
import time

def countInversionsNaive(arr):
    """Brute force O(n²) untuk menghitung inversions"""
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def mergeAndCount(arr, temp_arr, left, mid, right):
    """Menggabungkan dua sub-array dan menghitung inversions"""
    i = left    # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Semua elemen yang tersisa di kiri lebih besar dari arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # Copy back to original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def mergeSortAndCount(arr, temp_arr, left, right):
    """Merge sort yang menghitung inversions"""
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += mergeSortAndCount(arr, temp_arr, left, mid)
        inv_count += mergeSortAndCount(arr, temp_arr, mid + 1, right)
        inv_count += mergeAndCount(arr, temp_arr, left, mid, right)
    return inv_count

def countInversionsSmart(arr):
    """Menghitung inversions menggunakan modified merge sort O(n log n)"""
    arr_copy = arr.copy()
    temp_arr = [0] * len(arr_copy)
    return mergeSortAndCount(arr_copy, temp_arr, 0, len(arr_copy) - 1)

def testInversions():
    """Menguji kedua fungsi dan membandingkan waktu eksekusi"""
    sizes = [1000, 5000, 10000]
    
    print("=== Soal 5: Inversions Counter ===")
    print("Perbandingan Waktu Eksekusi")
    print("-" * 80)
    print(f"{'Ukuran':<10} {'Naive O(n²)':<20} {'Smart O(n log n)':<20} {'Hasil Sama?'}")
    print("-" * 80)
    
    for size in sizes:
        # Generate random array
        arr = [random.randint(1, 1000) for _ in range(size)]
        arr_small = arr[:100]  # Untuk naive method dengan ukuran kecil karena O(n²) lambat
        
        # Naive method (hanya untuk 100 elemen pertama)
        start = time.time()
        naive_count = countInversionsNaive(arr_small)
        naive_time = time.time() - start
        
        # Smart method
        start = time.time()
        smart_count = countInversionsSmart(arr)
        smart_time = time.time() - start
        
        # Test untuk array kecil apakah hasilnya sama
        smart_count_small = countInversionsSmart(arr_small)
        hasil_sama = "✓" if naive_count == smart_count_small else "✗"
        
        print(f"{size:<10} {naive_time:.6f} s{' ':<5} {smart_time:.6f} s{' ':<5} {hasil_sama}")
    
    print("\nPenjelasan: Merge sort lebih cepat karena:")
    print("1. Algoritma O(n log n) vs O(n²) - perbedaan dramatis untuk n besar")
    print("2. Merge sort membagi masalah menjadi sub-masalah yang lebih kecil")
    print("3. Menghitung inversions sambil mengurutkan dalam satu pass")

# Run the test
testInversions()
print()