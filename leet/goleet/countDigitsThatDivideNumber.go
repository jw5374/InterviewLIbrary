package main

func countDigits(num int) int {
	numCopy := num
	res := 0
	for numCopy > 0 {
		digit := numCopy % 10
		numCopy /= 10
		if num % digit != 0 {
			continue
		}
		res++
	}
	return res
}
