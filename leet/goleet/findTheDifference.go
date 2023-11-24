package main

func FindTheDifference(s string, t string) byte {
	sChars := make(map[byte]int)
	tChars := make(map[byte]int)
	for _, c := range []byte(s) {
		if _, exists := sChars[c]; exists {
			sChars[c]++
		} else {
			sChars[c] = 1
		}
	}
	for _, c := range []byte(t) {
		if _, exists := tChars[c]; exists {
			tChars[c]++
		} else {
			tChars[c] = 1
		}
		if v, exists := sChars[c]; !exists || v < tChars[c] {
			return c
		}
	}
	return 0
}

