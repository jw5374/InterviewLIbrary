package main

func MakeEqual(words []string) bool {
    occTable := [26]int{}
    for _, word := range words {
        for _, c := range word {
            occTable[c-97]++
        }
    }
    for _, occ := range occTable {
        if occ % len(words) != 0 {
            return false
        }
    }
    return true
}
