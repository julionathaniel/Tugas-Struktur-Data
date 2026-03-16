def findLeftBoundary(sortedList, target):
    """Binary search untuk menemukan kemunculan pertama target"""
    left, right = 0, len(sortedList) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if sortedList[mid] == target:
            result = mid
            right = mid - 1  # Cari ke kiri untuk kemunculan pertama
        elif sortedList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def findRightBoundary(sortedList, target):
    """Binary search untuk menemukan kemunculan terakhir target"""
    left, right = 0, len(sortedList) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if sortedList[mid] == target:
            result = mid
            left = mid + 1  # Cari ke kanan untuk kemunculan terakhir
        elif sortedList[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def countOccurrences(sortedList, target):
    """
    Menghitung berapa kali target muncul dalam sorted list
    Time Complexity: O(log n)
    """
    left = findLeftBoundary(sortedList, target)
    
    if left == -1:  # Target tidak ditemukan
        return 0
    
    right = findRightBoundary(sortedList, target)
    return right - left + 1

# Test cases
print("=== Soal 1: Modified Binary Search ===")
print(countOccurrences([1, 2, 4, 4, 4, 7, 9, 12], 4))  # Output: 3
print(countOccurrences([1, 2, 4, 4, 4, 7, 9, 12], 5))  # Output: 0
print()