def makeFancyString(s: str) -> str:
    s = list(s)
    counter = ['', 0]
    for i, c in enumerate(s):
        if counter[0] != c:
            counter = [c, 1]
        else:
            counter[1] += 1
        if counter[1] >= 3:
            s[i] = ""
    return "".join(s)
