def mergeThreeSortedLists(listA, listB, listC):
    i = j = k = 0
    lenA, lenB, lenC = len(listA), len(listB), len(listC)
    result = []

    # Gabung selama ketiga list masih ada elemen
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

    # Salin sisa list yang masih ada
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
# Output: [1, 2, 3, 4, 5, 6, 7, 9, 10]