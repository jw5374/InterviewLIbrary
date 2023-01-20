def oddCells(m: int, n: int, indices: list[list[int]]) -> int:
    rows = [0] * m
    cols = [0] * n
    oddRows = 0
    oddCols = 0
    evenRows = 0
    evenCols = 0
    for index in indices:
        rows[index[0]] += 1
        cols[index[1]] += 1
    for row in rows:
        if row % 2 != 0:
            oddRows += 1
        else:
            evenRows += 1
    for col in cols:
        if col % 2 != 0:
            oddCols += 1
        else:
            evenCols += 1
    return oddRows * evenCols + oddCols * evenRows

print(oddCells(2, 3, [[0,1],[1,1]]))

