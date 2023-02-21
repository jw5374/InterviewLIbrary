import math


def pickGifts(gifts: list[int], k: int) -> int:
    gifts.sort(reverse=True)
    i = 0
    while i < k:
        gifts[0] = math.floor(math.sqrt(gifts[0]))
        gifts.sort(reverse=True)
        i += 1
    return sum(gifts)


print(pickGifts([1, 1, 1, 1], 4))

