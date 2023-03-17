import math


def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    qlog = math.log(n, 4)
    return (4 ** math.ceil(qlog) == n) or (4 ** math.floor(qlog) == n)


print(isPowerOfFour(16))

