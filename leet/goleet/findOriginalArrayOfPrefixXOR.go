package main

func FindArray(pref []int) []int {
    var res []int = make([]int, len(pref))
    res[0] = pref[0]
    for i := 1; i < len(pref); i++ {
        res[i] = pref[i] ^ pref[i-1]
    }
    return res
}
