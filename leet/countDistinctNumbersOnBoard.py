# You are given a positive integer n, that is initially placed on a board. Every day, for 10^9 days, you perform the following procedure:
# For each number x present on the board, find all numbers 1 <= i <= n such that x % i == 1.
# Then, place those numbers on the board.
# Return the number of distinct integers present on the board after 10^9 days have elapsed.
# Once a number is placed on the board, it will remain on it until the end.
# % means modulo

def distinctIntegers(n: int) -> int:
    return n - 1 if n > 1 else 1


print(distinctIntegers(35))

