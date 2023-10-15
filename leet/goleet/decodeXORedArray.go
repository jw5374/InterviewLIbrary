package main

func DecodeXorArray(encoded []int, first int) []int {
    var res []int = make([]int, len(encoded) + 1)
    res[0] = first
    for i, num := range encoded {
        res[i+1] = res[i] ^ num
    }
    return res
}
