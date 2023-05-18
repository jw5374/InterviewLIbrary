def sortedSquares(nums: list[int]) -> list[int]:
    squares = []
    for num in nums:
        squares.append(num**2)
    squares.sort()
    return squares
