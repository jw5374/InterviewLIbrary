def minDeletionSize(strs: list[str]) -> int:
    toDel = 0
    for i in range(len(strs[0])):
        invalid = False
        for j in range(len(strs)-1):
            if ord(strs[j][i]) > ord(strs[j+1][i]):
                invalid = True
                break
        if invalid:
            toDel += 1
    return toDel
