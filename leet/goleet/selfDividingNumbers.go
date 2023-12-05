package main

func SelfDividingNumbers(left int, right int) []int {
	res := []int{}
	for i := left; i < right + 1; i++ {
		if !isSelfDividing(i) {
			continue
		}
		res = append(res, i)
	}
	return res
}

func isSelfDividing(num int) bool {
	numCopy := num
	for numCopy > 0 {
		digit := numCopy % 10
		if digit == 0 {
			return false
		}
		if num % digit != 0 {
			return false
		}
		numCopy /= 10
	}
	return true
}
