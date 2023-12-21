package main

func FindWordsContaining(words []string, x byte) []int {
	res := []int{}
	for i, word := range words {
		if wordContains(word, x) {
			res = append(res, i)
		}
	}
	return res
}

func wordContains(word string, x byte) bool {
	for _, c := range []byte(word) {
		if c == x {
			return true
		}
	}
	return false
}
