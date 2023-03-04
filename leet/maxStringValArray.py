def maximumValue(strs: list[str]) -> int:
    res = 0
    for str in strs:
        if str.isdigit():
            res = max(res, int(str))
        else:
            res = max(res, len(str))
    return res


print(maximumValue(["1","01","001","0001"]))

