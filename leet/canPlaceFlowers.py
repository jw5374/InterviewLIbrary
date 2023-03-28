def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if len(flowerbed) == 1 and flowerbed[0] == 0 or n == 0:
        return True
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        n -= 1
        flowerbed[0] = 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        n -= 1
        flowerbed[-1] = 1
    for i in range(1, len(flowerbed) - 1):
        [left, right] = [flowerbed[i-1], flowerbed[i+1]]
        if left == 0 and right == 0 and flowerbed[i] != 1:
            flowerbed[i] = 1
            n -= 1
    return n <= 0


print(canPlaceFlowers([1,0,0,0,1], 2))

