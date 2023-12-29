def xorOperation(n: int, start: int) -> int:
    res = start
    for i in range(start + 2, start + 2*n, 2):
        res ^= i
    return res
