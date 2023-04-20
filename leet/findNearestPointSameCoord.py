def nearestvalidPoint(x: int, y: int, points: list[list[int]]) -> int:
    smallestInd = len(points)
    smallestDist = x*y*100000
    for i, point in enumerate(points):
        if point[0] == x and point[1] == y:
            return i
        if point[0] == x or point[1] == y:
            currDist = calcManhattanDistance(point, [x, y])
            if currDist == smallestDist:
                smallestInd = min(i, smallestInd)
            elif currDist < smallestDist:
                smallestInd = i
                smallestDist = currDist
    return smallestInd if smallestInd != len(points) else -1


def calcManhattanDistance(point1: list[int], point2: list[int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


print(nearestvalidPoint(3, 4, [[1,2]]))

