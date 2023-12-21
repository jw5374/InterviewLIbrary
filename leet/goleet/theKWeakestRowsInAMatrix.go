package main

func KWeakestRows(mat [][]int, k int) []int {
	weakestTable := make([][]int, len(mat[0]) + 1)
	res := []int{}
	for i, row := range mat {
		strength := 0
		for _, soldier := range row {
			strength += soldier
		}
		weakestTable[strength] = append(weakestTable[strength], i)
	}
	i := 0
	for i < len(weakestTable) && k > 0 {
		if len(weakestTable[i]) == 0 {
			i++
			continue
		}
		res = append(res, weakestTable[i][0])
		weakestTable[i] = weakestTable[i][1:]
		k--
	}
	return res
}
