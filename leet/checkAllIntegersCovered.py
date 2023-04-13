def isCovered(ranges: list[list[int]], left: int, right: int) -> bool:
    ranges.sort(key=lambda x: x[0])
    [min, max] = [ranges[0][0], ranges[0][1]]
    for range in ranges:
        if range[0] <= max+1 and range[1] >= max:
            max = range[1]
            if min <= left and max >= right:
                return True
        elif range[0] > max+1:
            min = range[0]
            max = range[1]
    if min <= left and max >= right:
        return True
    return False


print(isCovered([[15,36],[15,23],[15,44],[30,49],[2,19],[27,36],[7,42],[12,41]], 19, 47))

