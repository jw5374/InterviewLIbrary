def freqAlphabets(s: str) -> str:
    splitted = [int(x) if x != "#" else x for x in s]
    res = ""
    i = 0
    while i < len(splitted):
        if i >= len(splitted) - 2 or splitted[i+2] != "#":
            res += chr(splitted[i] + 96)
            i += 1
        else:
            res += chr(splitted[i] * 10 + splitted[i+1] + 96)
            i += 3
    return res
