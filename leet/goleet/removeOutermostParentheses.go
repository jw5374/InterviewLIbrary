package main

import "strings"

func RemoveOutParentheses(s string) string {
	comp := 0
	stack := 0
	res := []string{}
	for i, p := range s {
		if p == '(' {
			stack++
			continue
		}
		stack--
		if stack == 0 {
			res = append(res, s[comp+1:i])
			comp = i + 1
		}
	}
	return strings.Join(res, "")
}
