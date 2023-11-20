package main

func MinNumber(nums1 []int, nums2 []int) int {
	common := findSmallestCommon(nums1, nums2)
	if common != 10 {
		return common
	}
	min1 := findMin(nums1)
	min2 := findMin(nums2)
	if min1 <= min2 {
		return (min1 * 10) + min2
	}
	return (min2 * 10) + min1
}

func findMin(arr []int) int {
	res := 10
	for _, num := range arr {
		if num < res {
			res = num
		}
	}
	return res
}

func findSmallestCommon(arr1 []int, arr2 []int) int {
	firstExists := make(map[int]struct{})
	res := 10
	for _, num := range arr1 {
		firstExists[num] = struct{}{}
	}
	for _, num := range arr2 {
		if _, exists := firstExists[num]; exists && num < res {
			res = num
		}
	}
	return res
}
