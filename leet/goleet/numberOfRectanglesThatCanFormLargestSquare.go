package main

import "math"

func CountGoodRectangles(rectangles [][]int) int {
    var maxLens map[int]int = make(map[int]int)
    var currMax int = -1
    for _, rect := range rectangles {
        maxLen := int(math.Min(float64(rect[0]), float64(rect[1])))
        if maxLen > currMax {
            currMax = maxLen
        }
        if _, exists := maxLens[maxLen]; exists == true {
            maxLens[maxLen]++
        } else {
            maxLens[maxLen] = 1
        }
    }
    return maxLens[currMax]
}
