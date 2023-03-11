def findLucky(arr: list[int]) -> int:
    occ = {}
    res = -1
    for num in arr:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1
    for key, val in occ.items():
        if key == val:
            res = max(res, key)
    return res


print(findLucky([2,2,2,3,3]))

