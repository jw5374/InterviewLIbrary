def maxProfit(prices: list[int]) -> int:
    [buy, sell] = [0, 1]
    maxProf = 0
    while sell < len(prices):
        curr = prices[sell] - prices[buy]
        if curr < 0:
            buy = sell
        if curr > maxProf:
            maxProf = curr
        sell += 1
    return maxProf


print(maxProfit([7,1,5,3,6,4]))

