package main

func MaxDepth(s string) int {
	res := 0
	currMax := 0
	for _, c := range s {
		if c == ')' {
			if currMax > res {
				res = currMax
			}
			currMax--
			continue
		}
		if c == '(' {
			currMax++
		}
	}
	return res
}
