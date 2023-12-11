package main

func IsFascinating(n int) bool {
    digits := [9]int{}
    for i := 1; i < 4; i++ {
        currNum := i * n
        for currNum > 0 {
            ind := (currNum % 10) - 1
            if ind == -1 {
                return false
            }
            if digits[ind] != 0 {
                return false
            }
            digits[ind]++
            currNum /= 10
        }
    }
    return true
}
