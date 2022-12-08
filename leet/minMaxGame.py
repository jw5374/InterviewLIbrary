def minMaxGame(nums: list[int]) -> int:
	halfList = [num for num in nums]
	currMaxLen = len(nums) // 2
	while len(halfList) > 1:
		local = []
		for i in range(currMaxLen):
			if i % 2 == 0:
				local.append(min(halfList[i*2], halfList[i*2 + 1]))
			else:
				local.append(max(halfList[i*2], halfList[i*2 + 1]))
		currMaxLen = currMaxLen // 2
		halfList = local
	return halfList[0]

print(minMaxGame([1,3,5,2,4,8,2,2]))
