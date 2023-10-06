package main

import (
	"strconv"
	"strings"
)

func SmallestNumber(pattern string) string {
    var (
        currI int = 0
        patChars []string = strings.Split(pattern, "")
        res []string = make([]string, len(pattern) + 1)
    )
    for currI < len(patChars) {
        switch patChars[currI] {
            case "D":
                right := currI + 1
                for right < len(patChars) && patChars[right] == "D" {
                    right++
                }
                temp := currI
                for temp < right {
                    res[currI] = strconv.Itoa(right+1)
                    currI++
                    right--
                }
                res[currI] = strconv.Itoa(temp + 1)
            case "I":
                res[currI] = strconv.Itoa(currI + 1)
        }
        currI++
    }
    if currI < len(res) {
        res[currI] = strconv.Itoa(currI + 1)
    }
    return strings.Join(res, "")
}
