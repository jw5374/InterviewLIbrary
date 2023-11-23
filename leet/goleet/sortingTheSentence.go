package main

import "strings"

func SortSentence(s string) string {
	words := strings.Split(s, " ")
	res := make([]string, len(words))
	for _, word := range words {
		wordPos := len(word) - 1
		res[word[wordPos] - 49] = string(word[:wordPos])
	}
	return strings.Join(res, " ")
}
