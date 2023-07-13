def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    res = 0
    [i, j] = [0, 0]
    while j < len(s) and i < len(g):
        if g[i] <= s[j]:
            res += 1
            i += 1
            j += 1
        else:
            j += 1
    return res
