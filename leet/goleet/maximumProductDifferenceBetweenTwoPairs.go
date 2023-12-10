package main

import "sort"

func MaxProductDifference(nums []int) int {
    numLen := len(nums)
    sort.Slice(nums, func(a, b int) bool {
        return nums[a] < nums[b]
    })
    return (nums[numLen - 1] * nums[numLen - 2]) - (nums[0] * nums[1])
}
