import random

def insertion_sort_ops(arr):
    comparisons = 0
    swaps = 0
    a = arr.copy()
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        swaps += 1          # penempatan key
    return a, comparisons, swaps

def selection_sort_ops(arr):
    comparisons = 0
    swaps = 0
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps

def hybrid_sort(arr, threshold=10):
    comparisons = 0
    swaps = 0
    a = arr.copy()
    n = len(a)
    if n <= threshold:
        # insertion sort
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while j >= 0:
                comparisons += 1
                if a[j] > key:
                    a[j + 1] = a[j]
                    swaps += 1
                    j -= 1
                else:
                    break
            a[j + 1] = key
            swaps += 1
    else:
        # selection sort
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                comparisons += 1
                if a[j] < a[min_idx]:
                    min_idx = j
            if min_idx != i:
                a[i], a[min_idx] = a[min_idx], a[i]
                swaps += 1
    return a, comparisons, swaps

# Pengujian perbandingan
sizes = [50, 100, 500]
print("Ukuran\tHybrid (comp+swaps)\tInsertion (comp+swaps)\tSelection (comp+swaps)")
for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    _, comp_h, swap_h = hybrid_sort(arr)
    total_h = comp_h + swap_h
    _, comp_i, swap_i = insertion_sort_ops(arr)
    total_i = comp_i + swap_i
    _, comp_s, swap_s = selection_sort_ops(arr)
    total_s = comp_s + swap_s
    print(f"{size}\t{total_h}\t\t\t{total_i}\t\t\t{total_s}")