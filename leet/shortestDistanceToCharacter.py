def shortestToChar(s: str, c: str) -> list[int]:
    targetPos = []
    closest = 0
    res = [0] * len(s)
    for i, ch in enumerate(s):
        if ch == c:
            targetPos.append(i)
    for i, ch in enumerate(s):
        if len(targetPos) > 1 and closest < len(targetPos) - 1:
            mid = ((targetPos[closest + 1] - targetPos[closest]) // 2) + targetPos[closest]
            if closest < len(targetPos) - 1 and i > mid:
                closest += 1
        res[i] = abs(targetPos[closest] - i)
    return res
