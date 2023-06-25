def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    secondNums = {}
    res = 0
    for num in arr2:
        secondNums[num] = True
    for num in arr1:
        for val in range(num-d, num + d + 1):
            if val in secondNums:
                res += 1
                break
    return len(arr1) - res
