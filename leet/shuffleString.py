def restoreString(s: str, indices: list[int]) -> str:
    res = [""] * len(s)
    for i, ch in enumerate(s):
        res[indices[i]] = ch
    return "".join(res)


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

