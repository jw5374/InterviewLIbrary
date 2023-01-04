def replaceDigits(s: str) -> str:
    chars = list(s)
    for i in range(1, len(chars), 2):
        chars[i] = shiftChar(chars[i-1],  int(chars[i]))
    return "".join(chars)


def shiftChar(c: str, x: int) -> str:
    return chr(ord(c) + x)


print(replaceDigits("a1b2c3d4e"))

