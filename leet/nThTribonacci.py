def tribonacci(n: int) -> int:
    [a, b ,c] = [0, 1, 1]
    if n < 3:
        return [a, b, c][n]
    for i in range(n - 2):
        temp = a + b + c
        a = b
        b = c
        c = temp
    return c


print(tribonacci(3))

