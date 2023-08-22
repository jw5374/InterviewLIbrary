def transpose(matrix: list[list[int]]) -> list[list[int]]:
    res = []
    for j in range(len(matrix[0])):
        newRow = []
        for i in range(len(matrix)):
            newRow.append(matrix[i][j])
        res.append(newRow)
    return res
