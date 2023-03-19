def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    res = []
    if m * n != len(original):
        return res
    i = 0
    for j in range(m):
        row = []
        for k in range(n):
            row.append(original[i])
            i += 1
        res.append(row)
    return res


print(construct2DArray([1,2,3], 1, 3))

