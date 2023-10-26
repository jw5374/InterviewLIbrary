package main

func CountGoodSubstrings(s string) int {
    var res int = 0
    for i := 0; i < len(s) - 2; i++ {
        if !isGoodSubstring(string(s[i:i + 3])) {
            continue
        }
        res++
    }
    return res
}

func isGoodSubstring(s string) bool {
    return string(s[0]) != string(s[1]) && string(s[1]) != string(s[2]) && string(s[0]) != string(s[2])
}
