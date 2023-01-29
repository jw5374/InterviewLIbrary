def hammingDistance(x: int, y: int) -> int:
    diff = x ^ y
    res = 0
    for c in bin(diff):
        if c == "1":
            res += 1
    return res


print(hammingDistance(3, 1))

