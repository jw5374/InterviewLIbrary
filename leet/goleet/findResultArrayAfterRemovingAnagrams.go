package main

func RemoveAnagrams(words []string) []string {
    i, j := 0, 1
    var res []string
    for i < len(words) {
        for j < len(words) && isAnagram(words[i], words[j]) {
            j++
        }
        j++
        res = append(res, words[i])
        i = j - 1
    }
    return res
}

// can be improved by using array instead of hash
func isAnagram(w1, w2 string) bool {
    if len(w1) != len(w2) {
        return false
    }
    o1 := make(map[string]int)
    o2 := make(map[string]int)
    for i, c := range w1 {
        if _, exists := o1[string(c)]; exists {
            o1[string(c)]++
        } else {
            o1[string(c)] = 1
        }
        if _, exists := o2[string(w2[i])]; exists {
            o2[string(w2[i])]++
        } else {
            o2[string(w2[i])] = 1
        }
    }
    for c, occ := range o1 {
        if occ2, exists := o2[c]; !exists || occ != occ2 {
            return false
        }
    }
    return true
}
