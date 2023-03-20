def countPrefixes(words: list[str], s: str) -> int:
    prefs = {}
    currPref = ""
    res = 0
    for pref in words:
        if pref in prefs:
            prefs[pref] += 1
        else:
            prefs[pref] = 1
    for i in range(len(s)):
        currPref += s[i]
        if currPref in prefs:
            res += prefs[currPref]
    return res


print(countPrefixes(["a","a"], "aa"))

