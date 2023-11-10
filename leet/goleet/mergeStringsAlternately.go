package main

import "strings"

func MergeAlternately(word1, word2 string) string {
	res := make([]string, (len(word1) + len(word2)) * 2)
	i := 0
	for _, c := range word1 {
		if i < len(res) {
			res[i] = string(c)
			i += 2
		}
	}
	i = 1
	for _, c := range word2 {
		if i < len(res) {
			res[i] = string(c)
			i += 2
		}
	}
	return strings.Join(res, "")
}
