def bubbleSort(arr):
    """
    Bubble sort dengan early termination
    Returns: (sorted_list, total_comparisons, total_swaps, passes_used)
    """
    n = len(arr)
    sorted_list = arr.copy()
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0
    
    for i in range(n - 1):
        swapped = False
        passes_used += 1
        
        print(f"Pass {passes_used}: {sorted_list}")
        
        for j in range(n - 1 - i):
            total_comparisons += 1
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                total_swaps += 1
                swapped = True
        
        if not swapped:  # Early termination
            break
    
    print(f"Final result: {sorted_list}")
    return sorted_list, total_comparisons, total_swaps, passes_used

# Test cases
print("=== Soal 2: Bubble Sort ===")
print("\nTest 1: [5, 1, 4, 2, 8]")
result1 = bubbleSort([5, 1, 4, 2, 8])
print(f"Total comparisons: {result1[1]}, Total swaps: {result1[2]}, Passes used: {result1[3]}")

print("\nTest 2: [1, 2, 3, 4, 5]")
result2 = bubbleSort([1, 2, 3, 4, 5])
print(f"Total comparisons: {result2[1]}, Total swaps: {result2[2]}, Passes used: {result2[3]}")

print("\nPenjelasan: Jumlah pass berbeda karena array [1,2,3,4,5] sudah terurut, sehingga early termination")
print("terjadi setelah pass pertama (tidak ada swap). Array [5,1,4,2,8] memerlukan 4 pass karena masih")
print("perlu penukaran hingga fully sorted.")
print()