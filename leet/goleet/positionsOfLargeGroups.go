package main

func LargeGroupPositions(s string) [][]int {
	res := [][]int{}
	i, j := 0, 0
	for i < len(s) {
		j = i
		start := i
		groupSize := 0
		for j < len(s) {
			if s[i] != s[j] {
				break
			}
			j++
		}
		groupSize = start - j
		if groupSize > 2 {
			res = append(res, []int{ start, j - 1 })
		}
		i = j
	}
	return res
}
