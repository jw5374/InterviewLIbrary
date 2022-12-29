def checkStraightLine(coordinates: list[list[int]]) -> bool:
	currSlope = checkSlope(coordinates[0], coordinates[1])
	for i in range(1, len(coordinates) - 1):
		nextSlope = checkSlope(coordinates[i], coordinates[i+1]) if coordinates[i][0] < coordinates[i+1][0] else checkSlope(coordinates[i+1], coordinates[i])
		if currSlope != nextSlope:
			return False
	return True


def checkSlope(start: list[int], dest: list[int]) -> int:
	if dest[0] == start[0]:
		return None
	return round((dest[1] - start[1]) / (dest[0] - start[0]), 2)


print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
