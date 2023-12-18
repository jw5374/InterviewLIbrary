package main

func DifferenceOfSums(n int, m int) int {
	totalSum, divSum := 0, 0
	for i := 1; i < n + 1; i++ {
		totalSum += i
		if i % m == 0 {
			divSum += i
		}
	}
	divSum *= 2
	return totalSum - divSum
}
