package main

func CountPoints(rings string) int {
	ringTable := [10][26]int{}
	for i := 0; i <= len(rings) - 2; i += 2 {
		ringCoord := []byte{ rings[i] - 65, rings[i+1] - 48 }
		if ringTable[ringCoord[1]][ringCoord[0]] == 0 {
			ringTable[ringCoord[1]][ringCoord[0]] = 1
		}
	}
	res := 0
	for _, ring := range ringTable {
		colors := 0
		for _, color := range ring {
			colors += color
		}
		if colors == 3 {
			res++
		}
	}
	return res
}
