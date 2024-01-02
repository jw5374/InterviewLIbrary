package main

func MaxLengthBetweenEqualCharacters(s string) int {
    equalChars := make(map[rune][]int)
    longest := -1
    for i, c := range s {
        if val, exists := equalChars[c]; exists {
            equalChars[c] = append(val, i)
        } else {
            equalChars[c] = []int{ i }
        }
    }
    for _, indices := range equalChars {
        if len(indices) < 2 {
            continue
        }
        subLength := indices[len(indices) - 1] - indices[0] - 1
        if subLength > longest {
            longest = subLength
        }
    }
    return longest
}
