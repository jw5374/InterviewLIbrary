package main

import "strings"

func ReverseWords(s string) string {
    var words []string = strings.Split(s, " ")
    for i, word := range words {
        words[i] = reverse(word)
    }
    return strings.Join(words, " ")
}

func reverse(s string) string {
    var split = strings.Split(s, "")
    var i, j int = 0, len(split) - 1
    for i < j {
        split[i], split[j] = split[j], split[i]
        i++
        j--
    }
    return strings.Join(split, "")
}

