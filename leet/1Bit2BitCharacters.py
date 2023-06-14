def isOneBitCharacter(bits: list[int]) -> bool:
    i = 0
    while i < len(bits)-1:
        if bits[i]:
            i += 2
        else:
            i += 1
    return i == (len(bits) - 1)
