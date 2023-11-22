package main

func numSplits(s string) int {
	leftSplit := make(map[byte]int)
	rightSplit := make(map[byte]int)
	res := 0
	for i := 0; i < len(s); i++ {
		if _, exists := rightSplit[s[i]]; exists {
			rightSplit[s[i]]++
		} else {
			rightSplit[s[i]] = 1
		}
	}
	for i := 0; i < len(s); i++ {
		if val, _ := rightSplit[s[i]]; val > 0 {
			rightSplit[s[i]]--
		} else {
			delete(rightSplit, s[i])
		}
		leftSplit[s[i]] = 1
		if len(leftSplit) == len(rightSplit) {
			res++
		}
	}
	return res
}
