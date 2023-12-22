package main

import "sort"

func SmallerNumbersThanCurrent(nums []int) []int {
	res := make([]int, len(nums))
	numSorted := make([]int, len(nums))
	copy(nums, numSorted)
	sort.Ints(numSorted)
	indexMap := make(map[int]int)
	for i, num := range numSorted {
		if _, exists := indexMap[num]; exists {
			continue
		}
		indexMap[num] = i
	}
	for i, num := range nums {
		res[i] = indexMap[num]
	}
	return res
}
