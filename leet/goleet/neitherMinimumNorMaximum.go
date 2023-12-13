package main

func findNonMinOrMax(nums []int) int {
    min, max := nums[0], nums[0]
    for _, num := range nums {
        if num < min {
            min = num
            continue
        }
        if num > max {
            max = num
            continue
        }
    }
    for _, num := range nums {
        if num != min && num != max {
            return num
        }
    }
    return -1
}
