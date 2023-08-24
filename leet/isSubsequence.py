def isSubsequence(s: str, t: str) -> bool:
    enumeration = {}
    for i, c in enumerate(t):
        if c in enumeration:
            enumeration[c].append(i)
        else:
            enumeration[c] = [i]
    currInd = len(t)
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in enumeration:
            return False
        index = None
        while len(enumeration[s[i]]) != 0:
            index = enumeration[s[i]].pop()
            if index < currInd:
                break
        else:
            return False
        currInd = index
    return True
