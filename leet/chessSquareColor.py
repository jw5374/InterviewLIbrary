def squareIsWhite(coordinates: str) -> bool:
	fileEven = ord(coordinates[0]) % 2 == 0
	rankEven = int(coordinates[1]) % 2 == 0
	if (fileEven and rankEven) or (not fileEven and not rankEven):
		return False
	return True

print(squareIsWhite("c3"))
