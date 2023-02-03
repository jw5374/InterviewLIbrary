def titleToNumber(columnTitle: str) -> int:
    i = len(columnTitle) - 1
    res = 0
    while i >= 0:
        charVal = ord(columnTitle[i]) - 64
        res += (26 ** ((len(columnTitle) - 1) - i)) * charVal
        i -= 1
    return res


print(titleToNumber("FXSHRXW"))

