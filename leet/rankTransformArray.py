def arrayRankTransform(arr: list[int]) -> list[int]:
    sortPosition = arr.copy()
    sortPosition.sort()
    ranks = {}
    currRank = 1
    for num in sortPosition:
        if num not in ranks:
            ranks[num] = currRank
            currRank += 1
    for i in range(len(arr)):
        arr[i] = ranks[arr[i]]
    return arr
