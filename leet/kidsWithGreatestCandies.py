def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    greatest = -1
    res = []
    for kid in candies:
        greatest = max(greatest, kid)
    for kid in candies:
        res.append(kid + extraCandies >= greatest)
    return res
