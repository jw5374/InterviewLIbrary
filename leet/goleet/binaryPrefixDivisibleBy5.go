package main

func prefixDivBy5(nums []int) []bool {
	res := make([]bool, len(nums))
	currBinary := 0
	for i, num := range nums {
		currBinary = ((currBinary % 5) * 2) + num
		res[i] = currBinary % 5 == 0
	}
	return res
}
