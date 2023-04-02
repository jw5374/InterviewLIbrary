def canFormArray(arr: list[int], pieces: list[list[int]]) -> bool:
    if len(arr) == 1:
        return pieces[0][0] == arr[0]
    segments = {}
    for piece in pieces:
        segments[piece[0]] = piece
    i = 0
    while i < len(arr) - 1:
        currKey = arr[i]
        if currKey not in segments:
            return False
        j = 0
        while j < len(segments[currKey]) and segments[currKey][j] == arr[i]:
            j += 1
            i += 1
        if j != len(segments[currKey]):
            return False
    return True


print(canFormArray([49, 18, 16], [[16, 18, 49]]))

