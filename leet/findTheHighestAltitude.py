def largestAltitude(gain: list[int]) -> int:
    currMax = 0
    runningSum = 0
    for alt in gain:
        runningSum += alt
        if runningSum > currMax:
            currMax = runningSum
    return currMax
