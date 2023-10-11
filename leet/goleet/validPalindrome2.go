package main

import (
	"fmt"
	"strings"
)

func ValidPalindrome(s string) bool {
    var splitted = strings.Split(s, "")
    var i, j int = 0, len(splitted) - 1
    var flag = false
    for i < j {
        fmt.Println(splitted[i], splitted[j], i, j)
        if splitted[i] == splitted[j] {
            i++
            j--
            continue
        }
        if flag == true {
            break
        }
        switch true {
            case splitted[i+1] == splitted[j]:
            i++
            default:
            j--
        }
        flag = true
    }
    if i >= j {
        return true
    }
    // because screw you leetcode
    flag = false
    i, j = 0, len(splitted) - 1
    for i < j {
        fmt.Println(splitted[i], splitted[j], i, j)
        if splitted[i] == splitted[j] {
            i++
            j--
            continue
        }
        if flag == true {
            return false
        }
        switch true {
            case splitted[i] == splitted[j-1]:
            j--
            default:
            i++
        }
        flag = true
    }
    return true
}
