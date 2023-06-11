def makeEqual(words: list[str]) -> bool:
    if len(words) == 1:
        return True
    occs = {}
    for word in words:
        for c in word:
            if c in occs:
                occs[c] += 1
            else:
                occs[c] = 1
    vals = set(occs.values())
    for val in vals:
        if val % len(words) != 0:
            return False
    return True
