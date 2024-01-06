# area = 25, sanity check
# area = 1002001, question number
def spiralCorners(squareArea: int) -> list[int]:
	cornerNums = [1]
	# iterate the square
	i = 3
	numLoop = 1
	numSkip = 2
	while i <= squareArea:
		if numLoop < 4:
			numLoop += 1
		else:
			numLoop = 1
			numSkip += 2
		cornerNums.append(i)
		i += numSkip
	return cornerNums

# yes i can just directly add within loop for more efficiency
print(sum(spiralCorners(1002001)))
