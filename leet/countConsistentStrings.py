def countConsistentStrings(allowed: str, words: list[str]) -> int:
    allowedHash = {}
    res = 0
    for c in allowed:
        allowedHash[c] = True
    for word in words:
        valid = True
        for c in set(list(word)):
            if c not in allowedHash:
                valid = False
                break
        if valid:
            res += 1
        valid = True
    return res


print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))

