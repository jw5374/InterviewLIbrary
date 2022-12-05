def dominantIndex(nums: list[int]) -> int:
	max = -1
	maxInd = 0
	for i in range(len(nums)):
		num = nums[i]
		if num > max:
			max = num
			maxInd = i
	for num in nums:
		greater = num * 2 > max and num != max
		if greater:
			return -1
	return maxInd

print(dominantIndex([1,2,3,4]))
