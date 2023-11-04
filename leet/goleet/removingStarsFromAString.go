package main

func RemoveStars(s string) string {
    cStack := []rune{}
    for _, c := range s {
        if c == '*' {
            cStack = cStack[:len(cStack) - 1]
            continue
        }
        cStack = append(cStack, c)
    }
    return string(cStack)
}
