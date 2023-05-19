def numberOfLines(widths: list[int], s: str) -> list[int]:
    limit = 100
    res = [0, 0]
    for c in s:
        limit -= widths[ord(c) - 97]
        if limit == 0:
            limit = 100
            res[0] += 1
        elif limit <= 0:
            limit = 100 - widths[ord(c) - 97]
            res[0] += 1
    if limit != 100:
        res[0] += 1
        res[1] = 100 - limit
    else:
        res[1] = limit
    return res
