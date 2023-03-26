def deleteGreatestValue(grid: list[list[int]]) -> int:
    sum = 0
    for row in grid:
        row.sort()
    for i in range(len(grid[0])):
        sum += max([row[i] for row in grid])
    return sum
