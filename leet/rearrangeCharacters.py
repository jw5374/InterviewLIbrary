def rearrangeCharacters(s: str, target: str) -> int:
    sChars = {}
    targetChars = {}
    for c in s:
        if c in sChars:
            sChars[c] += 1
        else:
            sChars[c] = 1
    for c in target:
        if c in targetChars:
            targetChars[c] += 1
        else:
            targetChars[c] = 1
    res = len(s)
    for val, num in targetChars.items():
        if val not in sChars:
            return 0
        res = min(sChars[val] // num, res)
    return res


print(rearrangeCharacters("aabbaccaddaeea", "aaaaa"))

