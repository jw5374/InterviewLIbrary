def fib(n: int) -> int:
    [left, right] = [0, 1]
    for i in range(n):
        temp = left + right
        left = right
        right = temp
    return left


print(fib(4))

