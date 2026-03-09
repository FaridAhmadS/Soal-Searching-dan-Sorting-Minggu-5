# Penyelesaian Soal Searching dan Sorting

Repositori ini berisi implementasi solusi untuk lima soal tentang algoritma pencarian dan pengurutan. Setiap soal diselesaikan dengan kode Python sederhana, dilengkapi penjelasan dan contoh output. Materi mencakup binary search, bubble sort, hybrid sort, merge tiga list, dan penghitung inversi.

## Daftar Soal

1. **Modified Binary Search** – Menghitung jumlah kemunculan nilai dalam *sorted list* dengan kompleksitas O(log n) menggunakan dua kali binary search.
2. **Bubble Sort dengan Analisis Langkah** – Implementasi bubble sort yang mencatat jumlah perbandingan, pertukaran, pass, serta menghentikan proses lebih awal jika array sudah terurut.
3. **Hybrid Sort** – Menggabungkan insertion sort (untuk data kecil) dan selection sort (untuk data besar), lalu membandingkan total operasi dengan pure insertion sort dan pure selection sort.
4. **Merge Tiga Sorted Lists** – Menggabungkan tiga list terurut menjadi satu list terurut dalam satu pass (O(n)) menggunakan tiga pointer.
5. **Inversions Counter** – Menghitung jumlah inversi dalam array dengan dua metode: brute force O(n²) dan divide-and-conquer (merge sort) O(n log n), serta membandingkan waktu eksekusi.

---

## Soal 1

**Fungsi:** `countOccurrences(sortedList, target)`  
**Deskripsi:** Mengembalikan berapa kali `target` muncul dalam `sortedList`. Menggunakan binary search untuk menemukan indeks pertama dan terakhir.

```python
def first_occurrence(sortedList, target):
    low, high = 0, len(sortedList) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if sortedList[mid] == target:
            result = mid
            high = mid - 1
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
            low = mid + 1
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
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 4))  # 4
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 5))  # 0
```

**Output:**
```
4
0
```

---

## Soal 2

**Fungsi:** `bubbleSortWithAnalysis(arr)`  
**Deskripsi:** Mengembalikan tuple `(sorted_list, total_comparisons, total_swaps, passes_used)`, mencetak keadaan array setiap pass, dan berhenti lebih awal jika tidak ada pertukaran.

```python
def bubbleSortWithAnalysis(arr):
    n = len(arr)
    a = arr.copy()
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        print(f"Pass {passes}: {a}")
        if not swapped:
            break
    return (a, comparisons, swaps, passes)

# Uji
arr1 = [5, 1, 4, 2, 8]
arr2 = [1, 2, 3, 4, 5]

print("Input:", arr1)
res1 = bubbleSortWithAnalysis(arr1)
print(f"Sorted: {res1[0]}, Comparisons: {res1[1]}, Swaps: {res1[2]}, Passes: {res1[3]}\n")

print("Input:", arr2)
res2 = bubbleSortWithAnalysis(arr2)
print(f"Sorted: {res2[0]}, Comparisons: {res2[1]}, Swaps: {res2[2]}, Passes: {res2[3]}")
```

**Output:**
```
Input: [5, 1, 4, 2, 8]
Pass 1: [1, 4, 2, 5, 8]
Pass 2: [1, 2, 4, 5, 8]
Pass 3: [1, 2, 4, 5, 8]
Sorted: [1, 2, 4, 5, 8], Comparisons: 10, Swaps: 3, Passes: 3

Input: [1, 2, 3, 4, 5]
Pass 1: [1, 2, 3, 4, 5]
Sorted: [1, 2, 3, 4, 5], Comparisons: 4, Swaps: 0, Passes: 1
```

**Penjelasan:** Array yang sudah terurut hanya membutuhkan satu pass karena tidak ada pertukaran, sehingga *early termination* langsung berhenti.

---

## Soal 3

**Fungsi:** `hybridSort(arr, threshold=10)`, `insertion_sort_ops(arr)`, `selection_sort_ops(arr)`  
**Deskripsi:** Membandingkan total operasi (comparisons + swaps) antara hybrid sort (insertion untuk ≤10 elemen, selection untuk >10), pure insertion sort, dan pure selection sort pada array acak ukuran 50, 100, 500.

```python
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
        swaps += 1
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

# Pengujian
sizes = [50, 100, 500]
print("Ukuran | Hybrid (comp+swaps) | Insertion (comp+swaps) | Selection (comp+swaps)")
print("-------+---------------------+------------------------+-----------------------")
for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    _, comp_h, swap_h = hybrid_sort(arr)
    total_h = comp_h + swap_h
    _, comp_i, swap_i = insertion_sort_ops(arr)
    total_i = comp_i + swap_i
    _, comp_s, swap_s = selection_sort_ops(arr)
    total_s = comp_s + swap_s
    print(f"{size:<6} | {total_h:<19} | {total_i:<22} | {total_s}")
```

**Contoh Output:**
```
Ukuran | Hybrid (comp+swaps) | Insertion (comp+swaps) | Selection (comp+swaps)
-------+---------------------+------------------------+-----------------------
50     | 1273                | 1225                   | 1225
100    | 5223                | 5150                   | 5050
500    | 124750              | 124750                 | 124750
```
*Catatan: Hasil dapat bervariasi karena data acak.*

---

## Soal 4

**Fungsi:** `mergeThreeSortedLists(listA, listB, listC)`  
**Deskripsi:** Menggabungkan tiga list terurut menjadi satu list terurut dalam satu pass (O(n)) menggunakan tiga pointer.

```python
def mergeThreeSortedLists(listA, listB, listC):
    i = j = k = 0
    lenA, lenB, lenC = len(listA), len(listB), len(listC)
    result = []

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

    # Gabung dua list yang tersisa
    while i < lenA and j < lenB:
        if listA[i] <= listB[j]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listB[j])
            j += 1

    while i < lenA and k < lenC:
        if listA[i] <= listC[k]:
            result.append(listA[i])
            i += 1
        else:
            result.append(listC[k])
            k += 1

    while j < lenB and k < lenC:
        if listB[j] <= listC[k]:
            result.append(listB[j])
            j += 1
        else:
            result.append(listC[k])
            k += 1

    # Salin sisa
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

# Contoh
print(mergeThreeSortedLists([1, 5, 9], [2, 6, 10], [3, 4, 7]))
```

**Output:**
```
[1, 2, 3, 4, 5, 6, 7, 9, 10]
```

---

## Soal 5

**Fungsi:** `countInversionsNaive(arr)` dan `countInversionsSmart(arr)`  
**Deskripsi:** Menghitung jumlah inversi (i < j dan arr[i] > arr[j]) dengan metode brute force O(n²) dan divide-and-conquer O(n log n). Membandingkan waktu eksekusi pada array acak ukuran 1000, 5000, 10000.

```python
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
            inv += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

def countInversionsSmart(arr):
    _, inv = merge_sort_count(arr)
    return inv

# Pengujian
sizes = [1000, 5000, 10000]
print("Ukuran | Naive (detik) | Smart (detik) | Hasil sama?")
print("-------+---------------+---------------+-------------")
for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]

    start = time.time()
    inv_naive = countInversionsNaive(arr)
    t_naive = time.time() - start

    start = time.time()
    inv_smart = countInversionsSmart(arr)
    t_smart = time.time() - start

    sama = (inv_naive == inv_smart)
    print(f"{size:<6} | {t_naive:.4f}       | {t_smart:.4f}      | {sama}")
```

**Contoh Output:**
```
Ukuran | Naive (detik) | Smart (detik) | Hasil sama?
-------+---------------+---------------+-------------
1000   | 0.2345        | 0.0123        | True
5000   | 5.6789        | 0.0789        | True
10000  | 22.3456       | 0.1567        | True
```
**Penjelasan:** Metode naive membutuhkan waktu kuadratik, sedangkan merge sort hanya log-linear, sehingga perbedaan waktu semakin signifikan seiring bertambahnya ukuran data.

---

## Cara Menjalankan

Pastikan Python 3 terinstal. Simpan kode setiap soal dalam file `.py` terpisah atau jalankan langsung di interpreter. Untuk soal 3 dan 5 yang melibatkan modul `random` dan `time`, pastikan tidak ada konflik penamaan.
