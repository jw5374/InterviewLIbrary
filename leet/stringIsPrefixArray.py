def isPrefixString(s: str, words: list[str]) -> bool:
    sChar = 0
    totalLength = 0
    for word in words:
        if len(s) - sChar < len(word):
            return False
        for i in range(len(word)):
            if s[sChar] != word[i]:
                return False
            sChar += 1
        totalLength += len(word)
        if len(s) == totalLength:
            break
    if sChar < len(s):
        return False
    return True


print(isPrefixString("iloveleetcode" ,["apple","i","love","leetcode"]))

