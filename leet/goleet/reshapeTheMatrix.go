package main

func MatrixReshape(mat [][]int, r int, c int) [][]int {
	if len(mat) * len(mat[0]) != r * c {
		return mat
	}
	res := [][]int{}
	for i := 0; i < r; i++ {
		res = append(res, make([]int, c))
	}
	m, n := 0, 0
	for _, row := range mat {
		for _, num := range row {
			if m >= r {
				return res
			}
			if n >= c {
				n = 0
				m++
			}
			res[m][n] = num
			n++
		}
	}
	return res
}
