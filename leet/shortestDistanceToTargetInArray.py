def closestTarget(words: list[str], target: str, startIndex: int) -> int:
    targetInds = []
    res = len(words)
    for i, word in enumerate(words):
        if word == target:
            targetInds.append(i)
    if len(targetInds) <= 0:
        return -1
    for ind in targetInds:
        res = min(res, abs(startIndex - ind), abs((len(words) - ind) + startIndex), abs((len(words) - ind) + startIndex))
    return res


print(closestTarget(["a","b","c","d","f","g","leetcode","e"], "leetcode", 1))

