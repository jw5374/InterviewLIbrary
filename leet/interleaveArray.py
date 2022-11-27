# going for naive n^2 again
def shuffle(nums: list[int], n: int) -> list[int]:
	[left, right] = [0, len(nums)-1]
	while(left < n-1 and right > n):
		[i, j] = [n-1, n]
		nums[i], nums[j] = nums[j], nums[i]
		i -= 1
		j += 1
		while(i > left and j < right):
			nums[i+1], nums[i] = nums[i], nums[i+1]
			nums[j], nums[j-1] = nums[j-1], nums[j]
			i -= 1
			j += 1
		left += 2
		right -= 2
	return nums

print(shuffle([7,5,9,7,5,8,10,4,3,3,2,5,9,10], 7))
