package main

func NumRookCaptures(board [][]byte) int {
	for j := 0; j < 8; j++ {
		for i := 0; i < 8; i++ {
			if board[i][j] == 82 {
				board[i][j] = 46
				return findCaptures(board, i, j)
			}
		}
	}
	return 0
}

func findCaptures(board [][]byte, i, j int) int {
	left, right, up, down := j, j, i, i
	for left > 0 && board[i][left] == 46 {
		left--
	}
	for right < 7 && board[i][right] == 46 {
		right++
	}
	for up > 0 && board[up][j] == 46 {
		up--
	}
	for down < 7 && board[down][j] == 46 {
		down++
	}
	res := 0
	for _, el := range [4]byte{ board[i][left], board[i][right], board[up][j], board[down][j] } {
		if el == 112 {
			res++
		}
	}
	return res
}
