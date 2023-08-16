def trimMean(arr: list[int]) -> float:
    sortedArray = sorted(arr)
    percentage = len(arr) // 20
    return sum(sortedArray[percentage:len(sortedArray) - percentage]) / (len(sortedArray) - (2 * percentage))
