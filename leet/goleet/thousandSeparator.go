package main

import (
	"strconv"
	"strings"
)

func ThousandSeparator(n int) string {
	numRunes := strconv.Itoa(n)
	res := []string{}

	for i := len(numRunes) - 1; i >= 0; i -= 3 {
		if i - 3 < 0 {
			res = append([]string{ numRunes[:i+1] }, res...)
			continue
		}
		res = append([]string{ numRunes[i-2:i+1] }, res...)
	}
	return strings.Join(res, ".")
}
