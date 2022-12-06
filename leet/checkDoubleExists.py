def checkIfExist(arr: list[int]) -> bool:
	hash = {}
	for i, num in enumerate(arr):
		if num not in hash:
			hash[num] = i
	for i, num in enumerate(arr):
		if (num * 2) in hash and hash[num*2] != i:
			return True
	return False

print(checkIfExist([0,0]))
