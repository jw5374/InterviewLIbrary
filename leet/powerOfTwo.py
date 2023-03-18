def isPowerOfTwo(n: int) -> bool:
    return (n > 0) and (n & (n - 1) == 0)


print(isPowerOfTwo(3))

