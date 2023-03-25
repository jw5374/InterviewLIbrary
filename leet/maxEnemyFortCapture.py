def captureForts(forts: list[int]) -> int:
    i = 0
    maxForts = 0
    while i < len(forts)-1:
        if forts[i] == 1:
            j = i+1
            while forts[j] == 0 and j < len(forts)-1:
                j += 1
            if forts[j] != -1 or j == len(forts):
                i = j
                continue
            maxForts = max(maxForts, abs(i - j))
            i = j
        i += 1
    i = len(forts) - 1
    while i > 0:
        if forts[i] == 1:
            j = i-1
            while forts[j] == 0 and j > 0:
                j -= 1
            if forts[j] != -1 or j == -1:
                i = j
                continue
            maxForts = max(maxForts, abs(i - j))
            i = j
        i -= 1
    return max(maxForts - 1, 0)


print(captureForts([0,0,1,-1]))

