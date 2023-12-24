package main

func CreateTargetArray(nums []int, index []int) []int {
	res := []int{ nums[0] }
	for i := 1; i < len(nums); i++ {
		if index[i] == len(res) {
			res = append(res, nums[i])
			continue
		}
		res = append(res[:index[i]+1], res[index[i]:]...)
		res[index[i]] = nums[i]
	}
	return res
}
