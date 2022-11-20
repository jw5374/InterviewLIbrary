def maxAscendingSum(nums: list[int]):
	subSum = nums[0]
	glob = nums[0]
	if len(nums) == 1:
		return glob
	for i in range(1, len(nums)):
		subSum = (max(nums[i], subSum + nums[i]), nums[i])[nums[i-1] >= nums[i]] 
		if(glob < subSum):
			glob = subSum
	return glob

print(maxAscendingSum([3,6,10,1,8,9,9,8,9]))
