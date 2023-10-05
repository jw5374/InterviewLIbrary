package main

import "strings"

func DiStringMatch(s string) []int {
    var (
        chars []string = strings.Split(s, "")
        currInd int = 0
        res []int = make([]int, len(s) + 1)
    )
    var left, right int = 0, len(s)
    for _, char := range chars {
        switch char {
            case "D":
                res[currInd] = right
                right--
            case "I":
                res[currInd] = left
                left++
        }
        currInd++
    }
    res[currInd] = left
    return res
}
