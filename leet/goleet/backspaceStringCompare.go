package main

func BackspaceCompare(s string, t string) bool {
    return decodeBackspaceString(s) == decodeBackspaceString(t)
}

func decodeBackspaceString(s string) string {
    var res []rune
    for _, c := range s {
        if string(c) == "#" && len(res) == 0 {
            continue
        }
        if string(c) == "#" {
            res = res[:len(res) - 1]
            continue
        }
        res = append(res, c)
    }
    return string(res)
}
