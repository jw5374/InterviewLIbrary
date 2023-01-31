def heightChecker(heights: list[int]) -> int:
    expected = sorted(heights)
    res = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    return res


print(heightChecker([1,2,3,4,5]))

