def repeatedCharacter(s: str) -> str:
    chars = {}
    for c in s:
        if c in chars:
            return c
        else:
            chars[c] = True
