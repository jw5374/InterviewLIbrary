package main

func IsGood(nums []int) bool {
	sortedNums := make([]int, len(nums) - 1)
	for _, num := range nums {
		if num - 1 > len(sortedNums) - 1 {
			return false
		}
		sortedNums[num - 1]++
	}
	if sortedNums[len(sortedNums) - 1] != 2 {
		return false
	}
	for i := 0; i < len(sortedNums) - 1; i++ {
		if sortedNums[i] != 1 {
			return false
		}
	}
	return true
}
