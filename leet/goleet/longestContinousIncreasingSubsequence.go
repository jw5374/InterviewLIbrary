package main

func FindLengthOfLCIS(nums []int) int {
	if len(nums) == 1 {
		return 1
	}
	i, j := 0, 0
	res := 0
	for i < len(nums) - 1 {
		j = i + 1
		for j < len(nums) && nums[j] > nums[j-1] {
			j++
		}
		if j - i > res {
			res = j - i
		}
		i = j
	}
	return res
}
