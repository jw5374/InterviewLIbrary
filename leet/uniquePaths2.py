def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    memo = {}
    return findPaths(0, 0, obstacleGrid, memo)


def findPaths(i: int, j: int, grid: list[list[int]], memo: dict[str, int]) -> int:
    if f"{i},{j}" in memo:
        return memo[f"{i},{j}"]
    if i >= len(grid):
        return 0
    if j >= len(grid[0]):
        return 0
    if grid[i][j] == 1:
        return 0
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return 1
    memo[f"{i},{j+1}"] = findPaths(i, j+1, grid, memo)
    memo[f"{i+1},{j}"] = findPaths(i+1, j, grid, memo)
    return memo[f"{i},{j+1}"] + memo[f"{i+1},{j}"]
