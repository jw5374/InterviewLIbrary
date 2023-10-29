package main

func BreakPalindrome(palindrome string) string {
    if len(palindrome) == 1 {
        return ""
    }
    i := 0
    for i < len(palindrome) {
        if string(palindrome[i]) == "a" || i == (len(palindrome) / 2) {
            i++
            continue
        }
        break
    }
    if i == len(palindrome) {
        return string(palindrome[:len(palindrome) - 1]) + "b"
    }
    return string(palindrome[:i]) + "a" + string(palindrome[i+1:])
}
