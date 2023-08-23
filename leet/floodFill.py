def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    starting = image[sr][sc]
    visited = set()
    nodeStack = [[sr, sc]]
    while len(nodeStack) > 0:
        curr = nodeStack.pop()
        if f"{curr[0]},{curr[1]}" in visited:
            continue
        visited.add(f"{curr[0]},{curr[1]}")
        image[curr[0]][curr[1]] = color
        nodeStack += findNeighbors(image, curr[0], curr[1], color, starting)
    return image


def findNeighbors(image: list[list[int]], row: int, col: int, color: int, startingColor: int) -> list[list[int]]:
    potential = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    return [x for x in potential
            if (x[0] < len(image) and x[0] > -1) and (x[1] < len(image[0]) and x[1] > -1)
            and (image[x[0]][x[1]] != color and image[x[0]][x[1]] == startingColor)
            ]
