package main

func FinalValueAfterOperations(operations []string) int {
	res := 0
	for _, op := range operations {
		if isDecrement(op) {
			res--
			continue
		}
		res++
	}
	return res
}

func isDecrement(op string) bool {
	return op[0] == '-' || op[2] == '-'
}
