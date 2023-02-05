def divideString(s: str, k: int, fill: str) -> list[str]:
    res = []
    for i in range(0, len(s), k):
        isEnd = i + k > len(s) - 1
        if isEnd:
            res.append(s[i:] + fill * ((i + k) - len(s)))
        else:
            res.append(s[i:i+k])
    return res


print(divideString("a", 3, "x"))

