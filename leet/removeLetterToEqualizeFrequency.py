def equalFrequency(word: str) -> bool:
    splitted = list(word)
    for i in range(len(splitted)):
        if countFreq(splitted[0:i] + splitted[i+1:]):
            return True
    return False


def countFreq(charList: list[str]) -> bool:
    occs = {}
    for c in charList:
        if c in occs:
            occs[c] += 1
        else:
            occs[c] = 1
    tot = set()
    for val in occs.values():
        tot.add(val)
    return len(tot) == 1
