def minLength(s: str) -> int:
    splitted = list(s)
    i = 0
    while i < len(s) - 1:
        if splitted[i] == "":
            i += 1
            continue
        j = i
        k = i + 1
        while j >= 0 and k < len(s):
            subStr = f"{splitted[j]}{splitted[k]}"
            if subStr != "AB" and subStr != "CD":
                break
            splitted[j] = ""
            splitted[k] = ""
            while j >= 0 and splitted[j] == "":
                j -= 1
            while k < len(s) and splitted[k] == "":
                k += 1
        i += 1
    return len("".join(splitted))
