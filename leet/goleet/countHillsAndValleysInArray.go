package main

func CountHillValley(nums []int) int {
    var res int = 0
    var i int = 1
    for i < len(nums) - 1 {
        var left, right int = i, i
        for right < len(nums) - 1 && nums[right+1] == nums[left] {
            right++
        }
        if right == len(nums) - 1 {
            break
        }
        var isHill bool = nums[left-1] < nums[i] && nums[right+1] < nums[i]
        var isValley bool = nums[left-1] > nums[i] && nums[right+1] > nums[i]
        if isHill || isValley {
            res++
        }
        i = right + 1
    }
    return res
}

