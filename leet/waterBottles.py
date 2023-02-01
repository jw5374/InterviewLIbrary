def numWaterBottles(numBottles: int, numExchange: int) -> int:
    res = numBottles
    while numBottles >= numExchange:
        res += numBottles // numExchange
        numBottles = (numBottles // numExchange) + (numBottles % numExchange)
    return res


print(numWaterBottles(1, 2))

