def digitSum(s: str, k: int) -> str:
    res = s
    while len(res) > k:
        leftover = len(res) % k
        digitsGroup = [[int(c) for c in res[x:x+k]] for x in range(0, len(res) - leftover, k)]
        new = ""
        for digits in digitsGroup:
            new += str(sum(digits))
        if leftover != 0:
            new += str(sum([int(c) for c in res[-leftover:]]))
        res = new
    return res
