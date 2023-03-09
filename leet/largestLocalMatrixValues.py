def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    largest = []
    for i in range(len(grid)-2):
        localLargest = []
        for j in range(len(grid[0])-2):
            localLargest.append(findLocal(i+1, j+1, grid))
        largest.append(localLargest)
    return largest


def findLocal(row: int, col: int, grid: list[list[int]]) -> list[int]:
    neighbors = [
        grid[row][col],
        grid[row-1][col],
        grid[row+1][col],
        grid[row-1][col-1],
        grid[row-1][col+1],
        grid[row+1][col-1],
        grid[row+1][col+1],
        grid[row][col-1],
        grid[row][col+1]
    ]
    return max(neighbors)


print(largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))

