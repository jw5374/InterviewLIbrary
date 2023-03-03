def diagonalSum(mat: list[list[int]]) -> int:
    sum = 0
    added = {}
    [i, j] = [0, 0]
    while i < len(mat) and j < len(mat[0]):
        coord = f'{i},{j}'
        added[coord] = True
        sum += mat[i][j]
        i += 1
        j += 1
    i = 0
    j = len(mat[0]) - 1
    while i < len(mat) and j >= 0:
        coord = f'{i},{j}'
        if coord not in added:
            sum += mat[i][j]
        i += 1
        j -= 1
    return sum


print(diagonalSum([[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))

