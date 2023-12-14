package main

func SplitWordsBySeparator(words []string, separator byte) []string {
	res := []string{}
	for _, word := range words {
		res = append(res, splitString(word, separator)...)
	}
	return res
}

func splitString(word string, sep byte) []string {
	currSep := 0
	for currSep < len(word) && word[currSep] == sep {
		currSep++
	}
	i := currSep + 1
	res := []string{}
	for i < len(word) && currSep < len(word) {
		c := word[i]
		if c == sep && word[currSep] != sep {
			res = append(res, word[currSep:i])
			currSep = i + 1
			for currSep < len(word) && word[currSep] == sep {
				currSep++
			}
			i = currSep
		}
		i++
	}
	remainder := word[currSep:]
	if len(remainder) > 0 {
		res = append(res, remainder)
	}
	return res
}
