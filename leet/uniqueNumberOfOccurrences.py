def uniqueOccurrences(arr: list[int]) -> bool:
    occ = {}
    setOcc = set()
    for num in arr:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1
    for val in occ.values():
        setOcc.add(val)
    return len(occ) == len(setOcc)


print(uniqueOccurrences([1,2,2,1,1,3]))

