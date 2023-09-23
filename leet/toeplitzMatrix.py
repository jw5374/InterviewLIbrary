def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    for i in range(len(matrix[0]) - 1):
        if not checkDiag(0, i, matrix):
            return False
    for i in range(1, len(matrix) - 1):
        if not checkDiag(i, 0, matrix):
            return False
    return True


def checkDiag(i: int, j: int, mat: list[list[int]]) -> bool:
    [ii, jj] = [i, j]
    tar = mat[i][j]
    while ii < len(mat) and jj < len(mat[0]):
        print(tar, ii, jj, mat[ii][jj])
        if mat[ii][jj] != tar:
            return False
        ii += 1
        jj += 1
    return True
