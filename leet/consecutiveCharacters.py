def maxPower(s: str) -> int:
    if len(s) == 1:
        return 1
    i = 0
    power = 0
    while i < len(s) - 1:
        local = i
        while local < len(s) - 1 and s[local] == s[local+1]:
            local += 1
        power = max(power, local - i + 1)
        i = local + 1
    return power


print(maxPower("abbcccddddeeeeedcba"))

