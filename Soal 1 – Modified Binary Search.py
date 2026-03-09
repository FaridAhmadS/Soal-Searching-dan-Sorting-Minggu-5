def first_occurrence(sortedList, target):
    low, high = 0, len(sortedList) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if sortedList[mid] == target:
            result = mid
            high = mid - 1          # cari ke kiri
        elif sortedList[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(sortedList, target):
    low, high = 0, len(sortedList) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if sortedList[mid] == target:
            result = mid
            low = mid + 1            # cari ke kanan
        elif sortedList[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def countOccurrences(sortedList, target):
    first = first_occurrence(sortedList, target)
    if first == -1:
        return 0
    last = last_occurrence(sortedList, target)
    return last - first + 1

# Contoh
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 4))  # Output: 4
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 5))  # Output: 0