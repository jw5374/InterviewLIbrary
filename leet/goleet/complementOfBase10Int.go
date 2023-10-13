package main

import "strconv"

func BitwiseComplement(n int) int {
    var bits int = len(strconv.FormatInt(int64(n), 2))
    return (n ^ (1 << bits - 1))
}
