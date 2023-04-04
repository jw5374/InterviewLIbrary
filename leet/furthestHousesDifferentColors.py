def maxDistance(colors: list[int]) -> int:
    maxDist = 0
    [left, right] = [colors[0], colors[-1]]
    if left != right:
        return len(colors) - 1
    for i in range(1, len(colors)-1):
        if colors[i] != left:
            maxDist = max(maxDist, i)
        if colors[i] != right:
            maxDist = max(maxDist, (len(colors) - 1) - i)
    return maxDist


print(maxDistance([1,1,1,6,1,1,1]))

