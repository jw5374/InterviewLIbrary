def isPathCrossing(path: str) -> bool:
	currentPos = [0,0]
	visited = {
		"0,0": True
	}
	for direction in path:
		if direction == "N":
			currentPos[1] += 1
		elif direction == "E":
			currentPos[0] += 1
		elif direction == "S":
			currentPos[1] -= 1
		elif direction == "W":
			currentPos[0] -= 1
		if f"{currentPos[0]},{currentPos[1]}" in visited:
			return True
		else:
			visited[f"{currentPos[0]},{currentPos[1]}"] = True
	return False

print(isPathCrossing("NESW"))
