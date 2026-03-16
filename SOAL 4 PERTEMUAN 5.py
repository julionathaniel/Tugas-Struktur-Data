def mergeThreeSortedLists(listA, listB, listC):
    """
    Menggabungkan tiga sorted list dalam satu pass menggunakan tiga pointer
    Time Complexity: O(n) dimana n = total elemen
    """
    result = []
    i = j = k = 0
    lenA, lenB, lenC = len(listA), len(listB), len(listC)
    
    while i < lenA and j < lenB and k < lenC:
        if listA[i] <= listB[j] and listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        elif listB[j] <= listA[i] and listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Sisa elemen dari listA dan listB
    while i < lenA and j < lenB:
        if listA[i] <= listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1
    
    # Sisa elemen dari listA dan listC
    while i < lenA and k < lenC:
        if listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Sisa elemen dari listB dan listC
    while j < lenB and k < lenC:
        if listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1
    
    # Sisa elemen dari masing-masing list
    while i < lenA:
        result.append(listA[i])
        i += 1
    while j < lenB:
        result.append(listB[j])
        j += 1
    while k < lenC:
        result.append(listC[k])
        k += 1
    
    return result

# Test case
print("=== Soal 4: Merge Tiga Sorted Lists ===")
listA = [1, 5, 9]
listB = [2, 6, 10]
listC = [3, 4, 7]
result = mergeThreeSortedLists(listA, listB, listC)
print(f"List A: {listA}")
print(f"List B: {listB}")
print(f"List C: {listC}")
print(f"Hasil merge: {result}")
print()