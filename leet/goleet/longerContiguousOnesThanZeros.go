package main

import "math"

func CheckZeroOnes(s string) bool {
    if s == "1" {
        return true
    }
    var (
        longestOne int = 0
        longestZero int = 0
        i int = 0
    )

    for i < len(s) {
        currStreak := 0
        j := i
        for j < len(s) - 1 && s[j] == s[j+1] {
            currStreak++
            j++
        }
        switch string(s[i]) {
            case "1":
            longestOne = int(math.Max(float64(currStreak), float64(longestOne)))
            case "0":
            longestZero = int(math.Max(float64(currStreak), float64(longestZero)))
        }
        i = j + 1
    }
    return longestOne > longestZero
}
