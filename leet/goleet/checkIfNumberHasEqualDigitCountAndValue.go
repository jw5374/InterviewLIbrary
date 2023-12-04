package main

func DigitCount(num string) bool {
	digits := [10]int{}
	for _, digit := range num {
		digits[digit - 48]++
	}
	for i, digit := range num {
		digitVal := int(digit - 48)
		if digitVal != digits[i] {
			return false
		}
	}
	return true
}
