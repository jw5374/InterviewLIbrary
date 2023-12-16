package main

import "strconv"

func FindColumnWidth(grid [][]int) []int {
	res := make([]int, len(grid[0]))
	for _, row := range grid {
		for j, num := range row {
			numLen := len(strconv.Itoa(num))
			if res[j] < numLen {
				res[j] = numLen
			}
		}
	}
	return res
}
