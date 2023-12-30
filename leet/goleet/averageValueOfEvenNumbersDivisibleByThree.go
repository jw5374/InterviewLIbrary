package main

func AverageValue(nums []int) int {
    total, count := 0, 0
    for _, num := range nums {
        if num % 6 == 0 {
            total += num
            count++
        }
    }
    if count == 0 {
        return 0
    }
    return total / count
}
