package main

func CountEven(num int) int {
	res := 0
	for i := 1; i < num + 1; i++ {
		if digitSum(i) % 2 == 0 {
			res++
		}
	}
	return res
}

func digitSum(num int) int {
	res := 0
	numCopy := num
	for numCopy > 0 {
		res += numCopy % 10
		numCopy /= 10
	}
	return res
}
