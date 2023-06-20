def longestPalindrome(s: str) -> int:
    occs = {}
    maxOdd = -1
    res = 0
    for c in s:
        if c in occs:
            occs[c] += 1
        else:
            occs[c] = 1
    flag = True
    for val in occs.values():
        if val % 2 != 0 and val > maxOdd:
            maxOdd = val
    for val in occs.values():
        print(maxOdd, val)
        if flag and val == maxOdd:
            res += val
            flag = False
            continue
        if val % 2 == 0:
            res += val
        else:
            res += val - 1
    return res
