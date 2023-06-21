def repeatedSubstringPattern(s: str) -> bool:
    newstr = s * 2
    for i in range(1, len(s)):
        if s == newstr[i:i + len(s)]:
            return True
    return False
