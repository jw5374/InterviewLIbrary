from checkStraightLine import checkStraightLine


def isBoomerang(points: list[list[int]]) -> bool:
    # straightline checkslope function needs to have increased precision for some test cases (to 5 decimal places)
    if checkStraightLine(points):
        return False
    pointsHash = {}
    for point in points:
        pointStr = f'{point[0]},{point[1]}'
        print(pointStr)
        if pointStr in pointsHash:
            return False
        pointsHash[pointStr] = True
    return True


print(isBoomerang([[52,68],[23,63],[46,67]]))  # will return false when should be true

