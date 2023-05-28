def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    currMin = 1000000
    res = []
    for i in range(len(arr) - 1):
        if currMin > arr[i + 1] - arr[i]:
            res = []
            currMin = arr[i + 1] - arr[i]
        if arr[i + 1] - arr[i] == currMin:
            res.append([arr[i], arr[i + 1]])
    return res
