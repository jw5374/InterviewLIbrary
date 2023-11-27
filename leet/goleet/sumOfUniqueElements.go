package main

func SumOfUnique(nums []int) int {
	res := 0
	visited := make(map[int]bool)
	for _, num := range nums {
		if val, exists := visited[num]; exists {
			if val {
				res -= num
				visited[num] = false
			}
		} else {
			visited[num] = true
			res += num
		}
	}
	return res
}
