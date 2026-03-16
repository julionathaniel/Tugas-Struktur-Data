import random
import time

def insertionSort(arr):
    """Insertion sort dengan menghitung operasi"""
    comparisons = 0
    swaps = 0
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(1, n):
        key = sorted_arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and sorted_arr[j] > key:
            comparisons += 1
            sorted_arr[j + 1] = sorted_arr[j]
            swaps += 1
            j -= 1
        sorted_arr[j + 1] = key
    
    return sorted_arr, comparisons, swaps

def selectionSort(arr):
    """Selection sort dengan menghitung operasi"""
    comparisons = 0
    swaps = 0
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        if min_idx != i:
            sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
            swaps += 1
    
    return sorted_arr, comparisons, swaps

def hybridSort(theSeq, threshold=10):
    """
    Hybrid sort: insertion sort untuk sub-array ≤ threshold
    selection sort untuk sub-array > threshold
    """
    comparisons = 0
    swaps = 0
    n = len(theSeq)
    sorted_arr = theSeq.copy()
    
    if n <= threshold:
        # Gunakan insertion sort
        result, comp, swp = insertionSort(sorted_arr)
        comparisons = comp
        swaps = swp
        return result, comparisons, swaps
    else:
        # Gunakan selection sort
        result, comp, swp = selectionSort(sorted_arr)
        comparisons = comp
        swaps = swp
        return result, comparisons, swaps

def testHybridSort():
    """Menguji hybrid sort dengan berbagai ukuran array"""
    sizes = [50, 100, 500]
    threshold = 10
    
    print("\n=== Soal 3: Hybrid Sort ===")
    print("Perbandingan Jumlah Operasi (comparisons + swaps)")
    print("-" * 70)
    print(f"{'Ukuran':<10} {'Hybrid Sort':<15} {'Insertion Sort':<18} {'Selection Sort':<15}")
    print("-" * 70)
    
    for size in sizes:
        # Generate random array
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        # Hybrid sort
        _, comp_hybrid, swap_hybrid = hybridSort(arr, threshold)
        total_hybrid = comp_hybrid + swap_hybrid
        
        # Insertion sort
        _, comp_insert, swap_insert = insertionSort(arr)
        total_insert = comp_insert + swap_insert
        
        # Selection sort
        _, comp_select, swap_select = selectionSort(arr)
        total_select = comp_select + swap_select
        
        print(f"{size:<10} {total_hybrid:<15} {total_insert:<18} {total_select:<15}")

testHybridSort()
print()