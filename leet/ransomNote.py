def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomOccs = {}
    magOccs = {}
    for c in ransomNote:
        if c in ransomOccs:
            ransomOccs[c] += 1
        else:
            ransomOccs[c] = 1
    for c in magazine:
        if c in magOccs:
            magOccs[c] += 1
        else:
            magOccs[c] = 1
    for c, occ in ransomOccs.items():
        if c not in magOccs:
            return False
        if magOccs[c] < occ:
            return False
    return True
