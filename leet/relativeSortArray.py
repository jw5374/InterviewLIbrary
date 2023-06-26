def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    keyHash = {}
    numGroups = {}
    numGroups[-1] = []
    for num in arr2:
        keyHash[num] = True
    for num in arr1:
        if num not in keyHash:
            numGroups[-1].append(num)
            continue
        if num in numGroups:
            numGroups[num].append(num)
        else:
            numGroups[num] = [num]
    numGroups[-1].sort()
    [i, j] = [0, 0]
    while j < len(arr2):
        for num in numGroups[arr2[j]]:
            arr1[i] = num
            i += 1
        j += 1
    for num in numGroups[-1]:
        arr1[i] = num
        i += 1
    return arr1
