package main

func SeparateDigits(nums []int) []int {
	res := []int{}
	for _, num := range nums {
		res = append(res, splitDigits(num)...)
	}
	return res
}

func splitDigits(num int) []int {
	res := [6]int{}
	numCopy := num
	currDigit := 5
	for numCopy > 0 {
		res[currDigit] = numCopy % 10
		numCopy /= 10
		currDigit--
	}
	return res[currDigit+1:]
}
