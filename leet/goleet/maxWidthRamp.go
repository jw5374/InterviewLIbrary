package main

func MaxWidthRamp(nums []int) int {
    res := 0
    for i, num := range nums {
        if len(nums) - (i + 1) <= res {
            break
        }
        for j := i + 1; j < len(nums); j++ {
            if nums[j] < num {
                continue
            }
            if j - i > res {
                res = j - i
            }
        }
    }
    return res
}
