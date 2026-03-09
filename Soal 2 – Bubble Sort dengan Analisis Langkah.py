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

# Uji dengan dua input
arr1 = [5, 1, 4, 2, 8]
arr2 = [1, 2, 3, 4, 5]

print("Input:", arr1)
res1 = bubbleSortWithAnalysis(arr1)
print(f"Sorted: {res1[0]}, Comparisons: {res1[1]}, Swaps: {res1[2]}, Passes: {res1[3]}\n")

print("Input:", arr2)
res2 = bubbleSortWithAnalysis(arr2)
print(f"Sorted: {res2[0]}, Comparisons: {res2[1]}, Swaps: {res2[2]}, Passes: {res2[3]}")