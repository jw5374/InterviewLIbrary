def findFinalValue(nums: list[int], original: int) -> int:
	hash = {}
	for num in nums:
		if num not in hash:
			hash[num] = True
	while original in hash:
		original *= 2
	return original

print(findFinalValue([2,7,9], 4))
