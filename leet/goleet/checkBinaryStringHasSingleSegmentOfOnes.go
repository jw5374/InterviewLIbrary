package main

func CheckOnesSegment(s string) bool {
    var i int = 0
    var segment bool = false
    for i < len(s) {
        if string(s[i]) == "1" {
            if segment {
                return false
            }
            for i < len(s) && string(s[i]) == "1" {
                i++
            }
            segment = true
            continue
        }
        i++
    }
    return true
}
