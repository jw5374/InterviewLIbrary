def fibThousandDigit():
	index = 0
	left, right = 0, 1
	while len(str(left)) < 1000:
		temp = left
		left = left + right
		right = temp
		index += 1
	return index

print(fibThousandDigit())
