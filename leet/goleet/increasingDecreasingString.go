package main

func SortString(s string) string {
    var (
        alphaKey []int = make([]int, 26)
        filled bool = true
        res string = ""
    )
    for _, b := range []byte(s) {
        alphaKey[b-97]++
    }
    for filled {
        filled = false
        for i, val := range alphaKey {
            if val != 0 {
                filled = true
                res += string(i + 97)
                alphaKey[i]--
            }
        }
        if !filled {
            break
        }
        for i := len(alphaKey) - 1; i > -1; i-- {
            if alphaKey[i] != 0 {
                filled = true
                res += string(i + 97)
                alphaKey[i]--
            }
        }
    }
    return res
}
