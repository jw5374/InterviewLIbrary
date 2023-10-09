package main

import "strings"

func FurthestDistanceFromOrigin(moves string) int {
    var (
        choice int = 0
        currentPos int = 0
    )
    for _, n := range strings.Split(moves, "") {
        switch n {
            case "L":
            currentPos++
            case "R":
            currentPos--
            default:
            choice++
        }
    }
    switch true {
        case currentPos < 0:
        return (currentPos * -1) + choice
        case currentPos > 0:
        return currentPos + choice
        default:
        return choice
    }
}
