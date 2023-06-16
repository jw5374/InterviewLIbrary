def isLongPressedName(name: str, typed: str) -> bool:
    if len(name) > len(typed):
        return False
    [i, j] = [0, 0]
    while i < len(name) and j < len(typed):
        startName = 1
        startTyped = 0
        if name[i] != typed[j]:
            return False
        while j < len(typed) and typed[j] == name[i]:
            startTyped += 1
            j += 1
        while i < len(name) - 1 and name[i] == name[i+1]:
            startName += 1
            i += 1
        if startName > startTyped:
            return False
        i += 1
    return j == len(typed) and i == len(name)
