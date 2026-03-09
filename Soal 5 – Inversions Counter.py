import random
import time

def countInversionsNaive(arr):
    n = len(arr)
    inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])
    merged, inv_split = merge_count(left, right)
    return merged, inv_left + inv_right + inv_split

def merge_count(left, right):
    i = j = 0
    inv = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i   # semua sisa di left > right[j]
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

def countInversionsSmart(arr):
    _, inv = merge_sort_count(arr)
    return inv

# Pengujian
sizes = [1000, 5000, 10000]
print("Ukuran\tNaive (detik)\tSmart (detik)\tHasil sama?")
for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]

    start = time.time()
    inv_naive = countInversionsNaive(arr)
    t_naive = time.time() - start

    start = time.time()
    inv_smart = countInversionsSmart(arr)
    t_smart = time.time() - start

    sama = (inv_naive == inv_smart)
    print(f"{size}\t{t_naive:.4f}\t\t{t_smart:.4f}\t\t{sama}")