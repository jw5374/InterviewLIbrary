package main

func RowAndMaximumOnes(mat [][]int) []int {
	res := []int{ 0, 0 }
	for i, row := range mat {
		currMax := rowSum(row)
		if currMax > res[1] {
			res[1] = currMax
			res[0] = i 
		}
	}
	return res
}

func rowSum(row []int) int {
	res := 0
	for _, num := range row {
		res += num
	}
	return res
}
