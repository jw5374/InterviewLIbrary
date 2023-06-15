def countBinarySubstrings(s: str) -> int:
    i = 0
    res = 0
    while i < len(s) - 1:
        [left, right] = [i, i + 1]
        [leftCh, rightCh] = [s[left], s[right]]
        while (left >= 0 and right < len(s)):
            if not (s[left] != s[right]) or not (s[left] == leftCh and s[right] == rightCh):
                break
            res += 1
            left -= 1
            right += 1
        i += 1
    return res
