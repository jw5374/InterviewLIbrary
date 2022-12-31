def countAsterisks(s: str) -> int:
    sections = s.split("|")
    flag = True
    res = 0
    for section in sections:
        if flag:
            for c in section:
                if c == "*":
                    res += 1
        flag = not flag
    return res


print(countAsterisks("yo|uar|e**|b|e***au|tifu|l"))

