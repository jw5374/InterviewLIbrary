package main

import "regexp"

func NumDifferentIntegers(word string) int {
	numsPattern := regexp.MustCompile(`[0-9]+`)
	numsRemoveZero := regexp.MustCompile(`[1-9]`)
	numsString := numsPattern.FindAllString(word, -1)
	uniqueNums := make(map[string]struct{})
	for _, num := range numsString {
		if num == "0" {
			uniqueNums[num] = struct{}{}
			continue
		}
		zeros := numsRemoveZero.FindStringIndex(num)
		if zeros == nil {
			uniqueNums["0"] = struct{}{}
			continue
		}
		removedZeros := num[zeros[0]:]
		uniqueNums[removedZeros] = struct{}{}
	}
	return len(uniqueNums)
}
